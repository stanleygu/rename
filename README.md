# Rename

A command line tool to rename files using regular expressions

# Installation

Using pip

```
pip install git+git://github.com/stanleygu/rename.git
```

# Usage

```
Usage: rename [OPTIONS]

Options:
  -d, --directory PATH   Directory to perform search
  -p, --pattern TEXT     Regex pattern to match files
                         with
  -t, --target TEXT      Regex pattern to replace files
                         with
  -r, --replace BOOLEAN  Boolean to replace files
  --help                 Show this message and exit.
```

* Rename png files with "Screen Shot" in name

`rename -p "Screen Shot.*png" -t screen\(index)`
