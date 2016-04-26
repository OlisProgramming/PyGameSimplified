from tks.Token import *


class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "3 + 5", "12 - 5", etc
        self.text = text
        # self.pos is an index of self.text
        self.pos = 0
        # current token instance
        self.current_token = None
        self.current_char = self.text[self.pos]
        self.arg1, self.arg2, self.arg3, self.arg4, self.arg5, self.arg6, self.arg7 = \
            None, None, None, None, None, None, None
        self.indent = 0  # How many tabs of indent are there at this point in code
        self.eof = False
        self.current_token = self.get_next_token()
        self.next_token_prefix = ""
        self.switch_arg = ""
        self.switch_cases = 0

    @staticmethod
    def error(string):
        raise Exception('\n\nError parsing input: ' + string)

    def advance(self):
        """Advance the 'pos' pointer and set the 'current_char' variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def reverse(self):
        """Reverse the 'pos' pointer and set the 'current_char' variable."""
        self.pos -= 1
        if self.pos < 0:
            self.current_char = None  # Indicates start of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def number(self):
        """Return a (multidigit) number consumed from the input."""
        result = ''
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            result += self.current_char
            self.advance()
        if int(result) == float(result):
            return int(result)
        return float(result)

    def string(self):
        """Return a string consumed from the input."""
        result = ''
        while self.current_char is not None and (self.current_char.isalpha() or
                                                 self.current_char == "'" or
                                                 self.current_char == "_"):
            result += self.current_char
            self.advance()
        return result

    def string_literal(self):
        """Return a string literal (e.g. "hello") consumed from the input."""
        result = ''
        while self.current_char is not None and not self.current_char == '"':
            result += self.current_char
            self.advance()
        self.advance()
        return result

    def line(self):
        """Return the next line of input."""
        result = ''
        while self.current_char is not None and not self.current_char == '\n':
            result += self.current_char
            self.advance()
        self.advance()
        return result

    def get_next_token(self):
        """
        Tokenizer

        This method is responsible for breaking a sentence
        apart into tokens.
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                self.next_token_prefix = ""
                return Token(MATH_NUMBER, self.number())

            if self.current_char.isalpha():
                word = self.string()

                if word == "eval":
                    self.next_token_prefix = ""
                    return Token(MATH_EVAL, word)

                elif word == "endprogram":
                    self.next_token_prefix = ""
                    return Token(KWD_ENDPROGRAM, word)
                elif word == "function":
                    self.next_token_prefix = ""
                    return Token(KWD_FUNCTION, word)
                elif word == "initfunction":
                    self.next_token_prefix = ""
                    return Token(KWD_INITFUNCTION, word)
                elif word == "mainfunction":
                    self.next_token_prefix = ""
                    return Token(KWD_MAINFUNCTION, word)
                elif word == "import":
                    self.next_token_prefix = ""
                    return Token(KWD_IMPORT, word)
                elif word == "return":
                    self.next_token_prefix = ""
                    return Token(KWD_RETURN, word)
                elif word == "if":
                    self.next_token_prefix = ""
                    return Token(KWD_IF, word)
                elif word == "elif":
                    self.next_token_prefix = ""
                    return Token(KWD_ELIF, word)
                elif word == "else":
                    self.next_token_prefix = ""
                    return Token(KWD_ELSE, word)
                elif word == "while":
                    self.next_token_prefix = ""
                    return Token(KWD_WHILE, word)
                elif word == "for":
                    self.next_token_prefix = ""
                    return Token(KWD_FOR, word)
                elif word == "in":
                    self.next_token_prefix = ""
                    return Token(KWD_IN, word)
                elif word == "equals":
                    self.next_token_prefix = ""
                    return Token(KWD_EQUAL, word)
                elif word == "store":
                    self.next_token_prefix = ""
                    return Token(KWD_STORE, word)
                elif word == "switch":
                    self.next_token_prefix = ""
                    return Token(KWD_SWITCH, word)
                elif word == "case":
                    self.next_token_prefix = ""
                    return Token(KWD_CASE, word)
                elif word == "default":
                    self.next_token_prefix = ""
                    return Token(KWD_DEFAULT, word)
                elif word == "inherits":
                    self.next_token_prefix = ""
                    return Token(KWD_INHERITS, word)
                elif word == "override":
                    self.next_token_prefix = ""
                    return Token(KWD_OVERRIDE, word)

                elif word == "class":
                    self.next_token_prefix = ""
                    return Token(CLA_CLASS, word)

                elif word == "set":
                    self.next_token_prefix = ""
                    return Token(VAR_SET, word)
                elif word == "to":
                    self.next_token_prefix = ""
                    return Token(VAR_TO, word)
                elif word == "make":
                    self.next_token_prefix = ""
                    return Token(VAR_MAKE, word)
                elif word == "called":
                    self.next_token_prefix = ""
                    return Token(VAR_CALLED, word)
                elif word == "true":
                    self.next_token_prefix = ""
                    return Token(VAR_TRUE, word)
                elif word == "false":
                    self.next_token_prefix = ""
                    return Token(VAR_FALSE, word)
                elif word == "list":
                    self.next_token_prefix = ""
                    return Token(VAR_LIST, word)

                elif word == "write":
                    self.next_token_prefix = ""
                    return Token(FUN_WRITE, word)
                elif word == "run":
                    self.next_token_prefix = ""
                    return Token(FUN_RUN, word)

                elif word == "begin":
                    self.next_token_prefix = ""
                    return Token(MISC_BEGIN, word)
                elif word == "end":
                    self.next_token_prefix = ""
                    return Token(MISC_END, word)
                elif word == "my":
                    self.next_token_prefix = "self."
                    continue
                else:
                    prefix = self.next_token_prefix
                    if word[-2:] == "'s":
                        if word == "super's":
                            self.next_token_prefix = ""
                            next_token = self.get_next_token()
                            return Token(MISC_STRING, prefix + "super()." + next_token.value)
                        else:
                            self.next_token_prefix = ""
                            next_token = self.get_next_token()
                            return Token(MISC_STRING, prefix + word[:-2] + "." + next_token.value)
                    else:
                        self.next_token_prefix = ""
                        return Token(MISC_STRING, prefix + word)  # Class / Variable name

            if self.current_char == '+':
                self.advance()
                self.next_token_prefix = ""
                return Token(MATH_PLUS, '+')
            elif self.current_char == '-':
                self.advance()
                self.next_token_prefix = ""
                return Token(MATH_MINUS, '-')
            elif self.current_char == '*':
                self.advance()
                self.next_token_prefix = ""
                return Token(MATH_MULTIPLY, '+')
            elif self.current_char == '/':
                self.advance()
                self.next_token_prefix = ""
                return Token(KWD_DIVIDE, '-')

            elif self.current_char == '(':
                self.advance()
                self.next_token_prefix = ""
                return Token(MISC_LPARENTH, '(')

            elif self.current_char == ')':
                self.advance()
                self.next_token_prefix = ""
                return Token(MISC_RPARENTH, ')')

            elif self.current_char == '"':
                self.advance()
                self.next_token_prefix = ""
                return Token(MISC_STRING_LITERAL, self.string_literal())

            elif self.current_char == "#":
                self.line()
                continue

            Interpreter.error("Invalid token (Valid types are e.g. NUMBER, PLUS, MINUS etc.): got " + self.current_char)

        self.eof = True
        return Token(MISC_EOF, None)

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise return false.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
            return True
        return False

    def expr(self):
        self.arg1 = self.current_token
        if self.eat(KWD_FUNCTION):
            self.arg2 = self.current_token
            if self.eat(MISC_STRING):
                self.arg3 = self.current_token
                if self.eat(MISC_BEGIN):
                    self.indent += 1
                    return "def " + self.arg2.value + "(self):"  # Function Str Begin
                elif self.eat(MISC_LPARENTH):
                    self.arg4 = self.current_token
                    self.arg4.value = str(self.arg4.value) + ", "
                    while self.eat(MISC_STRING) or self.eat(MATH_NUMBER) or self.eat(VAR_TRUE) or self.eat(VAR_FALSE):
                        self.arg4.value += str(self.current_token.value) + ", "
                    self.arg5 = self.current_token
                    if self.eat(MISC_RPARENTH):
                        self.arg6 = self.current_token
                        if self.eat(MISC_BEGIN):
                            self.indent += 1
                            return "def " + self.arg2.value + "(self, " + self.arg4.value[:-5] + "):"
                        else:
                            self.invalid(6)
                    else:
                        self.invalid(5)
                else:
                    self.invalid(3)
            else:
                self.invalid(2)

        elif self.eat(KWD_OVERRIDE):
            self.arg2 = self.current_token
            if self.eat(KWD_FUNCTION):
                self.arg3 = self.current_token
                if self.eat(MISC_STRING):
                    self.arg4 = self.current_token
                    if self.eat(MISC_BEGIN):
                        self.indent += 1
                        return "def " + self.arg3.value + "(self):\n" + self.indent*'    ' + \
                               "super()." + self.arg3.value + "()"  # Override Function Str Begin
                    elif self.eat(MISC_LPARENTH):
                        self.arg5 = self.current_token
                        self.arg5.value = str(self.arg5.value) + ", "
                        while self.eat(MISC_STRING) or self.eat(MATH_NUMBER) or self.eat(VAR_TRUE) or \
                              self.eat(VAR_FALSE):
                            self.arg5.value += str(self.current_token.value) + ", "
                        self.arg6 = self.current_token
                        if self.eat(MISC_RPARENTH):
                            self.arg7 = self.current_token
                            if self.eat(MISC_BEGIN):
                                self.indent += 1
                                return "def " + self.arg3.value + "(self, " + self.arg5.value[:-5] + "):\n" + \
                                       self.indent*'    ' + "super()." + self.arg3.value + "(" + \
                                       self.arg5.value[:-5] + ")"
                                # Override Function Str ( ... ) Begin
                            else:
                                self.invalid(7)
                        else:
                            self.invalid(6)
                    else:
                        self.invalid(4)
                else:
                    self.invalid(3)
            elif self.eat(KWD_INITFUNCTION):
                self.arg3 = self.current_token
                if self.eat(MISC_BEGIN):
                    self.indent += 1
                    return "def __init__(self):\n" + self.indent*'    ' + "super().__init__()"
            else:
                self.invalid(2)

        elif self.eat(KWD_MAINFUNCTION):
            self.arg2 = self.current_token
            if self.eat(MISC_BEGIN):
                self.indent += 1
                return "if __name__ == '__main__':"  # Mainfunction Begin
            else:
                self.invalid(2)

        elif self.eat(KWD_INITFUNCTION):
            self.arg2 = self.current_token
            if self.eat(MISC_BEGIN):
                self.indent += 1
                return "def __init__(self):"  # Initfunction Begin
            else:
                self.invalid(2)

        elif self.eat(KWD_ENDPROGRAM):
            return "quit()"

        elif self.eat(KWD_IMPORT):
            self.arg2 = self.current_token
            if self.eat(MISC_STRING):
                if self.arg2.value == "pygame":
                    return "import pygame"  # Import Pygame
                else:
                    return "from " + self.arg2.value + " import *"  # Mainfunction Begin
            else:
                self.invalid(2)

        elif self.eat(KWD_RETURN):
            self.arg2 = self.current_token
            if self.eat(MISC_STRING) or self.eat(MATH_NUMBER) or self.eat(VAR_TRUE) or self.eat(VAR_FALSE):
                return "return " + self.arg2.value
            elif self.eat(MISC_STRING_LITERAL):
                return "return \"" + self.arg2.value + "\""
            else:
                self.invalid(2)

        elif self.eat(KWD_IF):
            self.arg2 = self.current_token
            if self.eat(MISC_STRING):
                self.arg3 = self.current_token
                if self.eat(MISC_BEGIN):
                    self.indent += 1
                    return "if " + self.arg2.value + ":"  # If Str Begin
                elif self.eat(KWD_EQUAL):
                    self.arg4 = self.current_token
                    if self.eat(MISC_STRING):
                        self.arg5 = self.current_token
                        if self.eat(MISC_BEGIN):
                            self.indent += 1
                            return "if " + self.arg2.value + " == " + self.arg4.value + ":"  # If Str Equal Str Begin
                else:
                    self.invalid(3)
            else:
                self.invalid(2)

        elif self.eat(KWD_ELIF):
            self.arg2 = self.current_token
            if self.eat(MISC_STRING):
                self.arg3 = self.current_token
                if self.eat(MISC_BEGIN):
                    self.indent += 1
                    return "elif " + self.arg2.value + ":"  # Elif Str Begin
                elif self.eat(KWD_EQUAL):
                    self.arg4 = self.current_token
                    if self.eat(MISC_STRING):
                        self.arg5 = self.current_token
                        if self.eat(MISC_BEGIN):
                            self.indent += 1
                            return "elif " + self.arg2.value + " == " + self.arg4.value + ":"  # Elif Str Equal Str Begin
                else:
                    self.invalid(3)
            else:
                self.invalid(2)

        elif self.eat(KWD_ELSE):
            self.arg2 = self.current_token
            if self.eat(MISC_BEGIN):
                self.indent += 1
                return "else:"  # Else Str Begin

        elif self.eat(KWD_WHILE):
            self.arg2 = self.current_token
            if self.eat(MISC_STRING):
                self.arg3 = self.current_token
                if self.eat(MISC_BEGIN):
                    self.indent += 1
                    return "while " + self.arg2.value + ":"  # While Str Begin
                else:
                    self.invalid(3)
            else:
                self.invalid(2)

        elif self.eat(KWD_FOR):
            self.arg2 = self.current_token
            if self.eat(MISC_STRING):
                self.arg3 = self.current_token
                if self.eat(KWD_IN):
                    self.arg4 = self.current_token
                    if self.eat(MISC_STRING):
                        self.arg5 = self.current_token
                        if self.eat(MISC_BEGIN):
                            self.indent += 1
                            return "for " + self.arg2.value + " in " + self.arg4.value + ":"  # For Str In Str Begin
                        else:
                            self.invalid(5)
                    else:
                        self.invalid(4)
                else:
                    self.invalid(3)
            else:
                self.invalid(2)

        elif self.eat(CLA_CLASS):
            self.arg2 = self.current_token
            if self.eat(MISC_STRING):
                self.arg3 = self.current_token
                if self.eat(MISC_BEGIN):
                    self.indent += 1
                    return "class " + self.arg2.value + ":"  # Class Str Begin
                elif self.eat(KWD_INHERITS):
                    self.arg4 = self.current_token
                    if self.eat(MISC_STRING):
                        self.arg5 = self.current_token
                        if self.eat(MISC_BEGIN):
                            self.indent += 1
                            return "class " + self.arg2.value + "(" + self.arg4.value + "):"
                            # Class Str Inherits Str Begin
                        else:
                            self.invalid(5)
                    else:
                        self.invalid(4)
                else:
                    self.invalid(3)
            else:
                self.invalid(2)

        elif self.eat(VAR_SET):
            self.arg2 = self.current_token
            if self.eat(MISC_STRING):
                self.arg3 = self.current_token
                if self.eat(VAR_TO):
                    self.arg4 = self.current_token
                    if self.eat(MISC_STRING):
                        return self.arg2.value + " = " + self.arg4.value  # Set Str to Str
                    elif self.eat(MISC_STRING_LITERAL):
                        return self.arg2.value + ' = "' + self.arg4.value + '"'  # Set Str to StrLit
                    elif self.eat(MATH_NUMBER):
                        return self.arg2.value + ' = ' + str(self.arg4.value) + ''  # Set Str to Number
                    elif self.eat(VAR_TRUE):
                        return self.arg2.value + ' = True'  # Set Str to True
                    elif self.eat(VAR_FALSE):
                        return self.arg2.value + ' = False'  # Set Str to False

                    elif self.eat(MATH_EVAL):
                        self.arg5 = self.current_token
                        if self.eat(MATH_NUMBER) or self.eat(MISC_STRING):
                            self.arg6 = self.current_token
                            if self.eat(MATH_PLUS):
                                self.arg7 = self.current_token
                                if self.eat(MATH_NUMBER) or self.eat(MISC_STRING):
                                    return self.arg2.value + " = " + self.arg5.value + " + " + self.arg7.value
                                    # Set Str To Eval Num/Var Plus Num/Var
                                else:
                                    self.invalid(7)
                            elif self.eat(MATH_MINUS):
                                self.arg7 = self.current_token
                                if self.eat(MATH_NUMBER) or self.eat(MISC_STRING):
                                    return self.arg2.value + " = " + self.arg5.value + " - " + self.arg7.value
                                    # Set Str To Eval Num/Var Minus Num/Var
                                else:
                                    self.invalid(7)
                            elif self.eat(MATH_MULTIPLY):
                                self.arg7 = self.current_token
                                if self.eat(MATH_NUMBER) or self.eat(MISC_STRING):
                                    return self.arg2.value + " = " + self.arg5.value + " * " + self.arg7.value
                                    # Set Str To Eval Num/Var Multiply Num/Var
                                else:
                                    self.invalid(7)
                            elif self.eat(KWD_DIVIDE):
                                self.arg7 = self.current_token
                                if self.eat(MATH_NUMBER) or self.eat(MISC_STRING):
                                    return self.arg2.value + " = " + self.arg5.value + " / " + self.arg7.value
                                    # Set Str To Eval Num/Var Divide Num/Var
                                else:
                                    self.invalid(7)
                            else:
                                self.invalid(6)
                        else:
                            self.invalid(5)
                    else:
                        self.invalid(4)
                else:
                    self.invalid(3)
            else:
                self.invalid(2)

        elif self.eat(VAR_MAKE):
            self.arg2 = self.current_token
            if self.eat(MISC_STRING):
                self.arg3 = self.current_token
                if self.eat(VAR_CALLED):
                    self.arg4 = self.current_token
                    if self.eat(MISC_STRING):
                        return self.arg4.value + " = " + self.arg2.value + "()"  # Make Str Called Str
                    else:
                        self.invalid(4)
                else:
                    self.invalid(3)
            elif self.eat(VAR_LIST):
                self.arg3.value = self.current_token
                if self.eat(MISC_LPARENTH):
                    self.arg4 = self.current_token
                    self.arg4.value = str(self.arg4.value) + ", "
                    while self.eat(MISC_STRING) or self.eat(MATH_NUMBER) or self.eat(VAR_TRUE) or self.eat(VAR_FALSE):
                        self.arg4.value += str(self.current_token.value) + ", "
                    self.arg5 = self.current_token
                    if self.eat(MISC_RPARENTH):
                        self.arg6 = self.current_token
                        if self.eat(VAR_CALLED):
                            self.arg7 = self.current_token
                            if self.eat(MISC_STRING):
                                return self.arg7.value + " = (" + self.arg4.value[:-5] + ")"
                                # Make List (...) Called Str
                            else:
                                self.invalid(7)
                        else:
                            self.invalid(6)
                    else:
                        self.invalid(5)
                else:
                    self.invalid(3)
            else:
                self.invalid(2)

        elif self.eat(FUN_WRITE):
            self.arg2 = self.current_token
            if self.eat(MISC_STRING_LITERAL):
                return "print(\"" + self.arg2.value + "\")"  # Write StrLit
            elif self.eat(MISC_STRING) or self.eat(MATH_NUMBER):
                return "print(str(" + self.arg2.value + "))"  # Write Variable/Number
            elif self.eat(VAR_TRUE):
                return "print(\"true\")"  # Write True
            elif self.eat(VAR_FALSE):
                return "print(\"false\")"  # Write False
            else:
                self.invalid(2)

        elif self.eat(FUN_RUN):
            self.arg2 = self.current_token
            if self.eat(MISC_STRING):
                self.arg3 = self.current_token
                if self.eat(MISC_LPARENTH):
                    self.arg4 = self.current_token
                    self.arg4.value = str(self.arg4.value) + ", "
                    while self.eat(MISC_STRING) or self.eat(MATH_NUMBER) or self.eat(VAR_TRUE) or self.eat(VAR_FALSE):
                        self.arg4.value += str(self.current_token.value) + ", "
                    self.arg5 = self.current_token
                    if self.eat(MISC_RPARENTH):
                        return self.arg2.value + "(" + self.arg4.value[:-5] + ")"
                    else:
                        self.invalid(5)
                else:
                    return self.arg2.value + "()"
            else:
                self.invalid(2)

        elif self.eat(KWD_STORE):
            self.arg2 = self.current_token
            if self.eat(MISC_STRING):
                self.arg3 = self.current_token
                if self.eat(MISC_LPARENTH):
                    self.arg4 = self.current_token
                    self.arg4.value = str(self.arg4.value) + ", "
                    while self.eat(MISC_STRING) or self.eat(MATH_NUMBER) or self.eat(VAR_TRUE) or self.eat(VAR_FALSE):
                        self.arg4.value += str(self.current_token.value) + ", "
                    self.arg5 = self.current_token
                    if self.eat(MISC_RPARENTH):
                        self.arg6 = self.current_token
                        if self.eat(KWD_IN):
                            self.arg7 = self.current_token
                            if self.eat(MISC_STRING):
                                return self.arg7.value + " = " + self.arg2.value + "(" + self.arg4.value[:-5] + ")"
                            else:
                                self.invalid(7)
                        else:
                            self.invalid(6)
                    else:
                        self.invalid(5)
                elif self.eat(KWD_IN):
                    self.arg4 = self.current_token
                    if self.eat(MISC_STRING):
                        return self.arg4.value + " = " + self.arg2.value + "()"
                    else:
                        self.invalid(4)
                else:
                    self.invalid(3)
            else:
                self.invalid(2)

        elif self.eat(KWD_SWITCH):  # SWITCH statements CANNOT be nested... yet?
            self.arg2 = self.current_token
            if self.eat(MISC_STRING):
                self.switch_arg = self.arg2.value  # Switch Str
                self.switch_cases = 0
                return ''
            else:
                self.invalid(2)

        elif self.eat(KWD_CASE):
            self.arg2 = self.current_token
            if self.eat(MISC_STRING):
                self.arg3 = self.current_token
                if self.eat(MISC_BEGIN):
                    self.indent += 1
                    self.switch_cases += 1
                    return ("elif " if self.switch_cases > 1 else "if ") + \
                            self.switch_arg + " == " + self.arg2.value + ":"
                else:
                    self.invalid(3)
            elif self.eat(KWD_DEFAULT):
                self.arg3 = self.current_token
                if self.eat(MISC_BEGIN):
                    self.indent += 1
                    self.switch_cases += 1
                    return "else:"
                else:
                    self.invalid(3)
            else:
                self.invalid(2)

        elif self.eat(MISC_END):
            self.indent -= 1
            return ''  # End

        else:
            self.invalid(1)

    def invalid(self, args):
        if args == 1:
            Interpreter.error("Invalid phrase:\n" + self.arg1.type + "\n" + str(self.arg1.value))

        elif args == 2:
            Interpreter.error("Invalid phrase\n" + self.arg1.type + " " + self.arg2.type + "\n" +
                              str(self.arg1.value) + " " + str(self.arg2.value))
        elif args == 3:
            Interpreter.error(
                "Invalid phrase:\n" + self.arg1.type + " " + self.arg2.type + " " + self.arg3.type + "\n" +
                str(self.arg1.value) + " " + str(self.arg2.value) + " " + str(self.arg3.value))

        elif args == 4:
            Interpreter.error("Invalid phrase:\n" + self.arg1.type + " " + self.arg2.type + " " +
                              self.arg3.type + " " + self.arg4.type + "\n" +
                              str(self.arg1.value) + " " + str(self.arg2.value) +
                              " " + str(self.arg3.value) + " " + str(self.arg4.value))

        elif args == 5:
            Interpreter.error("Invalid phrase:\n" + self.arg1.type + " " + self.arg2.type + " " +
                              self.arg3.type + " " + self.arg4.type + " " + self.arg5.type + "\n" +
                              str(self.arg1.value) + " " + str(self.arg2.value) +
                              " " + str(self.arg3.value) + " " + str(self.arg4.value) + " " +
                              str(self.arg5.value))

        elif args == 6:
            Interpreter.error("Invalid phrase:\n" + self.arg1.type + " " + self.arg2.type + " " +
                              self.arg3.type + " " + self.arg4.type + " " + self.arg5.type + " " +
                              self.arg6.value + "\n" +
                              str(self.arg1.value) + " " + str(self.arg2.value) +
                              " " + str(self.arg3.value) + " " + str(self.arg4.value) + " " +
                              str(self.arg5.value) + " " + str(self.arg6.value))

        elif args == 7:
            Interpreter.error("Invalid phrase:\n" + self.arg1.type + " " + self.arg2.type + " " +
                              self.arg3.type + " " + self.arg4.type + " " + self.arg5.type + " " +
                              self.arg6.value + " " + self.arg7.value + "\n" +
                              str(self.arg1.value) + " " + str(self.arg2.value) +
                              " " + str(self.arg3.value) + " " + str(self.arg4.value) + " " +
                              str(self.arg5.value) + " " + str(self.arg6.value) + " " + str(self.arg7.value))


def main():
    project_file = open(".pgsproject")
    files = project_file.read().splitlines()
    for file_name in files:
        try:
            file = open(file_name + '.pgs')
            text = file.read()
            file.close()
            if not text:
                quit()
        except EOFError:
            quit()
        interpreter = Interpreter(text)
        indent_new = 0
        full_result = ''
        while not interpreter.eof:
            result = interpreter.expr()
            if indent_new >= 0:
                for _ in range(indent_new):
                    print('    ', end='')
                    full_result += '    '
                print(result)
                full_result += result + '\n'
                indent_new = interpreter.indent
            else:
                Interpreter.error("'end' statement invalid (too many)")

        if indent_new < 0:
            Interpreter.error("'end' statement expected")

        full_result = full_result.strip()
        full_result += '\n'

        file_out = open(file_name + '.py', mode='w')
        file_out.write(full_result)
        file_out.close()


if __name__ == '__main__':
    main()
