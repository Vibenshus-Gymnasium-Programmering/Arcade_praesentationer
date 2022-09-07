import arcade
from math import cos, sin, pi

SKAERMBREDDE = 800
SKAERMHOEJDE = 600

arcade.open_window(SKAERMBREDDE, SKAERMHOEJDE, "Tegning af regnbue")


# Baggrundsfarve
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

# Græs
arcade.draw_lrtb_rectangle_filled(0, 799, 200, 0, arcade.csscolor.LAWNGREEN)

# Sol
arcade.draw_circle_filled(200, 450, 50, arcade.csscolor.YELLOW)
arcade.draw_line(200, 450 + 50 + 20, 200, 450 + 50 + 20 + 50, arcade.csscolor.YELLOW, 4)
arcade.draw_line(200, 450 - 50 - 20, 200, 450 - 50 - 20 - 50, arcade.csscolor.YELLOW, 4)
arcade.draw_line(200 + 50 + 20, 450, 200 + 50 + 20 + 50, 450, arcade.csscolor.YELLOW, 4)
arcade.draw_line(200 - 50 - 20, 450, 200 - 50 - 20 - 50, 450, arcade.csscolor.YELLOW, 4)
arcade.draw_line(200 + cos(pi/4)*(50 + 20), 450 +sin(pi/4)*(50 + 20), 200 + cos(pi/4)*(50 + 20 + 15), 450 + sin(pi/4)*(50 + 20 + 15), arcade.csscolor.YELLOW, 4)
arcade.draw_line(200 - cos(pi/4)*(50 + 20), 450 -sin(pi/4)*(50 + 20), 200 - cos(pi/4)*(50 + 20 + 15), 450 - sin(pi/4)*(50 + 20 + 15), arcade.csscolor.YELLOW, 4)
arcade.draw_line(200 + cos(pi/4)*(50 + 20), 450 -sin(pi/4)*(50 + 20), 200 + cos(pi/4)*(50 + 20 + 15), 450 - sin(pi/4)*(50 + 20 + 15), arcade.csscolor.YELLOW, 4)
arcade.draw_line(200 - cos(pi/4)*(50 + 20), 450 +sin(pi/4)*(50 + 20), 200 - cos(pi/4)*(50 + 20 + 15), 450 + sin(pi/4)*(50 + 20 + 15), arcade.csscolor.YELLOW, 4)

# Regnbue
arcade.draw_arc_outline(500,300,100,100, arcade.csscolor.VIOLET, 0, 180,10)
arcade.draw_arc_outline(500,300,110,110, arcade.csscolor.INDIGO, 0, 180,10)
arcade.draw_arc_outline(500,300,120,120, arcade.csscolor.BLUE, 0, 180,10)
arcade.draw_arc_outline(500,300,130,130, arcade.csscolor.GREEN, 0, 180,10)
arcade.draw_arc_outline(500,300,140,140, arcade.csscolor.YELLOW, 0, 180,10)
arcade.draw_arc_outline(500,300,150,150, arcade.csscolor.ORANGE, 0, 180,10)
arcade.draw_arc_outline(500,300,160,160, arcade.csscolor.RED, 0, 180,10)


# Skyer
arcade.draw_ellipse_filled(300, 300, 150, 100, arcade.csscolor.LIGHT_GRAY)
arcade.draw_ellipse_filled(380, 300, 150, 120, arcade.csscolor.LIGHT_GRAY)

arcade.draw_ellipse_filled(600, 300, 150, 100, arcade.csscolor.LIGHT_GRAY)
arcade.draw_ellipse_filled(680, 300, 150, 120, arcade.csscolor.LIGHT_GRAY)
arcade.finish_render()

arcade.run()
