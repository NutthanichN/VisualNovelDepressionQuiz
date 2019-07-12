import arcade
from dialog import DialogDrawer

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 720
SCREEN_TITLE = 'Test visual novel'


class VisualNovelWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.SADDLE_BROWN)

        self.dialog_box = DialogDrawer(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.background_pics = ["images/forest_background.jpg", "images/forest_background_2.jpg"]
        self.background_pic = self.background_pics[0]
        self.character_pic = ""
        self.background = arcade.load_texture(self.background_pic)

        self.draw_dialog_box = False
        self.draw_choice_box = False

    def change_background(self):
        next_index = self.background_pics.index(self.background_pic) + 1
        if next_index < len(self.background_pics):
            self.background_pic = self.background_pics[next_index]
        else:
            return

    def update(self, delta):
        self.background = arcade.load_texture(self.background_pic)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        if self.draw_dialog_box:
            self.dialog_box.display_dialog_box()

        if self.draw_choice_box:
            self.dialog_box.display_choice_box()

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.RIGHT:
            self.change_background()

        if key == arcade.key.ENTER:
            if self.draw_dialog_box:
                self.draw_dialog_box = False
            else:
                self.draw_dialog_box = True

        if key == arcade.key.SPACE:
            if self.draw_choice_box:
                self.draw_choice_box = False
            else:
                self.draw_choice_box = True


def main():
    window = VisualNovelWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_window(window)
    arcade.run()


if __name__ == '__main__':
    main()