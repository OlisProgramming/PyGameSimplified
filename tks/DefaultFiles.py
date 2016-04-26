proj_name = ""


def main():
    return """import """ + proj_name + """Window

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
        write """ + '"' + proj_name + """ init"
		make """ + proj_name + """Window called window  # Calls Window's initfunction automatically
    end
end

mainfunction  # Runs at program start
begin
    make Main called main  # Calls Main's initfunction automatically
end
"""


#############################


def window():
    return """import pygame


class Window:
    def __init__(self):
        print("Window init")
        pygame.init()
        size = (640, 480)
        self.hwnd = pygame.display.set_mode(size)
        self.title = """ + '"' + proj_name + '"' """
        pygame.display.set_caption(self.title)
        self.background_color = (255, 255, 255)

        self.clock = pygame.time.Clock()
        self.running = True


    def display_screen(self):
        print("Window display_screen")
        while self.running:
            event_list = pygame.event.get()
            for event in event_list:

                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:
                    print("Key Down!")

            self.hwnd.fill(self.background_color)
            pygame.display.flip()
            self.clock.tick(60)
"""

#############################


def project_window():
    return """import Window

# Window Class
#
# Handles all draw calls and
# PyGame events
class TestWindow inherits Window
begin
	override initfunction
	begin
		write "Initialising """ + proj_name + """..."
		# Write code here to be run at the
		# start of the game.
		# Once 'display_screen' is run, no
		# more code will be executed until
		# the game closes.

		run display_screen

		write """ + '"' + proj_name + """ closed."
		# Write code here to be run once the
		# game has closed.
	end
end
"""


#############################


def pgsproject():
    return "Main\n" + \
           proj_name + "Window"
