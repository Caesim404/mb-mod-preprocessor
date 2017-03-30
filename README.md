# MB Mod Preprocessor

Allows injecting code into MB module before compilation.

## Dependencies:
* Python 2

## Installation:
1. Copy the `compile.py` file to the same folder your module source files are.
2. Creata a `scripts` directory

## Usage:
All custom scripts are located in `scripts` directory. Each is in a `*.py` file. 

Each script should contain `from pp import *` at the beginning.

After that you can modify the variables in each module as you wish.

They are the same as in `module_*.py` files (e.g. if you want to edit mission templates edit `mission_templates` variable).

Do check if mutation applies.

All `header_*`/`ID_*`/`module_*` variables will be imported with `pp`.

When ready simply run compile.py and it will be compiled with the applied changes.

## Examples:
See `examples_nw` directory.
