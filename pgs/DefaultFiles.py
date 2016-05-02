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
    return """import pygame
import math
from Color import *


class Window:
    def __init__(self):
        print("Window init")
        pygame.init()
        size = (640, 480)
        self.window = pygame.display.set_mode(size)
        pygame.display.set_caption("Test")
        self.background_color = WHITE

        self.clock = pygame.time.Clock()
        self.running = True

    def display_screen(self):
        print("Window display_screen")
        while self.running:
            event_list = pygame.event.get()
            for event in event_list:

                if event.type == pygame.QUIT:
                    self.press_quit()

                elif event.type == pygame.KEYDOWN:
                    self.key_down(event)

            self.window.fill(self.background_color)
            for i in range(1000):
                radians_x = i / 100
                radians_y = i / 30

                x = int(75 * math.sin(radians_x)) + 200
                y = int(75 * math.cos(radians_y)) + 200

                pygame.draw.line(self.window, BLACK, [x,y], [x+5,y], 5)
            pygame.display.flip()
            self.clock.tick(60)
        self.quit_game()
        pygame.quit()

    def set_screen_title(self, title):
        pygame.display.set_caption(title)

    def set_background_color(self, color):
        self.background_color = color

    def draw(self):
        pass

    def press_quit(self):
        pass

    def quit_game(self):
        self.running = False

    def key_down(self, event):
        self.set_background_color(random_color())
"""


#############################


def color():
    return """RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
"""


#############################


def drawable():
    return """

"""


#############################


def pgsproject():
    return "Main\n" + \
           proj_name + "Window"
