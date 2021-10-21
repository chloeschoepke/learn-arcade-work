import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_sunset():
    """ Draw the sunset background"""
    arcade.set_background_color(arcade.color.INDIAN_RED)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 2, 0, arcade.color.JELLY_BEAN)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 4, 0, arcade.color.LIGHT_RED_OCHRE)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 6, 0, arcade.color.LIGHT_SALMON)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 12, 0, arcade.color.LIGHT_APRICOT)


class Cloud:
    def __init__(self, position_x, position_y, color):
        self.position_x = position_x
        self.position_y = position_y
        self.color = color

    def draw(self):
        arcade.draw_ellipse_filled(self.position_x, self.position_y, 150, 75, self.color, 0, -1)
        arcade.draw_ellipse_filled(self.position_x, self.position_y, 70, 115, self.color, 65, -1)
        arcade.draw_ellipse_filled(self.position_x, self.position_y, 70, 115, self.color, -65, -1)


class Bird:
    def __init__(self, position_x, position_y, change_x, change_y, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.color = color

    def draw(self):
        x = self.position_x
        y = self.position_y
        arcade.draw_triangle_filled(x - 60, y, x - 20, y + 20, x - 20, y - 20, self.color)
        arcade.draw_triangle_filled(x + 50, y - 50, x + 100, y - 10, x + 120, y - 20, self.color)
        arcade.draw_circle_filled(x + 20, y, 60, arcade.color.CELESTE)
        arcade.draw_circle_filled(x, y + 20, 7, self.color)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < 60:
            self.position_x = 60

        if self.position_x > SCREEN_WIDTH - 60:
            self.position_x = SCREEN_WIDTH - 60

        if self.position_y < 60:
            self.position_y = 60

        if self.position_y > SCREEN_HEIGHT - 60:
            self.position_y = SCREEN_HEIGHT - 60


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.set_mouse_visible(False)
        self.cloud = Cloud(50, 50, arcade.color.WHITE)
        self.bird = Bird(100, 100, 0, 0, arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        draw_sunset()
        self.cloud.draw()
        self.bird.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.cloud.position_x = x
        self.cloud.position_y = y

    def update(self, delta_time):
        self.bird.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.bird.change_x = -5
        elif key == arcade.key.RIGHT:
            self.bird.change_x = 5
        elif key == arcade.key.UP:
            self.bird.change_y = 5
        elif key == arcade.key.DOWN:
            self.bird.change_y = -5

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.bird.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.bird.change_y = 0


def main():
    window = MyGame()
    arcade.run()


main()
