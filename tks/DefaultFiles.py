main = \
    """import Window

class Main
begin
    initfunction
    begin
        write "Main init"
		make Window called hwnd
    end
end

mainfunction
begin
    make Main called main
end
"""
#############################

window = \
    """import pygame

class Window
begin
    initfunction
    begin
		write "Window init"
        run pygame's init
		make list (640 480) called size
		run pygame's display's set_mode(size)
    end
end
"""

#############################

pgsproject = \
    """Main
Window"""
