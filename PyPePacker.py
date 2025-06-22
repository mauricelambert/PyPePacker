#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################
#    This package implements a packer written in python, the packer reduce
#    the size (gzip compression), encrypt data (RC6 encryption) and reduce
#    data entropy (using EntropyEncoding).
#    Copyright (C) 2025  PyPePacker

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
###################

"""
This package implements a packer written in python, the packer reduce
the size (gzip compression), encrypt data (RC6 encryption) and reduce
data entropy (using EntropyEncoding).
"""

__version__ = "1.0.0"
__author__ = "Maurice Lambert"
__author_email__ = "mauricelambert434@gmail.com"
__maintainer__ = "Maurice Lambert"
__maintainer_email__ = "mauricelambert434@gmail.com"
__description__ = """
This package implements a packer written in python, the packer reduce
the size (gzip compression), encrypt data (RC6 encryption) and reduce
data entropy (using EntropyEncoding).
"""
__url__ = "https://github.com/mauricelambert/PyPePacker"

# __all__ = []

__license__ = "GPL-3.0 License"
__copyright__ = """
PyPePacker  Copyright (C) 2025  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""
copyright = __copyright__
license = __license__

from EntropyEncoding import entropy_encode2
from RC6Encryption import RC6Encryption

from os.path import basename, splitext, isdir, abspath
from sys import argv, executable, exit, stderr
from zipapp import create_archive
from base64 import b85decode
from string import Template
from gzip import compress
from os import mkdir

code = Template(
    """
from PyPeLoader import (
    load,
    get_peb,
    modify_process_informations,
    modify_executable_path_name,
    set_command_lines,
)
from RC6Encryption import RC6Encryption
from EntropyEncoding import entropy_decode2

from io import BytesIO
from gzip import decompress

rc6 = RC6Encryption(${key})

peb = get_peb()

modify_process_informations(peb, ${full_path}, ${command_line})
modify_executable_path_name(peb, ${module_name}, ${full_path})
set_command_lines(${command_line})

load(BytesIO(
    decompress(rc6.data_decryption_CBC(entropy_decode2(${packed_data}), ${iv}))
))
"""
)

executable_console = (
    b"O<Iru0{{R31ONa4|Nj60xBvhE00000KmY&$00000000000000000000000000000000000"
    b"00000fB*mh4j;M>0JI6sA-Dld%^_51X>%ZOa&KpHVQnB|VQy}3bRc47AaZqXAZczOL{C#7"
    b"ZEs{{E)5L|Bme*a00000P(=U$WQGO+000000000000000@Bl6X3jzWl01yBG02lxO00000"
    b"P!j+E01yBG0000$0RR9101yBG00IC21^@s6000001^@s6000000B`^R00aO4qXhu~0{~!w"
    b"000mG0000001yBG00000000mG0000001yBG00000000005C8xG00000000005GViuv;Y7A"
    b"08jt`-"
    b"~j*t06+i$i~#@u00000000000AK(BFaQ7mkRt#98~^|S00000000000000000000000000"
    b"0000P$B>TKmh;%000000000003ZMWpaB2?000000000000000000000000000000E_7vhb"
    b"N~PVoDKj001yBG01yBG00aO4000000000000000AOKKcE^=gHbYTDhtPTJG03ZMW01yBG0"
    b"2BZK000000000000000KmbrcE@WYJVE_OCI0gU!05AXm00IC203-"
    b"ka000000000000000Kmbs{E^uUFbYTDhi~#@u06+i$00IC2044wc000000000000000Kma"
    b"g6E^>2nV*mgE-"
    b"~j*t08jt`00IC204M+e000000000000000KmahnE^=jTZ({%eFaQ7m0AK(B00IC204e|g0"
    b"00000000000000Kmag8000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000KvhVC>@Y};Y$PB^iCrK_iG3(Yiv{i<002lc#Yl-"
    b"o0RI&k5dZ*4V+cr%49y4t002mhK@Uhf!FLKsxbXk~|NsC04@iUH@aTdK002lU;7E;pBq0A"
    b"4ybu5YNQ($aivdW92mck-"
    b"5C8y3V;KJxq!0iAOpC)vjZX+k!QcZ(ixB9S4FCZD6|)ck07#41iwOV0{}uKS002mfO#nzU"
    b"&FCrs002mfT_8w{eJDtcWe{D%%*@Qp%*@Qp%*@Qp%*@Qp%*<wH4<Cd800000NIMNN9{>P#"
    b"5J<tn5N7wm|NnIX!$`r&5b3G{007L)KvPJA>>#-"
    b"T0002!$_oGh=;H<e0E@`z^a}t0=*tEG0E^h@3=9AOxd8wG0ErmrL<9f;gurxj=syVn07#7"
    b"ubO`_e=-&kZ0O+Cy004`~=#dKm0ENJHQs|-"
    b"v008LW1^@tsz;p~qjSYSV008K13jhG<oCW{@=$8fn0O)E4004`~=${J!0O*1S004x*bOq>"
    b"D3jhG<PzC@1=o1J40ENJH21tX%AX~$^2LJ#7=(7d@0L;wHNQ3Ms=w}8105iZygTyGqNQ3M"
    b"s=sySm0O%G5004`~NQ1;E=}ij&0L;wHNQqn|2uO)^BoJ3fgX}Q50RR91=r02R0EEB~gf;;"
    b"H06;SKK!|iCAn4u#004^Eiw&kD004ve0S|;D0RRAn$#qJ{1&<>D0096107#7$;12)*NR17"
    b"_4*&q@x(WaQg}`(Qxc>kE0O{EP002mh6`v0P07#7uhz|e&=#vTn0LKMUBLDyb0002%2tc+"
    b"0K!|iCAd1WA90ULW=*tBF07#42NP{>4bRI~H$mnhZ004x*bP`1~z(I{r0yD`-"
    b"iv#}^6b}FZ=%)n$07#42NP{>4bQDO7$ml`?004x*bO=a`3+Pk|008J83IG5|i}>j62><{{"
    b"ix}wZ2><|0i^oWd(~Ah`ApQUUi`eMJ1^@trz;snWg!Xj>=n)D405j6D0qC*=004`_>lusK"
    b"=%WSz0EEDFJAiy7AOLj*=<^8x0E@#&i(Di?NQ-nNNJxXkFki#D2LJ#7=pzLH0Fb!{0002!"
    b"7zF?Ti_7S(2><|)i_7S%2><|)NQ3Ms=+^@P07!$xDCu(k|NqR)KvPJA>>x;s*)z%i6}t=o"
    b"07#3={}rkX0093Lv<v_MNQ=n22?PMZNQ1;6TS)&Us0;uANQq1&2uOqMIJp-"
    b"90093LoD2W}g}`(NxdH$H0L>{#jSV6l008Kz0000;i$o+iNQngr9smGHjYK3kNQ1x#NQni"
    b"R9RL7Giv{u>002md1!Eil07#2OBtS@s1!o-"
    b"q0LKMA8~^|b1OULt1veZ3009610LKME8~^|T0002E2mk;8NNd0VNR16S8~^}F#{>Za0002"
    b"E2mk;8NNd0VNQ({08vp=EiA)3_xCj6M07z@V0Z5AttQ!CTNQq1YAV`f3&<y|p=>Puz|44("
    b"xIK#}$KvPy%NQ3M^NQ>G36_X1907#3o_y7O^Gyg?1z(|c$Bw$F3&i@sG3jhE}g}`(<NP}b"
    b"~H~>hEOeAPXi&P|FOpC}!iA*FgOpC@yjZ7qPNQq1&C^N}OiCiQg{}oaT0095TgZ~12u}Fi"
    b"&Kwn;4!_3UgNQ3Ms=%)t&0ENJGA!SI51SK#4002mfNC@i%NIS@M6f?l^NDr|MtRMgYb?!3"
    b"2NQ1;E!>|GC_sq=9KvPJA>>v-"
    b"e1(zTI0ENlB0RR914@AR=1&1I20O+O#008K{0ssJnz;y&N!0Qy~umS)8gurzPGs)<s0ssK"
    b"(>WafigTx?P!_3UgKvPJA>>z+WOdtRN0E^jmXM_0xcWUSj2LJ$tz;q~u+jS&JjSV&+008K"
    b"d2LJ$tz;zHvjSW5^008KN2LJ$tz;rG$!0R(+4{rsD3;+N~gUJ8$4}S#(AOHYJi3JWI008q"
    b"3e+3R8002md1s5Oy0LBI39{>OWumMPe#2{P4xdi|K0O)1{007L)NQ3McOpC#|O<Di|W;q4"
    b"<>Hq(Act~RnEb9ONNR1Wg>Hq&o1ImFpP(=U$bzis(0ssJJIYAh8R7@+v54TYiNQ1%{NCVL"
    b"iw?PI-jSPTHjSR|2i4-"
    b"JBJJEC)i%JYkJHc`ai$Vwk!Av{AatKI+!YJ$CGtx+f(scwf!0Qx)dL#gS1Tw(u3a|m|1~S"
    b"0w0y4lzgTxraKvPJA>>!HS==TKx05j5sz;p|Q+jR#>hZPPV002mX#2{P4KvPJA>>z+W10M"
    b"hY0E*dk1ccIc4Cpoi004^1=q~{P0I&f_gTx?P!_3UgKvPJA>>x;kJ>DJw0RKpf*>wl#LIw"
    b"Z;>kmka(@2dC$Q}Ry=qm;Q05j5sz(@~7(@2ZLNQ1;6Tf@xENQ3Ms=)3>_|48@P8^HJ2|Hw"
    b"###3;keNQqn|AXP|<>_~&`AV`Y^#25eoNV_tk-"
    b"z}Ld002lk!*z5>gJl>1NR3Sx{}l!a002mfMHonlMG*fL@CX0^i@-=RMG*fL+z0>wi@-"
    b">YO&~}yMG*fL#0UTYi$x$vjZF|p!QdcBGesasGer<cGr>r?|NsC0|Nj60NF%{Wxig~QEtx"
    b"9-07yH-NDoB8NQnhO7ytlBi(Di~NcYf4i3KVc002mX#2{V6Gr+^lxB&nF0K?48xBx%^0K?"
    b"48NR15%9smGH|0Mzl007L)umQu&!T<owNR0&n9smHtNR0&n9smHtNQ3Ms=;#0c|44%fB<S"
    b"Y<|NlsX2m(lh#3;keGr&0o*cSi*50t>eNR0*Q9RL8sNR0*A9RL8sgC)rw0002PNQqn|2vt"
    b"aptRz7D|NlsV?7#&80E^kV7XSbN{}s*$004!+bOejb%_+G90002!#Q*>QGtx+nP4Gdu&;$"
    b"Sg=oJJ207#8Z@c$KQ2LJ#_i=F5I002mhmDmIT07#3=MKi$v6;}rU07!+vbUa9dWF$BMNR5"
    b"r)1ONa?i<Q^}002yj$ViDyBrr^i!$^&d=mY=&NQq1&C`gS>@JNYFBp@@%{}mnw002mfg~$"
    b"W|07#8YBv43+h3EhP05j4^jfKbr002R_m;e9(NQ1x#NQs4r0002!eggmiNQ;HY1ONa?i9{"
    b"q|$3!Gh6#xK0$3!Gl0RR91{}mbs004vd0Z5HRBv43+L?l2+jYaSel*34gL?lQv$^R9(1^@"
    b"s^jZ7p!{}rYN004!+bqs{tbqI|}1L(f~|NlsfoFvc%002mV#J~jr0A0h(=`;TS|IEzHNQ3"
    b"MsGs*uIPzC@1NQJ<3Ik`<*003q=2z4(=V@Nzm1IU3nP(=U$bs)G40ssJJIYAh86@$5i000"
    b"0Eb_|2L_y7O^01uVG>jE;sNQ1;E!_3UgNR15%0000;|0N;@007L)NQqn|2v<mh>>x;s8Ay"
    b"xyfjeV!ZQykrgL@bRbry?LAdQ0H`fTQd_yTqnf%*VInE`YSNQ+z~Ff+hNgTx?T!{|@~002"
    b"md7)Xm>2<S=z002md80gXh007L)NQqn|2v<mh>>x;u9dir-"
    b"07#8JYzzPZ>k>$d14xCybO!$w90vdZNQ1)&NITzh=}3!QBrr&W#2{b8NQqn|2v<mh>>x;u"
    b"9Y+iR07#8JKnwr?>k>$d14xCybO!$w;06EyNQ1)&NITzh=}3!QBrr&W#2{b8NQqn|5J-"
    b"u1Bp6pngX|D9z%$7YqC|_qMKjw(i_$@X@NRTvY(atYX>MgnM2pLd@H5FljY9!N3(yauL4o"
    b"l{Wo~te1SCZZ(TQ9n1dI8JOe6@2R3r>_TS$Wq;}ie@|0VE0{|`vV1<Mow004jh06oA40RV"
    b"I;Jzxd`0CXWea0UVZbQ%S)`TYNb_#k&ANVx$30RRC2002l2qrr0&M2iKP8UO%6gUA6yi3N"
    b"@t008R;M2iK58UO&e2LJ#7M2$%MJMeraGszF4i3B7>i`$7@Bm{{}BnXLABn%I_;|X&LMGL"
    b"`1i3L&`0074YJQM%`0RR91M2QVK6aWAZy5|%RgOLCL07QumBoqJuy9NLN0ErzP6aWAZy5}"
    b"2nc@Mhh9CLFs$qxb0NWtPDNDI(NiBu#YNQ*=yAR@y$!*y4S1@9980E5T~#|7RK00093004"
    b";v+!Fu*LH5HSbU1^^Ajbv86951O0001q1;Y~n0Js1E1JFbx*hD+nbr?vCL?j?2;5^`U4TB"
    b"A&6951}i5;2~002mfTqGznz(|X9Brr&W#1LP@Gr&0om=gd150${f%*@Qp|0U`J0093b>;n"
    b"J*|0V7N0093b$O8ZX|0P-"
    b"k0093bd;|ah|0Qk&0093bcmx0d|0VhZ0093b1Oxy8|0M<l0093b2m}BC|0N0p0093b3<Ll"
    b"G|0NCt0093b5Ci}K|0Qw+0093b6a)YO|0Na#0093b7z6+S|0SXW0093bi~|4w|0Pxg0093"
    b"bAOrva|0N;>0093bBm@8e|0N~_007L)NQ3MsO^ZP|NQ=rzi_z!}0002E0RR91NQ1;E!_3U"
    b"gKvPAF7)XoSL4)J?OpD1u_5cJ-i_vrwL5n~LO=D05_t;DW(MV&+Oe4`rW5Y^|6c9*@LlBE"
    b"d2uO=V2=+t)0}pfy54J=B1B2l3OasVFGs;Pe$y@0W^Z)<M%*@Qp%*<wH4<Cd800000NQ3M"
    b"UOo<dEOo?112u(BFOpR0|7)&eBO%FoTWlW14B@h4r08Km7a~5Vnf#Lx0O^urX@c;io#sdI"
    b"NJJWUWOp6pGOp9D32uOp(5X1i^WC8#H%*@Qp%*@Qp%*@Qp%*@Qp%*<wH4<Cd800000|KQB"
    b"b%*@Qp%*@Qp%*@Qp%*@Qp%*<wH4<Cd800000|0PNT002N$NQ3MkNQ>%7ivdWB(TfP^NdEu"
    b"-kVu2XAYH@EKvhVK>PU+LGs%HC1polR50t@+!Ck}500000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"000000000000000000000000000000000000000000000000000000000000000000o+|("
    b"V00000$SVK<00000ekuR}00000k}3cI00000tSSHi00000z$yR$00000+$sP700000`YHe"
    b"b000004l4iv00000A}as@00000J}UqK00000SStVk00000ZYux)00000gew3500000v?~A"
    b"r000000000000000HY@-"
    b"D00000qAmac00000>MH;M000000xSRk000007%Tt)000000000000000j4c2F000000000"
    b"000000b}aw^000000000000000kSqWI000000000000000q$~gc00000yet3!00000+$;b"
    b"900000{44+f000002rU2r000007A*h(000009xVU>00000QY-"
    b")f00000G%WxC00000J}m$M00000NG$*W00000ZY%%*00000U@QOt00000fGhw200000tSt"
    b"Zl00000$SnW>00000<ShUI00000@+|-"
    b"W000000000000000CM^H}00000oGkzV000000000000000Xes~z0000000000000001Q-"
    b"B70RR911Q-"
    b"B70RR91Kpp@<0RR91U>*QK0RR91U>*QK0RR9100000000009v%Qd0RR910000000000xDf"
    b"zA0RR9100000000000000000000@DKn%0RR91s1X1_0RR9100000000000000000000000"
    b"000000000000000000000000000KrjG60RR91;4lC{0RR91|NsC0|NsC0|NsC0|NsC0Kmh"
    b";%00000000000000000000000000000000000000000000000000000000000000000000"
    b"00000000000000000000000000000000000002rvLZ0RR9100000000000000000000pdk"
    b"Q20RR91upt0I0RR9100000000000000000000009610000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"000000000000000000000000000000000000003-"
    b"lF0RR9100000000000000000000s38DA0RR91xFG;Q0RR91z##xY0RR91$RPkg0RR91&>;"
    b"Xo0RR9100000^&@Fy000004FCWDgaQBnWF!CpWEcPd0000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"00000007ytkO0)PU57$g7yEC2uiL?i$JAOHXW!xI1iKNJ7}R1^RJ?Gyk20~G)OqZR-"
    b"F0vP}RG#LN@7aRZp92@`uW*h(j01yBGzyJUM@DKn1unPbHL>&MCd;kCdW*z_lHUIzsM?+L"
    b"h01yBGFb)6!E_7vhbR=zV00000FdhH^HUIzsE_7vhbR=zVBrq@lW*z_lHUIzsE_7vhbR>8"
    b"H03ZMWpaB2?E@@<8bYUbl00000pdkPNH~;_uE-)}-"
    b"W@i8Z*dYJ_2mk;8E<;jOBv?a100000;2{722mk;8E<;jOBv?a1K>z>%=pg_A2mk;8E<;jO"
    b"Bv?aQ00000@F4&I2mk;8E<;jOBv?s700000_#prQ2mk;8E<;jOBv?s7K>z>%03rYY2mk;8"
    b"E<;jOBv?s7LjV8(2qFLg2mk;8E<;jOBv?sW000005F!8o2mk;8E<;jOBv?>E000007$N`w"
    b"2mk;8E<;jOBv?>d00000AR+(&2mk;8E<;jOBv@2I00000C?Ws=2mk;8E<;jOBv@2h00000"
    b"Fd_f|&;bAdE^=gHbYTDh03-"
    b"kaWB>pFE^=gHbYUcRZ)|jJWB>pFWF!CpgaQBnE^=gHbYUcVdU|AHX8-"
    b"^I=q3OF2mk;8E^>5ZBuPO*00000@FoBN2mk;8E^>5ZBuQFY00000_$B}V2mk;8E^>5ZBve"
    b"5`0000004D$d2mk;8E^>5ZBve{j000002qypl2mt^9E_h^NbYTDh5GViupa1{>E@@<8bYU"
    b"bi00000uqXfk7ytkOE@@<8bYUbj00000$S42+paB2?E@@<8bYUbk00000Xes~zL<9f;E@@"
    b"<8bYUbm0000005AXmKmY&$E@WYJVE_OCKrjFR_yqs}E@E?Y0000006+i$i~#@uE^uUFbYT"
    b"Dh08jt`U;qFBE^>2nV<a#!00000U{C-"
    b"6fB^siE^>2nV<a##00000000000000000000000000000000000000000000086gKH6Lbj"
    b"x4>Sk>3nK<n0#E<|L>&MCAOHXW000000RR910R{p91~LLL0R#a61VR7+2@eJU4`c}d4>Sk"
    b">4^j(opd0`I0ssI2{Sg2F0uulLW*z_l0uulLHWL5<ND}}6W*z_l0uulL0R{p91~LLr0SN&"
    b"B31R>M0SE*D2yz5)17HF$2?PNE1R?+cpd0`I0RR91`xO8Hg%$t+gdP9@g%$t+0RjO40#E<"
    b"|0SyEI4KxV=4KfB$0Tl%R6*Rg46#=*a22cP10SW{F3N!`)3Ni+80S^WM4`c=a4>Sb;4-"
    b"yM-0RR91000000RR910RjO40x$po000000R#a61QGxMSSkPj0000000000aw-4-"
    b"kRbp7$S42+0000000000+$#V803ZMWNGSjS0000000000Kr8?NfFJ+>s3`yd0000000000"
    b"{w)9i;2;11m?;1N0000000000AT9s^&>#Q+Kq>$L0000000000KrR3Pcp(4)h$#R700000"
    b"00000U@iavz#sqscqsq?0000000000f-"
    b"V36upj^c000000000000000000000000000000o+|(V00000$SVK<00000ekuR}00000k}"
    b"3cI00000tSSHi00000z$yR$00000+$sP700000`YHeb000004l4iv00000A}as@00000J}"
    b"UqK00000SStVk00000ZYux)00000gew3500000v?~Ar000000000000000HY@-"
    b"D00000qAmac00000>MH;M000000xSRk000007%Tt)000000000000000j4c2F000000000"
    b"000000b}aw^000000000000000kSqWI000000000000000q$~gc00000yet3!00000+$;b"
    b"900000{44+f000002rU2r000007A*h(000009xVU>00000QY-"
    b")f00000G%WxC00000J}m$M00000NG$*W00000ZY%%*00000U@QOt00000fGhw200000tSt"
    b"Zl00000$SnW>00000<ShUI00000@+|-"
    b"W000000000000000CM^H}00000oGkzV000000000000000Xes~z000000000000000C<9P"
    b"=Urk|YZUAt3bZBpGGcIIoYyjy5Qgm!XVQ_SHa%DqrZggdMbO7-"
    b"LQgm!gZ*OaLa7J}*V{~b6Zbfc%a(Ms%_ykgPY*uM<bai2DRc?1_Ze#!e*acN?Xkl(-Y-"
    b"MCccw=R7bZKvHMrmwxWpV%jmjzR0bX9I>VQyq>Wn@KoV`Xr3X>V>uX>4?5asVm<M`d(Fb#"
    b"iiLZgfy`Z)0V1a{#slRAq8)X>MV3Wl(Z&V`X!5005o?NpnzgZ)0V1b8m7+Wnpx6a%E6*Wp"
    b"ib2bO2-"
    b"oQFUc<c~E6?W^ZzBVQyn(LvM9%bY*e?D*{JlbVGG=a%FCGP;zf$Wpi^$WB@M$M`d(Fb#ii"
    b"LZgf;=a%Ev;Nn`*30Ru;6bW?eAbY*Q+X>Daeb4F=wWmIWxWdMN#Np5L$X<=+>dSz2gX>)W"
    b")Wnp9hmjg+2L}g-"
    b"iXJ=({P;zB+Wo~o;i~>hxbWLw$b!=rwVQyq>Wmf<IOGQ#nMNBg?E@W(M000O8UtdFCb8uy"
    b"2X=Z6-Uua=&WNc+}000{RUteQ&a&l#EbYEq7V`Xr3X>V=-"
    b"8~|TmV|8+JWo~p|Wq4y{aCB*JZeL?>ZggdMbO1g8ZDnn9Wpn@lRzp%%PE<)vMKLrmE@W(M"
    b"000I6Ute%vUtf1&a%Xk`1OQ)Oa9>|vVRC0<002M$Uvp(>UuJ1+bY*g1Wq4%(LI7WLWprO*"
    b"aByFAd2nR_2>@STb7gdOb7gXEVRUF^a&iCw8312nZ*FF3XLWLAUw3I_WnW=(XLbMpH2_~}"
    b"ZfSIBVQgu7WnXt`WMyAvZgy#MZ*Fa6Zgc<uDF9z*WprO@ZfSIBVQgP_X=G(zWo~w9a&K;J"
    b"Wo~o;HUM8~ZfSIMWpZr*HvnI0ZfSIMWpZs_WdKzGWq4_H001KZUuAe{bO2NUUvp)2UuJD@"
    b"WMu#V764ykWq4_H000#LUt?cocxiM1Jpf;FWoKz~bY*g1bZByAVPs!yZ)0I>UuAe@Utx4*"
    b"cxiNBV_|G;Vqs%z000O8Ut@1>W@%@1XmVv?WNdF^VQggp764y!WprO|Wp`g~Z)9Zv0RUfL"
    b"a9>|zZ*6UFWMu#VGyq>|ZfSIBVQgu7WnXV@Wq4_HUvyz&Y-"
    b"IodJOE#EWoKz~bY*g1Z*FCHX>?y^b#7yHX>V=-"
    b"9splsa&%u|bY*yHbO2`nbY*gFX>MV3WdLDtX)SGYEq7^dEn{+YEpl~kbZKp6Eo?C@F)c7I"
    b"WNd5zVQ^_JZF4PmX>KiJa&#?iVRUFMY%wh{Eif)*Y-"
    b"|7kVQ^_JZF4PmX>KiJa&#?obYy97Eo?C@F)c7IWNd5zVQ^_JZF4PmX>KiJa&#?hZ)0I>Wi"
    b"4zmEio-HE@W(M003cdX)SGYEq7^dEn{+YEofz7a4l>xEio-HE@W(M002AyZDnm^aCra#00"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"000&0QeUX4L=xGNRutnJWMQ|NsC00RR910RR910ssI2000O80000000002000000RR9100"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"000000000000001yBGv=9IQ2qypl&=3Fs?hpU~C?@~_@DKn1rV#)DEGGZ}s1X1FxDfyVG$"
    b"#N6xDfyV(GdUuG$#N6)DZvxP!j+EJSPAEP!j+EViN!WG$#N6WD@`Ym=gd1EGGZ}m=gd1Y7"
    b"_tfd?x?^Y!m<h-4p--geL$1;1mD=85IBkG$#N692EcnWfcGbEGGZ}XcYhe^A!L9EGGZ}^c"
    b"4UAj1~X@kS72Dj1~X@uoeISEGGZ}uoeIS*%kl*EGGZ}+!g=;78d{jEGGZ}7#9ElFBbp+G$"
    b"#N6Fc$y-+!p`<xF-Mr7#IKmGZ+8>G$#N6SQr2RqZt4I#3uj%tQi0R{TToNG$#N65E=jgYZ"
    b"?Fm)F%J{Y#IOns2TtO)F%J{s2TtO<Qf0~)F%J{<Qf0~kQ@L2;3oh8L>&MCVI2SfG$#N6WE"
    b"}tiza0Po{3iea&>a8(9v%Py2q*vmKpp@9LLLAB@FxHOU>*PfW*z_l_$L4WW*z_lgdP9@bS"
    b"D4+gdP9@oE`uGuqOZj0000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"00000000000000000000000000000000000000000317ytkO7ytl(00000000000000000"
    b"0310RR91FaQ96000000000000000000312?PKDNB{r;U{C-"
    b"6eE|Rf00000000000000000000JU@7CY#?@Ja&u{KZapV4E-"
    b")t`Wo~0{WNB_^JttLEMlCoeAaitKZe(F>Z*FBhCwXOaCqF(73Or$Rb7gH}Y<VDfZES9HJt"
    b"uW?ZaQ;gXk~3-"
    b"b1iLYV{&hEZ)S8YV{dIbVRLORb}=U)ZDDR{W@U49R%LQ?X>V>lCowKCCq4}dARs(+a&>cb"
    b"Np5CuAb4$TZgV{%b#iVxb7N>_ZDDgQZE0h2Z*y;EbS-"
    b"0VZ8~9dZ7y~*B0dcYARr(hJac7Zb#iHRc|HvaARr(hARs()WpQ<7b97~7P;zN@X>4U@Wph"
    b"3a3LqdLARr(hAUtwqadl;LbY)~kcx7XCbZKvHOl5XuY#?l9c4cfmCt-"
    b"6*Zgy{LWpXDVb!kCkV`X!5Jtt;iY;$ENATK@*3LqdLARr(-"
    b"FLGsZb!BsOWn@rtX?AIBWoKn`J`D;WARr(-"
    b"FLPyMb#iHRc|HvaARs(1baHibbV+VzZ$1qQJTGB$b7gH}Y<WHn3IG5A000000000000000"
    b"000000000000000000000000003ZMWFaQ7mprNRtu%Wo2z@gBg;Gy`T0HQFWIHIVcz@o^a"
    b"P@`z0aHDvmfTM_`0000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"0000000000000000000000000000000000000000000000000000000000000000000000"
    b"00000000000000000000000000000000000"
)


def main() -> int:
    """
    This is the main function to start the program from command line.
    """

    print(copyright)
    argc = len(argv)
    argc_4 = argc != 3

    if argc_4 and argc != 4:
        print(
            'USAGES: "',
            executable,
            '"',
            *("" if executable.endswith(argv[0]) else (' "', argv[0], '" ')),
            "[executables path] [command line] (key)",
            sep="",
            file=stderr,
        )
        return 1

    _, path, command_line, *key = argv
    full_path = abspath(path)

    if argc_4:
        key = key[0].encode()
    else:
        key = b"$up3rP4$$w0rd"

    module_name = basename(full_path)

    rc6 = RC6Encryption(key)
    with open(path, "rb") as file:
        iv, data = rc6.data_encryption_CBC(compress(file.read()))

    data = repr(entropy_encode2(data))
    iv = repr(iv)
    key_repr = repr(key)
    packed_code = code.safe_substitute(
        key=key_repr,
        packed_data=data,
        iv=iv,
        module_name=repr(module_name),
        full_path=repr(full_path),
        command_line=repr(command_line),
    )
    filename = splitext(basename(path))[0] + "_packed"

    with open("./" + filename + ".py", "w") as file:
        file.write(packed_code)

    if not isdir(filename):
        mkdir(filename)

    with open("./" + filename + "/__main__.py", "w") as file:
        file.write(packed_code)

    create_archive(filename)

    with open("./" + filename + ".exe", "wb") as exe:
        with open("./" + filename + ".pyz", "rb") as file:
            exe.write(b85decode(executable_console) + file.read())

    return 0


if __name__ == "__main__":
    exit(main())
