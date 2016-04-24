# PyGameSimplified
A simple, user-friendly programming language that hopes to make game development easier and faster!
This project is a PyCharm Community Edition 5.0.4 Project.
PGS translates `*.pgs` files into `*.py` (Python 3.5) files that `import pygame`.


# How to use
To create a new project, run `SetupProject.py`.
To get PGS to interpret your project and translate it into Python, run `Interpreter.py`.


# Syntax
PGS is object-oriented.
It works around the basis of 'phrases', groups of tokens that connect to form one function or statement.
See list below for all possible tokens, phrases and their Python translations.

## Tokens
Here are all of the valid tokens (not organised very well). Token names are as stated in, for example, the source code and error handling messages.

### Math/Maths (`MATH_*`)
Symbol/Word | Token Name
----------- | ----------
Any number (no sign, can be floating point) | `MATH_NUMBER`
`+` | `MATH_PLUS`
`-` | `MATH_MINUS`
`eval` | `MATH_EVAL`

### Keywords (`KWD_*`)
Symbol/Word | Token Name
----------- | ----------
`function` | `KWD_FUNCTION`
`initfunction` | `KWD_INITFUNCTION`
`mainfunction` | `KWD_MAINFUNCTION`
`endprogram` | `KWD_ENDPROGRAM`
`import` | `KWD_IMPORT`
`return` | `KWD_RETURN`
`if` | `KWD_IF`
`elif` | `KWD_ELIF`
`else` | `KWD_ELSE`
`while` | `KWD_WHILE`
`for` | `KWD_FOR`
`in` | `KWD_IN`
`store` | `KWD_STORE`
`switch` | `KWD_SWITCH`
`case` | `KWD_CASE`
`default` | `KWD_DEFAULT`

### Classes (`CLA_*`)
Symbol/Word | Token Name
----------- | ----------
`class` | `CLA_CLASS`

### Variables (`VAR_*`)
Symbol/Word | Token Name
----------- | ----------
`set` | `VAR_SET`
`to` | `VAR_TO`
`make` | `VAR_MAKE`
`called` | `VAR_CALLED`
`true` | `VAR_TRUE`
`false` | `VAR_FALSE`
`list` | `VAR_LIST`

### Functions (`FUN_*`)
Symbol/Word | Token Name
----------- | ----------
`write` | `FUN_WRITE`
`run` | `FUN_RUN`

### Miscellaneous (`MISC_*`)
Symbol/Word | Token Name
----------- | ----------
When the end of the file has been reached | `MISC_EOF`
Any string of alpha characters or single quote for `'s` statement | `MISC_STRING`
Any string of characters surrounded by `"` on both sides (no single quotes, just double). Python escape characters (`\n`, `\t`, `\"`, `\\`, `\r`, `\uxxxx` etc.) are permitted. | `MISC_STRING_LITERAL`
`begin` | `MISC_BEGIN`
`end` | `MISC_END`
`(` | `MISC_LPARENTH`
`)` | `MISC_RPARENTH`

## Phrases
Certain sequences of characters do not make phrases (but are still valid), for example, comments, e.g.:

    # This is a comment.
    
    # This is a multi-line
    # comment. You need a '#'
    # symbol at the start of
    # every line.

Here are the other phrases, translations and definitions.
* ``
