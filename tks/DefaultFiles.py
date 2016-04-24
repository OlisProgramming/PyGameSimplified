main = \
    """import Window

class Main
begin
    initfunction
    begin
        write "Main init"
		make Window called window
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

		store pygame's display's set_mode(size)
		set hwnd to result

		set title to "PGS Test"
		run pygame's display's set_caption(title)

		make list (255 255 255) called background_color
		make pygame's time's Clock called clock
		set running to true

		while running
		begin
			store pygame's event's get
			for event in result
			begin
				if event's type equals pygame's QUIT
				begin
					set running to false
				end
			end

			run hwnd's fill (background_color)
			run pygame's display's flip
			run clock's tick (60)
		end
    end
end
"""

#############################

pgsproject = \
    """Main
Window"""
