from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

# axes
draw_line(0, 250, 500, 250, screen, color)
draw_line(250, 0, 250, 500, screen, color)


display(screen)
save_extension(screen, 'img.png')
