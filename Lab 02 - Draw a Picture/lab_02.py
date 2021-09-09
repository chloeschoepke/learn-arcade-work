"""
Drawing birds on a powerline at sunset
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
arcade.draw_triangle_filled(80, 400, 80, 375, 40, 375, arcade.csscolor.BLACK)
arcade.draw_triangle_filled(80, 373, 80, 360, 50, 375, arcade.csscolor.BLACK)
arcade.draw_circle_filled(130, 400, 10, arcade.csscolor.BLACK)
arcade.draw_triangle_filled(225, 250, 250, 320, 275, 320, arcade.csscolor.BLACK)

# Create circle bird
arcade.draw_line(340, 250, 340, 200, arcade.color.BLACK, 5)
arcade.draw_line(375, 270, 375, 200, arcade.color.BLACK, 5)
arcade.draw_triangle_filled(280, 300, 320, 320, 320, 280, arcade.csscolor.BLACK)
arcade.draw_triangle_filled(390, 250, 440, 290, 460, 280, arcade.csscolor.BLACK)
arcade.draw_circle_filled(360, 300, 60, arcade.color.CELESTE)
arcade.draw_circle_filled(340, 320, 7, arcade.csscolor.BLACK)

# Create triangle bird
arcade.draw_line(495, 250, 495, 200, arcade.color.BLACK, 5)
arcade.draw_line(520, 270, 520, 200, arcade.color.BLACK, 5)
arcade.draw_triangle_filled(465, 345, 470, 325, 450, 335, arcade.csscolor.BLACK)
arcade.draw_triangle_filled(465, 345, 475, 225, 570, 295, arcade.color.DARK_SEA_GREEN)
arcade.draw_circle_filled(480, 325, 6, arcade.csscolor.BLACK)
arcade.draw_triangle_filled(570, 295, 565, 320, 590, 320, arcade.csscolor.BLACK)

# Finish drawing
arcade.finish_render()

# Keep window open
arcade.run()
