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

        self.background_pics = ["images/black.PNG", "images/garden.png", "images/TeaParty.PNG",
                                "images/garden_twilight.png"]
        self.background_pic = self.background_pics[0]
        self.background = arcade.load_texture(self.background_pic)

        self.dialog = DialogDrawer(SCREEN_WIDTH, SCREEN_HEIGHT,
                                   self.dialog_box_pic, self.choice_box_pic, self.question_box_pic,
                                   self.character_pic)

        self.draw_dialog_box = False
        self.draw_choice_box = False
        self.draw_dialog_text = False
        self.draw_character = True

    def change_background(self):
        # next_index = self.background_pics.index(self.background_pic) + 1
        # if next_index < len(self.background_pics):
        #     self.background_pic = self.background_pics[next_index]
        # else:
        #     return
        index = self.dialog.get_scene_change()
        self.background_pic = self.background_pics[index]

    def update(self, delta):
        self.background = arcade.load_texture(self.background_pic)
        self.dialog.update_category()

        # use print to test so I put these lines here
        # if self.draw_text:
        #     self.dialog.display_text()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        if self.dialog.scene_change:
            self.change_background()
            if self.background_pic == self.background_pics[0]:
                self.draw_character = False
            else:
                self.draw_character = True

        if self.draw_character:
            self.dialog.display_character()

        # new
        if self.dialog.is_dialog:
            self.dialog.display_dialog_box()
            self.dialog.display_text()
        elif self.dialog.is_choice:
            self.dialog.display_choice_and_question_box()
            self.dialog.display_text()

        # if self.draw_dialog_box:
        #     self.dialog.display_dialog_box()
        #
        # if self.draw_choice_box:
        #     self.dialog.display_choice_and_question_box()
        #
        # if self.draw_dialog_text:
        #     self.dialog.display_text()

    def on_key_press(self, key, key_modifiers):
        # if key == arcade.key.RIGHT:
        #     self.change_background()

        if key == arcade.key.ENTER:
            if not self.dialog.is_choice:
                self.dialog.text.next_dialog()
            # if self.draw_dialog_box:
            #     self.draw_dialog_box = False
            # else:
            #     self.draw_dialog_box = True

        # if key == arcade.key.SPACE:
        #     if self.draw_choice_box:
        #         self.draw_choice_box = False
        #     else:
        #         self.draw_choice_box = True
        #
        # if key == arcade.key.T:
        #     self.draw_dialog_text = True
        #     self.dialog.text.next_dialog()
        #
        # if key == arcade.key.Y:
        #     self.draw_dialog_text = False

    def on_mouse_press(self, x, y, button, modifiers):
        # answer = self.dialog.check_answer(x, y)
        # self.dialog.choose_root_story(answer)

        if self.dialog.is_choice:
            if len(self.dialog.text.current_dialog[1]) >= 1:
                if self.dialog.choice_box_l_t.on_choice_box(x, y):
                    print("On l_t")
                    print("===================")
                    # self.dialog.choose_root_story(1)
                    self.dialog.text.text_reader.change_path(1)
                    self.dialog.text.update_dialog()

            if len(self.dialog.text.current_dialog[1]) >= 2:
                if self.dialog.choice_box_r_t.on_choice_box(x, y):
                    print("On r_t")
                    print("===================")
                    # self.dialog.choose_root_story(2)
                    self.dialog.text.text_reader.change_path(2)
                    self.dialog.text.update_dialog()

            if len(self.dialog.text.current_dialog[1]) >= 3:
                if self.dialog.choice_box_l_b.on_choice_box(x, y):
                    print("On l_b")
                    print("===================")
                    # self.dialog.choose_root_story(3)
                    self.dialog.text.text_reader.change_path(3)
                    self.dialog.text.update_dialog()

            if len(self.dialog.text.current_dialog[1]) >= 4:
                if self.dialog.choice_box_r_b.on_choice_box(x, y):
                    print("On r_b")
                    print("===================")
                    # self.dialog.choose_root_story(4)
                    self.dialog.text.text_reader.change_path(4)
                    self.dialog.text.update_dialog()

            # else:
            #     print("not on any choice box")
            #     print("===================")
        else:
            print("not on any choice box")
            print("===================")


def main():
    window = VisualNovelWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_window(window)
    arcade.run()


if __name__ == '__main__':
    main()