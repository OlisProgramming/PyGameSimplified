# Token types
# Math / Maths (MATH)
MATH_NUMBER,   MATH_PLUS,   MATH_MINUS,   MATH_EVAL = \
'MATH_NUMBER', 'MATH_PLUS', 'MATH_MINUS', 'MATH_EVAL'

# Keywords (KWD)
KWD_FUNCTION,   KWD_INITFUNCTION,    KWD_ENDPROGRAM,   KWD_MAINFUNCTION,   KWD_IMPORT,   KWD_RETURN = \
'KWD_FUNCTION', 'KWD_INIT_FUNCTION', 'KWD_ENDPROGRAM', 'KWD_MAINFUNCTION', 'KWD_IMPORT', 'KWD_RETURN'
KWD_IF,   KWD_ELIF,   KWD_ELSE,   KWD_WHILE,   KWD_FOR,   KWD_IN,   KWD_EQUAL,   KWD_STORE = \
'KWD_IF', 'KWD_ELIF', 'KWD_ELSE', 'KWD_WHILE', 'KWD_FOR', 'KWD_IN', 'KWD_EQUAL', 'KWD_STORE'

# Class (CLA)
CLA_CLASS, = \
'CLA_CLASS',

# Variables (VAR)
VAR_SET,   VAR_TO,   VAR_MAKE,   VAR_CALLED,   VAR_TRUE,   VAR_FALSE,   VAR_LIST = \
'VAR_SET', 'VAR_TO', 'VAR_MAKE', 'VAR_CALLED', 'VAR_TRUE', 'VAR_FALSE', 'VAR_LIST'

# Functions (FUN)
FUN_WRITE,   FUN_RUN = \
'FUN_WRITE', 'FUN_RUN'

# Misc (MISC)
MISC_EOF,   MISC_STRING,   MISC_STRING_LITERAL,   MISC_BEGIN,   MISC_END,   MISC_LPARENTH,   MISC_RPARENTH = \
'MISC_EOF', 'MISC_STRING', 'MISC_STRING_LITERAL', 'MISC_BEGIN', 'MISC_END', 'MISC_LPARENTH', 'MISC_RPARENTH'


class Token(object):
    def __init__(self, type, value):
        # token type e.g. MATH_NUMBER, KWD_ENDPROGRAM
        self.type = type
        # token value e.g. 42, "endprogram"
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()
