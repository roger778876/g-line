from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line( 1, 1, 500, 500, screen, color )


display(screen)
save_extension(screen, 'img.png')
