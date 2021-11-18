import arcade
import random

WIDTH = 60
HEIGHT = 60
MARGIN = 5
COLUMN_COUNT = 10
ROW_COUNT = 10

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        self.grid[2][1] = 0
        print(self.grid)

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                arcade.draw_rectangle_filled(x, y,
                                             WIDTH, HEIGHT,
                                             color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        row = y // (HEIGHT + MARGIN)
        column = x // (WIDTH + MARGIN)

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        if row < ROW_COUNT and column < COLUMN_COUNT:
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0

        if row + 1 < ROW_COUNT and column < COLUMN_COUNT:
            if self.grid[row + 1][column] == 0:
                self.grid[row + 1][column] = 1
            else:
                self.grid[row + 1][column] = 0

        if row - 1 < ROW_COUNT and column < COLUMN_COUNT:
            if row == 0:
                pass
            elif self.grid[row - 1][column] == 0:
                self.grid[row - 1][column] = 1
            else:
                self.grid[row - 1][column] = 0

        if row < ROW_COUNT and column + 1 < COLUMN_COUNT:
            if self.grid[row][column + 1] == 0:
                self.grid[row][column + 1] = 1
            else:
                self.grid[row][column + 1] = 0

        if row < ROW_COUNT and column - 1 < COLUMN_COUNT:
            if column == 0:
                pass
            elif self.grid[row][column - 1] == 0:
                self.grid[row][column - 1] = 1
            else:
                self.grid[row][column - 1] = 0


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()

    # on draw will not change for lab
    # adjust on click method for above, below, left and right (+1 to y or x)
    # need 4 if statements to keep within range (cardinal directions)
    #