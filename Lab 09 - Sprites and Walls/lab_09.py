import arcade
import random

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5
CAMERA_SPEED = 1


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Load coin sound
        self.coin_sound = arcade.load_sound("coin1.wav")

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.rock_list = None
        self.coin_list = None

        # Set up the player
        self.player_sprite = None
        self.score = 0

        # This variable holds our simple "physics engine"
        self.physics_engine = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):

        # Set the background color
        arcade.set_background_color(arcade.color.STORMCLOUD)

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Reset the score
        self.score = 0

        # Create the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("character1.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # --- Place boxes inside a loop
        # Stone wall and rock image from kenney.nl
        for x in range(0, 1024, 64):
            wall = arcade.Sprite("stone.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 960
            self.wall_list.append(wall)

        for x in range(0, 960, 64):
            wall = arcade.Sprite("stone.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

        for y in range(0, 960, 64):
            wall = arcade.Sprite("stone.png", SPRITE_SCALING_BOX)
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 960, 64):
            wall = arcade.Sprite("stone.png", SPRITE_SCALING_BOX)
            wall.center_x = 960
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(120, 632, 64):
            wall = arcade.Sprite("stone.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 140
            self.wall_list.append(wall)

        for x in range(760, 900, 64):
            wall = arcade.Sprite("stone.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 140
            self.wall_list.append(wall)

        for x in range(64, 700, 64):
            wall = arcade.Sprite("stone.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 280
            self.wall_list.append(wall)

        for x in range(120, 300, 64):
            wall = arcade.Sprite("stone.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 420
            self.wall_list.append(wall)

        for x in range(400, 800, 64):
            wall = arcade.Sprite("stone.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 420
            self.wall_list.append(wall)

        for x in range(250, 800, 64):
            wall = arcade.Sprite("stone.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 560
            self.wall_list.append(wall)

        for x in range(64, 750, 64):
            wall = arcade.Sprite("stone.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 700
            self.wall_list.append(wall)

        # Individually place rocks using coordinates
        rock_coordinate_list = [[450, 210],
                                [470, 500],
                                [480, 240],
                                [896, 420],
                                [855, 445],
                                [120, 800],
                                [700, 800],
                                [400, 900],
                                [270, 900]]

        # Loop through coordinates
        for coordinate in rock_coordinate_list:
            rock = arcade.Sprite("rock.png", SPRITE_SCALING_BOX)
            rock.center_x = coordinate[0]
            rock.center_y = coordinate[1]
            self.wall_list.append(rock)

        # Individually place walls using coordinates
        wall_coordinate_list = [[896, 700],
                                [832, 700]]

        # Loop through coordinates
        for coordinate in wall_coordinate_list:
            wall = arcade.Sprite("stone.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Create the physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        for i in range(COIN_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("coin.png", SPRITE_SCALING_COIN)

            coin_placed_successfully = False

            # Keep trying until success
            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(960)
                coin.center_y = random.randrange(960)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    # It is!
                    coin_placed_successfully = True

            # Add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()

        # Select the scrolled camera for our sprites
        self.camera_for_sprites.use()

        # Draw the sprites
        self.wall_list.draw()
        self.player_list.draw()
        self.rock_list.draw()
        self.coin_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_for_gui.use()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)

    def on_update(self, delta_time):
        """ Movement and game logic """

        self.physics_engine.update()

        self.coin_list.update()
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)

        lower_left_corner = (self.player_sprite.center_x - self.width / 2,
                             self.player_sprite.center_y - self.height / 2)
        self.camera_for_sprites.move_to(lower_left_corner, CAMERA_SPEED)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
