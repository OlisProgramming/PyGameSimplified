proj_name = ""


def main():
    return """import Window  # Window.pgs

# Main class
#
# Handles window instance and is run
# as a single instance when
# the program is started
class Main
begin
    initfunction
    begin
        write """ + '"' + proj_name + """ init"
		make Window called window  # Calls Window's initfunction automatically
    end
end

mainfunction  # Runs at program start
begin
    make Main called main  # Calls Main's initfunction automatically
end
"""


#############################


def window():
    return """import pygame  # Module for windows and apps

# Window class
#
# Handles draw calls and
# PyGame events
# Is owned by the Main class
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
"""


#############################


def pgsproject():
    return """Main
Window"""
