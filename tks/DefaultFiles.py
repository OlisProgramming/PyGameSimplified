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

		store pygame's display's set_mode(size) in my hwnd

		set my title to "PGS Test"
		run pygame's display's set_caption(my title)

		make list (255 255 255) called my background_color
		make pygame's time's Clock called my clock
		set my running to true

		while my running
		begin
			store pygame's event's get in eventlist
			for event in eventlist
			begin
				switch event's type
				case pygame's QUIT
				begin
					set my running to false
				end
				case pygame's KEYDOWN
				begin
					write "Key Down!"
				end
			end

			run my hwnd's fill (my background_color)
			run pygame's display's flip
			run my clock's tick (60)
		end
    end
end
"""

#############################

pgsproject = \
    """Main
Window"""
