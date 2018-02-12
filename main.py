from display import *
from draw import *
import random

screen = new_screen()
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 191, 255]

# axes
draw_line(0, 250, 500, 250, screen, blue)
draw_line(250, 0, 250, 500, screen, blue)

''' demonstrate octants
draw_line(0, 0, 200, 500, screen, green)
draw_line(0, 0, 500, 200, screen, green)
draw_line(0, 0, 500, 500, screen, green)
draw_line(0, 500, 500, 0, screen, green)
draw_line(0, 500, 300, 0, screen, green)
draw_line(0, 500, 500, 200, screen, green)
'''

''' generate cool pic
for x in range(0, 251):
  for y in range(0, 251):
    x0 = x
    y0 = y
    x1 = random.randint(252, 500)
    y1 = random.randint(252, 500)
    i = random.randint(0, 2)
    if (i == 0):
      draw_line(x0, y0, x1, y1, screen, red)
    elif (i == 1):
      draw_line(x0, y0, x1, y1, screen, green)
    else:
      draw_line(x0, y0, x1, y1, screen, blue)
'''

display(screen)
save_extension(screen, 'img.png')