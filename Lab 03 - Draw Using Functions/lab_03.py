"""
Drawing skyline at sunset
"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_sunset():
    """ Draw the sunset background"""
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 2, 0, arcade.color.JELLY_BEAN)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 4, 0, arcade.color.LIGHT_RED_OCHRE)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 6, 0, arcade.color.LIGHT_SALMON)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 12, 0, arcade.color.LIGHT_APRICOT)


def draw_cloud(x, y):
    """Draws a cloud"""
    arcade.draw_ellipse_filled(x, y, 150, 75, arcade.color.WHITE, 0, -1)
    arcade.draw_ellipse_filled(x, y, 70, 115, arcade.color.WHITE, 65, -1)
    arcade.draw_ellipse_filled(x, y, 70, 115, arcade.color.WHITE, -65, -1)


def draw_building(x, y):
    """Creates the main building"""
    arcade.draw_rectangle_filled(x, y - 95, 200, 450, arcade.color.BLACK, 0)
    """Drawing windows"""
    arcade.draw_rectangle_filled(x, y + 75, 30, 50, arcade.color.BLOND, 0)
    arcade.draw_rectangle_filled(x + 60, y + 75, 30, 50, arcade.color.BLOND, 0)
    arcade.draw_rectangle_filled(x - 60, y + 75, 30, 50, arcade.color.BLOND, 0)
    arcade.draw_rectangle_filled(x, y, 30, 50, arcade.color.BLOND, 0)
    arcade.draw_rectangle_filled(x + 60, y, 30, 50, arcade.color.BLOND, 0)
    arcade.draw_rectangle_filled(x - 60, y, 30, 50, arcade.color.BLOND, 0)
    arcade.draw_rectangle_filled(x, y - 75, 30, 50, arcade.color.BLOND, 0)
    arcade.draw_rectangle_filled(x + 60, y - 75, 30, 50, arcade.color.BLOND, 0)
    arcade.draw_rectangle_filled(x - 60, y - 75, 30, 50, arcade.color.BLOND, 0)
    arcade.draw_rectangle_filled(x, y - 150, 30, 50, arcade.color.BLOND, 0)
    arcade.draw_rectangle_filled(x + 60, y - 150, 30, 50, arcade.color.BLOND, 0)
    arcade.draw_rectangle_filled(x - 60, y - 150, 30, 50, arcade.color.BLOND, 0)
    arcade.draw_rectangle_filled(x, y - 225, 30, 50, arcade.color.BLOND, 0)
    arcade.draw_rectangle_filled(x + 60, y - 225, 30, 50, arcade.color.BLOND, 0)
    arcade.draw_rectangle_filled(x - 60, y - 225, 30, 50, arcade.color.BLOND, 0)


def draw_building_top(x, y):
    arcade.draw_rectangle_filled(x, y + 130, 170, 50, arcade.color.BLACK, 0)
    arcade.draw_rectangle_filled(x, y + 150, 140, 30, arcade.color.BLACK, 0)
    arcade.draw_rectangle_filled(x, y + 160, 100, 30, arcade.color.BLACK, 0)
    arcade.draw_rectangle_filled(x, y + 170, 70, 30, arcade.color.BLACK, 0)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
    arcade.set_background_color(arcade.color.INDIAN_RED)
    arcade.start_render()

    draw_sunset()
    draw_cloud(150, 500)
    draw_cloud(300, 475)
    draw_cloud(370, 305)
    draw_cloud(600, 400)
    draw_cloud(700, 550)
    draw_building(50, 270)
    draw_building(275, 100)
    draw_building_top(275, 100)
    draw_building(500, 200)
    draw_building_top(500, 200)
    draw_building(720, 175)

    # Finish drawing and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
