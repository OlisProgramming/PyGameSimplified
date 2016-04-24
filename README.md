# PyGameSimplified
A simple, user-friendly programming language that hopes to make game development easier and faster!
PGS translates `*.pgs` files into `*.py` (Python 3.5) files that `import pygame`.


# How to use
To create a new project, run `SetupProject.py`.
To get PGS to interpret your project and translate it into Python, run `Interpreter.py`.


# Syntax
PGS is object-oriented.
It works around the basis of 'phrases', groups of tokens that connect to form one function or statement.
See list below for all possible tokens, phrases and their Python translations.

## Tokens
Here are all of the valid tokens:

### Math/Maths
Symbol/Word | Token Name
----------- | ----------
Any number (no sign, can be floating point) | `MATH_NUMBER`
`+` | `MATH_PLUS`
`-` | `MATH_MINUS`
`eval` | `MATH_EVAL`


## Phrases
Certain sequences of characters do not make phrases (but are still valid), for example, comments, e.g.:

    # This is a comment.
    
    # This is a multi-line
    # comment. You need a '#'
    # symbol at the start of
    # every line.

Here are the other phrases, translations and definitions.
* ``
