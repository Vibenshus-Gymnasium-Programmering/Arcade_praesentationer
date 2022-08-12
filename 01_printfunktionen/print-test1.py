import arcade
arcade.open_window(600, 600, "Mit nye arcadebvindue")

arcade.start_render()
arcade.draw_circle_filled(300, 300, 50,arcade.color.RED)
arcade.draw_ellipse_outline(400, 500, 100, 50, arcade.color.BLUE, 30)
arcade.finish_render()
arcade.run()
