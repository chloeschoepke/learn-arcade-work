import random
import arcade
import math

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Fly(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):
        # Calculate a new x, y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
            + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
            + self.circle_center_y

        # Increase the angle in prep for the next round.
        self.circle_angle += self.circle_speed


class Bee(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the bee
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0 and self.change_x < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH and self.change_x > 0:
            self.change_x *= -1

        if self.bottom < 0 and self.change_y < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT and self.change_y > 0:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):

        super().__init__(width, height)

        # Sprite lists
        self.player_list = None
        self.fly_list = None
        self.bee_list = None

        # Set up the player
        self.score = 0
        self.player_sprite = None

        # Load sounds
        self.fly_sound = arcade.load_sound("coin1.wav")
        self.bee_sound = arcade.load_sound("error4.wav")

    def start_new_game(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.fly_list = arcade.SpriteList()
        self.bee_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("frog_move.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        for i in range(50):

            # Create the fly instance
            # Fly image from kenney.nl
            fly = Fly("fly.png", SPRITE_SCALING / 3)

            # Position the center of the circle the fly will orbit
            fly.circle_center_x = random.randrange(SCREEN_WIDTH)
            fly.circle_center_y = random.randrange(SCREEN_HEIGHT)

            # Random radius from 10 to 200
            fly.circle_radius = random.randrange(10, 200)

            # Random start angle from 0 to 2pi
            fly.circle_angle = random.random() * 2 * math.pi

            # Add the fly to the lists
            self.fly_list.append(fly)

        for i in range(10):

            # Create the bee instance
            # Bee image from kenney.nl
            bee = Bee("bee.png", SPRITE_SCALING / 3)

            bee.center_x = random.randrange(SCREEN_WIDTH)
            bee.center_y = random.randrange(SCREEN_HEIGHT)
            bee.change_x = random.randrange(-5, 6)
            bee.change_y = random.randrange(-5, 6)

            # Add the bee to the lists
            self.bee_list.append(bee)

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Set the background color
        arcade.set_background_color(arcade.color.CERULEAN)

    def on_draw(self):

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.fly_list.draw()
        self.player_list.draw()
        self.bee_list.draw()

        # Put the text on the screen.
        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if len(self.fly_list) == 0:
            arcade.draw_text("GAME OVER", 200, 300, arcade.color.BLACK, 50)

    def on_mouse_motion(self, x, y, dx, dy):
        if len(self.fly_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):

        if len(self.fly_list) > 0:
            self.fly_list.update()
            self.bee_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.fly_list)
        for fly in hit_list:
            self.score += 1
            arcade.play_sound(self.fly_sound)
            fly.remove_from_sprite_lists()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bee_list)
        for bee in hit_list:
            self.score -= 1
            arcade.play_sound(self.bee_sound)
            bee.remove_from_sprite_lists()


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.start_new_game()
    arcade.run()


if __name__ == "__main__":
    main()
