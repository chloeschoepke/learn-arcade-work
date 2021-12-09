"""

Artwork for platform tiles from https://kenney.nl
Artwork for character from https://pixelfrog-assets.itch.io/pixel-adventure-1

"""

import arcade

SPRITE_SCALING = 0.5

PLAYER_SCALING = 2
DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"


VIEWPORT_MARGIN = 220
CAMERA_SPEED = 0.1
PLAYER_MOVEMENT_SPEED = 7
DEAD_ZONE = 0.1

RIGHT_FACING = 0
LEFT_FACING = 1
DISTANCE_TO_CHANGE_TEXTURE = 20


class MenuView(arcade.View):
    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Welcome to Frog Run",
                         DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2 + 100,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

        arcade.draw_text("Use arrow keys to move and jump",
                        DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2 + 20,
                        arcade.color.BLACK, font_size=30, anchor_x="center")

        arcade.draw_text("Collect all 60 coins to win",
                         DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2 - 20,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

        arcade.draw_text("CLICK TO START",
                         DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2 - 100,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class PlayerSprite(arcade.Sprite):
    """ Player Sprite """

    def __init__(self):
        """ Init """
        # Let parent initialize
        super().__init__()
        # Set our scale
        self.scale = PLAYER_SCALING

        # Get textures
        image_locations = [[0, 0, 32, 32],
                           [32, 0, 32, 32],
                           [64, 0, 32, 32],
                           [96, 0, 32, 32],
                           [128, 0, 32, 32]]

        self.idle_textures = arcade.load_textures("frog_run.png", image_locations)

        # What frame of the animation are we on now?
        self.cur_texture_index = 0

        # Set our texture to the current frame
        self.texture = self.idle_textures[self.cur_texture_index]

        # Start a clock to time how fast to iterate the frames
        self.time = 0.0

    def update_animation(self, delta_time):

        """ Update our player animations """

        # Update the clock
        self.time += delta_time

        # Is it time to go to the next frame?
        if self.time > 0.05:
            # Reset the clock
            self.time = 0
            # Move the texture frame index forward one
            self.cur_texture_index += 1

            # If we ran out of frames, reset to zero
            if self.cur_texture_index >= len(self.idle_textures):
                self.cur_texture_index = 0
            # Set current texture to the frame index we are on
            self.texture = self.idle_textures[self.cur_texture_index]


class GameView(arcade.View):
    """ Main application class. """

    def __init__(self):
        """
        Initializer
        """
        super().__init__()

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.background_list = None
        self.background_list = None
        self.coin_list = None
        self.coin_door_list = None
        self.cave_door_list = None
        self.exit_door_list = None
        self.room_list = []

        # Load main level into empty list
        map_name = "../Testing/level1.json"
        self.tile_map = arcade.load_tilemap(map_name, scaling=SPRITE_SCALING)
        self.room_list.append(self.tile_map)

        # Load secret coin room into empty list
        map_name = "../Testing/coinroom.json"
        self.tile_map = arcade.load_tilemap(map_name, scaling=SPRITE_SCALING)
        self.room_list.append(self.tile_map)

        # Load cave level into empty list
        map_name = "../Testing/level2.json"
        self.tile_map = arcade.load_tilemap(map_name, scaling=SPRITE_SCALING)
        self.room_list.append(self.tile_map)

        # Set up sounds
        self.coin_sound = arcade.load_sound("coin5.wav")

        # Set up the player
        self.player_sprite = None
        self.score = 0

        self.tile_map = self.room_list[0]

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.coin_door_list = arcade.SpriteList()
        self.cave_door_list = arcade.SpriteList()
        self.exit_door_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = PlayerSprite()
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        # Pull the sprite layers out of the tile map
        self.wall_list = self.tile_map.sprite_lists["Walls"]
        self.background_list = self.tile_map.sprite_lists["Background"]
        self.coin_list = self.tile_map.sprite_lists["Coins"]
        self.coin_door_list = self.tile_map.sprite_lists["Coin Door"]
        self.cave_door_list = self.tile_map.sprite_lists["Cave Door"]
        self.exit_door_list = self.tile_map.sprite_lists["Exit Door"]
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             gravity_constant=0.7)

    def on_show(self):
        # Set the background color
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

    def on_draw(self):
        arcade.start_render()
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.background_list.draw()
        self.player_list.draw(pixelated=True)
        self.coin_list.draw()
        self.coin_door_list.draw()
        self.cave_door_list.draw()
        self.exit_door_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.window.width // 2,
                                     20,
                                     self.window.width,
                                     40,
                                     arcade.color.ALMOND)

        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.BLACK, 24)

        if self.score == 60:
            arcade.draw_rectangle_filled(DEFAULT_SCREEN_WIDTH / 2,
                                         DEFAULT_SCREEN_HEIGHT / 2,
                                         DEFAULT_SCREEN_WIDTH,
                                         DEFAULT_SCREEN_HEIGHT,
                                         arcade.color.WHITE)
            arcade.draw_text("CONGRATULATIONS",
                             DEFAULT_SCREEN_WIDTH / 2,
                             DEFAULT_SCREEN_HEIGHT / 2 + 50,
                             arcade.color.BLACK,
                             font_size=50, anchor_x="center")
            arcade.draw_text("YOU WON",
                             DEFAULT_SCREEN_WIDTH / 2,
                             DEFAULT_SCREEN_HEIGHT / 2 - 50,
                             arcade.color.BLACK,
                             font_size=50, anchor_x="center")

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = 15
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if self.score < 60:
            if key == arcade.key.UP or key == arcade.key.DOWN:
                self.player_sprite.change_y = 0
            elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
                self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        if self.score < 60:
            self.physics_engine.update()
            self.player_sprite.update_animation(delta_time)
            self.coin_list.update()

        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                self.coin_list)
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)

        self.coin_door_list.update()
        coin_door_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_door_list)
        for door in coin_door_list:
            self.tile_map = self.room_list[1]
            self.wall_list = self.tile_map.sprite_lists["Walls"]
            self.background_list = self.tile_map.sprite_lists["Background"]
            self.coin_list = self.tile_map.sprite_lists["Coins"]
            self.coin_door_list = self.tile_map.sprite_lists["Coin Door"]
            self.cave_door_list = self.tile_map.sprite_lists["Cave Door"]
            self.exit_door_list = self.tile_map.sprite_lists["Exit Door"]
            self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                                 self.wall_list,
                                                                 gravity_constant=0.7)
            self.player_sprite.center_x = 128
            self.player_sprite.center_y = 128

        self.cave_door_list.update()
        cave_door_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.cave_door_list)
        for door in cave_door_list:
            self.tile_map = self.room_list[2]
            self.wall_list = self.tile_map.sprite_lists["Walls"]
            self.background_list = self.tile_map.sprite_lists["Background"]
            self.coin_list = self.tile_map.sprite_lists["Coins"]
            self.coin_door_list = self.tile_map.sprite_lists["Coin Door"]
            self.cave_door_list = self.tile_map.sprite_lists["Cave Door"]
            self.exit_door_list = self.tile_map.sprite_lists["Exit Door"]
            self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                                 self.wall_list,
                                                                 gravity_constant=0.7)
            self.player_sprite.center_x = 128
            self.player_sprite.center_y = 128

        self.exit_door_list.update()
        exit_door_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.exit_door_list)
        for door in exit_door_list:
            self.tile_map = self.room_list[0]
            self.wall_list = self.tile_map.sprite_lists["Walls"]
            self.background_list = self.tile_map.sprite_lists["Background"]
            self.coin_list = self.tile_map.sprite_lists["Coins"]
            self.coin_door_list = self.tile_map.sprite_lists["Coin Door"]
            self.cave_door_list = self.tile_map.sprite_lists["Cave Door"]
            self.exit_door_list = self.tile_map.sprite_lists["Exit Door"]
            self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                                 self.wall_list,
                                                                 gravity_constant=0.7)
            self.player_sprite.center_x = 128
            self.player_sprite.center_y = 128

        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):
        position = self.player_sprite.center_x - self.window.width / 2, \
                   self.player_sprite.center_y - self.window.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    window = arcade.Window(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
