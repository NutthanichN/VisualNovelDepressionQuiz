import arcade
from dialog import DialogDrawer

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 720
SCREEN_TITLE = 'Test visual novel'


class VisualNovelWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # arcade.set_background_color(arcade.color.SADDLE_BROWN)

        self.dialog_box_pic = "images/dialog_box_1350x240.png"
        self.question_box_pic = "images/question_box_1350x100.PNG"
        self.choice_box_pic = "images/choice_box_652x140.PNG"
        self.character_pic = "images/Miina.png"

        self.background_pics = ["images/garden.png", "images/forest_background_2.jpg"]
        self.background_pic = self.background_pics[0]
        self.background = arcade.load_texture(self.background_pic)

        self.dialog = DialogDrawer(SCREEN_WIDTH, SCREEN_HEIGHT,
                                   self.dialog_box_pic, self.choice_box_pic, self.question_box_pic,
                                   self.character_pic)

        self.draw_dialog_box = False
        self.draw_choice_box = False
        self.draw_text = False
        self.draw_character = True

    def change_background(self):
        next_index = self.background_pics.index(self.background_pic) + 1
        if next_index < len(self.background_pics):
            self.background_pic = self.background_pics[next_index]
        else:
            return

    def update(self, delta):
        self.background = arcade.load_texture(self.background_pic)

        # use print to test so I put these lines here
        # if self.draw_text:
        #     self.dialog.display_text()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        if self.draw_character:
            self.dialog.display_character()

        if self.draw_dialog_box:
            self.dialog.display_dialog_box()

        if self.draw_choice_box:
            self.dialog.display_choice_and_question_box()

        if self.draw_text:
            self.dialog.display_text()

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

        if key == arcade.key.T:
            # if self.draw_text:
            #     self.draw_text = False
            # else:
            #     self.draw_text = True
            self.draw_text = True
            self.dialog.text.next_dialog()

    def on_mouse_press(self, x, y, button, modifiers):
        if self.dialog.choice_box_l_t.on_choice_box(x, y):
            print("On")
            print("===================")
        else:
            print("not on")
            print("===================")


def main():
    window = VisualNovelWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_window(window)
    arcade.run()


if __name__ == '__main__':
    main()