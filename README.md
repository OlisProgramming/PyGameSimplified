# PyGame Simplified
***This project is now deprecated. Please see [this project](https://github.com/OlisProgramming/AppDevLanguage) instead!***
**This README file is out of date. See [the website](http://olisprogramming.github.io/PyGameSimplified/) instead for information!**


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
Any number (no sign, can be floating point), `Num`/`Number` in docs | `MATH_NUMBER`
`+`, `Plus` in docs | `MATH_PLUS`
`-`, `Minus` in docs | `MATH_MINUS`
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
`equal` | `KWD_EQUAL`
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
When the end of the file has been reached, `Eof` in docs | `MISC_EOF`
Any string of alpha characters or single quote for `'s` statement, `Str`/`String` in docs | `MISC_STRING`
Any string of characters surrounded by `"` on both sides (no single quotes, just double). Python escape characters (`\n`, `\t`, `\"`, `\\`, `\r`, `\uxxxx` etc.) are permitted. `StrLit` in docs. | `MISC_STRING_LITERAL`
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

Here are the other phrases, translations and definitions. When a phrase increases or decreases the resulting indent in Python, the terms `(ind+)` and `(ind-)` are used, respectively. `arg1`, `arg2` etc refer to the values of the tokens, respectively. For example, the phrase `Function Str Begin` could be translated from `function draw begin` into `def draw():`. If a specific string is required for certain behaviour, it is listed in the Usage column.

Phrase | Translation into Python | Usage
------ | ----------------------- | -----------
`Num Plus Num` | Result of addition | Optimisation code.
`Num Minus Num` | Result of subtraction | Optimisation code.
`Function Str Begin` | `def arg2(self):` | `(ind+)` Creates a function with no parameters. Only use inside classes.
`Mainfunction Begin` | `if __name__ == '__main__':` | `(ind+)` Code that runs if this file is the main file being run. Only use outside classes.
`Initfunction Begin` | `def __init__(self):` | `(ind+)` Code that runs when an instance of the containing class is created. Only use inside classes.
`Endprogram` | `quit()` | Quits the program without unloading any data. Use with caution.
`Import Str` | `from arg2 import *` | Imports code from local file. *Exception:* `arg2` is `pygame`; translates to `import pygame`.
`Return Str/Num/True/False` | `return arg2` | Returns value from function. *Exception:* `arg2` is a `StrLit`; translates to `return "arg2"`
`If Str Begin` | `if arg2:` | `(ind+)` If clause on a (boolean) variable.
`If Str Equal Str Begin` | `if arg2 == arg4:` | `(ind+)` If clause on whether two variables are equal.
`Elif Str Begin` | `elif arg2:` | `(ind+)` Elif clause on a (boolean) variable.
`Elif Str Equal Str Begin` | `elif arg2 == arg4:` | `(ind+)` Elif clause on whether two variables are equal.
`Else Begin` | `else:` | `(ind+)` Else clause.
`While Str Begin` | `while arg2:` | `(ind+)` While a (boolean) variable is `true`, execute block of code.
`For Str In Str Begin` | `for arg2 in arg4:` | `(ind+)` Iterate over all values in (list/tuple) `arg4`, setting `arg2` to the value each iteration.
`Class Str Begin` | `class arg2:` | `(ind+)` Create a new class named `arg2`, not inheriting any other class.
`Set Str To Str` | `arg2 = arg4` | Set value of `arg2` to value of `arg4`.
`Set Str To StrLit` | `arg2 = "arg4"` | Set value of `arg2` to value of `arg4`.
`Set Str To Num` | `arg2 = arg4` | Set value of `arg2` to value of `arg4`.
`Set Str To True` | `arg2 = true` | Set value of `arg2` to `true`.
`Set Str To False` | `arg2 = false` | Set value of `arg2` to `false`.
`Set Str To Eval Str/Num Plus Str/Num` | `arg2 = arg5 + arg7` | Set value of `arg2` to value of `arg5` plus value of `arg7`.
`Set Str To Eval Str/Num Minus Str/Num` | `arg2 = arg5 - arg7` | Set value of `arg2` to value of `arg5` minus value of `arg7`.
`Make Str Called Str` | `arg4 = arg2()` | Set value of `arg4` to a default-constructed `arg2`.
`Make List ( ... ) Called Str` | `arg7 = (arg4)` | Set value of `arg7` to a list of all of the values between `(` and `)`, separated by whitespace.
`Write Str/Num` | `print(arg2)` | Print value of `arg2` to the screen.
`Write StrLit` | `print("arg2")` | Print value of `arg2` to the screen.
`Write True` | `print("true")` | Print `"true"` to the screen.
`Write False` | `print("false")` | Print `"false"` to the screen.
`Run Str` | `arg2()` | Runs function `arg2`.
`Run Str ( ... )` | `arg2(arg4)` | Run function `arg2` with arguments of a list of all of the values between `(` and `)`, separated by whitespace.
`Store Str In Str` | `arg2()` | Run function `arg2`, and store result in `arg4`.
`Store Str ( ... ) In Str` | `arg2(arg4)` | Run function `arg2` with arguments of a list of all of the values between `(` and `)`, separated by whitespace, and store result in `arg7`.
`Switch Str` | Returns nothing | Initialise switch statement made of `if/elif/else` blocks. Store arg2 in `switch_arg`. *Note:* `switch` statements cannot yet be nested.
`Case Str Begin` | `if/elif switch_arg == arg2:` | `(ind+)` Switch Case statement on `arg2`.
`Case Default Begin` | `else:` | `(ind+)` Switch Case default statement.
`End` | Returns nothing | `(ind-)` Signals end of indented block.

# Naming and Spacing Conventions
All of these are optional, but give clarity.
## Naming
* Class names and file names: `UpperCamelCase`
* Function names and variables: `lower_underscore`
* Constants: `UPPER_UNDERSCORE`

## Spacing
* Indentation: Indent four spaces after a `begin` statement.
* Outdentation: Outdent four spaces just before an `end` statement.
* Line spaces: Each `begin` and `end` statement should have their own new line.
* Furthermore, phrases should not share lines with other phrases, and they should not span more than one line, except in cases of very long lines (over 79 chars).
* Comments: Place comments two or more spaces away from code. One space only should be allowed after the `#` symbol before commented documentation.
* Use long continuous lines of `#`s (over 10) to separate parts of code.
* To title certain parts of code, use 5 `#`s then the title name in all caps then 5 `#`s again, e.g.: `##### DRAW CALLS #####`
* Between classes/functions: allow two line breaks between two classes, two functions or the beginning of a class. Documentation in comments counts as lines IN the class/function.
* Inline Documentation: Documentation should be immediately one line before the item it is documenting, leaving one blank line before it to separate it from previous code. Classes should have class name on the first line of documentation, then an empty line (still with `#` symbol), then further documentation. Certain documentation items can be given using this set of annotations:
	- `@author NAME` states who authored the file.
	- `@date DD/MM/YY` is the date the file was CREATED, not last updated.
	- `@param NAME` is a parameter or argument to a specific function (once this feature is added).
	- `@return VAR_TYPE NAME` or `@return NAME` shows what this function returns, e.g. `@return StrLit greeting`. It is recommended to use `@return Str/String` as opposed to `@return StrLit` because Python does not support pointers to variables (so the `String` keyword would be unused)
	- `@todo` is what the user indends to add in the future.
	- `@see FILE_NAME/CLASS_NAME` recommends to the user to also look at said file/class for extra information.
	- `@see CLASS_NAME's FUNCTION_NAME/VARIABLE_NAME` is as above but shows functions and variables instead.

Examples of these rules in action:
```
import Window  # Window.pgs


# Main class
#
# @author Oli's Programming
# @date 24/04/16
# Main class for sample PGS project.
class Main
begin
    initfunction
    begin
        write "Main init"
        
        # @see Main's write_hello
        # This is where "hello_message" is used.
        set my hello_message to "hello"
    end
    
    
    # Writes "hello" to the screen.
    #
    # @return StrLit hello_message
    # The message that was just written to the screen.
    #
    # @todo add the user's name, to write for example "hello, user!"
    function write_hello
    begin
        write hello_message  # and do something else
        return hello_message
    end
end
```

# Example Code
Here are some example code files, showing usage of code, phrases and stylistic conventions.

## `Main.pgs`
```
import Window  # Window.pgs

# Main class
#
# @author Oli's Programming
# @date 24/04/16
#
# Handles window instance and is run
# as a single instance when
# the program is started
class Main
begin
    initfunction
    begin
        write "Main init"
		make Window called window  # Calls Window's initfunction automatically
    end
end


mainfunction  # Runs at program start
begin
    make Main called main  # Calls Main's initfunction automatically
end
```

## `Window.pgs`
```
import pygame  # Module for windows and apps

# Window class
#
# @author Oli's Programming
# @date 24/04/16
#
# Handles draw calls and
# PyGame events
# Is owned by the Main class
# @see Main
class Window
begin
    initfunction
    begin
		write "Window init"
        run pygame's init  # Initialise PyGame
		make list (640 480) called size  # Set window size to 640x480

		store pygame's display's set_mode(size) in my hwnd  # Store window in hwnd

		set my title to """ + '"' + proj_name + '"' + """
		run pygame's display's set_caption(my title)  # Set title to """ + '"' + proj_name + '"' + """

		make list (255 255 255) called my background_color  # Set background colour to white
		make pygame's time's Clock called my clock  # Make a clock to record FPS and time since last frame
		set my running to true  # Game is still running

		########################################

		while my running  # Main Loop
		begin
			##### EVENTS #####
			store pygame's event's get in eventlist
			for event in eventlist  # Get all events since last frame
			begin
				switch event's type
				case pygame's QUIT  # User pressed 'X' button
				begin
					set my running to false
				end
				case pygame's KEYDOWN  # User pressed a key down
				begin
					write "Key Down!"
				end
			end

			##### DRAWING #####
			run my hwnd's fill (my background_color)  # Fill background with 'my background_color'
			run pygame's display's flip  # Flip sprites drawn onto screen
			run my clock's tick (60)  # Delay so that frames never exceed 60FPS
		end
    end
end
```
