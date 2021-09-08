"""
Drawing a
"""

import arcade

# Open a window
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.INDIAN_RED)

# Clear the screen
arcade.start_render()

# Create sunset background
arcade.draw_lrtb_rectangle_filled(0, 600, 300, 0, arcade.color.JELLY_BEAN)
arcade.draw_lrtb_rectangle_filled(0, 600, 150, 0, arcade.color.LIGHT_RED_OCHRE)
arcade.draw_lrtb_rectangle_filled(0, 600, 100, 0, arcade.color.LIGHT_SALMON)
arcade.draw_lrtb_rectangle_filled(0, 600, 50, 0, arcade.color.LIGHT_APRICOT)

# Create power line
arcade.draw_line(0, 200, 600, 200, arcade.color.BLACK, 5)

# Create square bird
arcade.draw_rectangle_filled(150, 350, 150, 200, arcade.csscolor.SKY_BLUE)
arcade.draw_line(175, 250, 175, 200, arcade.color.BLACK, 7)
arcade.draw_line(100, 250, 100, 200, arcade.color.BLACK, 7)
arcade.draw_triangle_filled(100, 370, 100, 345, 50, 345, arcade.csscolor.BLACK)

# Finish drawing
arcade.finish_render()

#Keep window open
arcade.run()
