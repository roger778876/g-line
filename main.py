from display import *
from draw import *

screen = new_screen()
green = [0, 255, 0]
blue = [0, 191, 255]

# axes
draw_line(0, 250, 500, 250, screen, blue)
draw_line(250, 0, 250, 500, screen, blue)

draw_line(0, 0, 200, 500, screen, green)
draw_line(0, 0, 500, 200, screen, green)
draw_line(0, 0, 500, 500, screen, green)
draw_line(0, 500, 500, 0, screen, green)
draw_line(0, 500, 300, 0, screen, green)
draw_line(0, 500, 500, 200, screen, green)

display(screen)
save_extension(screen, 'img.png')