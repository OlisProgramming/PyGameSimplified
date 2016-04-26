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
# @author Oli's Programming
# @date 25/04/16
#
# Handles all draw calls and
# PyGame events
class """ + proj_name + """Window inherits Window
begin

end
"""


#############################


def pgsproject():
    return "Main\n" + \
           proj_name + "Window"
