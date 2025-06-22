![PyPePacker Logo](https://mauricelambert.github.io/info/python/security/PyPePacker_small.png "PyPePacker logo")

# PyPePacker

## Description

This package implements a packer written in python, the packer reduce
the size (gzip compression), encrypt data (RC6 encryption) and reduce
data entropy (using EntropyEncoding).

## Requirements

This package require:

 - python3
 - python3 Standard Library
 - PyPeLoader >= 1.0.0
 - RC6Encryption >= 1.0.1
 - EntropyEncoding >= 0.0.5

## Installation

### Pip

```bash
python3 -m pip install PyPePacker
```

### Git

```bash
git clone "https://github.com/mauricelambert/PyPePacker.git"
cd "PyPePacker"
python3 -m pip install .
```

### Wget

```bash
wget https://github.com/mauricelambert/PyPePacker/archive/refs/heads/main.zip
unzip main.zip
cd PyPePacker-main
python3 -m pip install .
```

### cURL

```bash
curl -O https://github.com/mauricelambert/PyPePacker/archive/refs/heads/main.zip
unzip main.zip
cd PyPePacker-main
python3 -m pip install .
```

## Usages

### Command line

```bash
PyPePacker              # Using CLI package executable
python3 -m PyPePacker   # Using python module
python3 PyPePacker.pyz  # Using python executable
PyPePacker.exe          # Using python Windows executable

PyPePacker C:\Windows\System32\net1.exe C:\Windows\System32\calc.exe
```

## Links

 - [Pypi](https://pypi.org/project/PyPePacker)
 - [Github](https://github.com/mauricelambert/PyPePacker)
 - [Documentation](https://mauricelambert.github.io/info/python/security/PyPePacker.html)
 - [Python executable](https://mauricelambert.github.io/info/python/security/PyPePacker.pyz)
 - [Python Windows executable](https://mauricelambert.github.io/info/python/security/PyPePacker.exe)

## License

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).
