"""
12/7/19 4:17
1.change dialog&choice box to sprite or not? --> yes consider size
2.build mouse motion (try to use only this file) --> check is mouse at choice box
3.think how to change first dialog to others dialog with/without background change
4.ask whose file will use as a main (to run game window) --> do I have to write it my self?
5.ask size of game window
"""
import arcade
from text_reader import TextReader

CHARACTER_SCALE = 1.5


class DialogBox(arcade.Sprite):
    def __init__(self, filename, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        super().__init__(filename)

        self.center_x = self.screen_width // 2     # screen_width // 2
        self.center_y = (self.height // 2) + 30     # 150


class ChoiceBox(arcade.Sprite):
    def __init__(self, filename, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        super().__init__(filename)

        self.center_x = 0
        self.center_y = 0

    def set_up_position(self, left_top, left_bottom, right_top, right_bottom):
        center_x_left = self.width // 2 + 75    # 401
        center_x_right = self.screen_width - (self.width // 2) - 75     # 1099
        center_y_bottom = (self.height // 2) + 25      # 385
        center_y_top = center_y_bottom + self.height + 20

        if left_top:
            self.center_x = center_x_left
            self.center_y = center_y_top
        elif left_bottom:
            self.center_x = center_x_left
            self.center_y = center_y_bottom
        elif right_top:
            self.center_x = center_x_right
            self.center_y = center_y_top
        elif right_bottom:
            self.center_x = center_x_right
            self.center_y = center_y_bottom

    def on_choice_box(self):
        pass


class QuestionBox(arcade.Sprite):
    def __init__(self, filename, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        super().__init__(filename)

        self.center_x = self.screen_width // 2
        self.center_y = self.screen_height - (self.height // 2) - 25


class Text:
    def __init__(self):
        self.text_reader = TextReader('story/test story 1.txt', 'admin')
        self.current_dialog = self.text_reader.get_next_action()

        self.start_x = 0
        self.start_y = 0
        self.width = 0

    def draw_text_paragraph(self):
        category = self.current_dialog[0]
        # ['D', ['miina', 'nice to meet you\nline break test']]
        if category == 'D':
            arcade.draw_text(self.current_dialog[1][1], self.start_x, self.start_y, arcade.color.BLACK, font_size=30)
        else:
            arcade.draw_text(self.current_dialog[1][0], self.start_x, self.start_y, arcade.color.BLACK, font_size=30)

        print(self.current_dialog)

    def next_dialog(self):
        self.current_dialog = self.text_reader.get_next_action()

    def count_paragraph(self):
        paragraphs = self.current_dialog[1][0].split('\n')
        return len(paragraphs)
        # print(paragraphs)


class Character(arcade.Sprite):
    def __init__(self, filename, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        super().__init__(filename, CHARACTER_SCALE)

        self.center_x = self.screen_width // 2
        self.center_y = 250


class DialogDrawer(arcade.Sprite):
    def __init__(self, screen_width, screen_height, dialog_box_pic, choice_box_pic, question_box_pic,
                 character_pic):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.dialog_box = DialogBox(dialog_box_pic, screen_width, screen_height)

        self.question_box = QuestionBox(question_box_pic, screen_width, screen_height)

        self.choice_box_l_t = ChoiceBox(choice_box_pic, screen_width, screen_height)
        self.choice_box_l_b = ChoiceBox(choice_box_pic, screen_width, screen_height)
        self.choice_box_r_t = ChoiceBox(choice_box_pic, screen_width, screen_height)
        self.choice_box_r_b = ChoiceBox(choice_box_pic, screen_width, screen_height)
        self.set_up_choice_boxes()

        self.text = Text()
        self.set_up_text_position()

        self.character = Character(character_pic, screen_width, screen_height)

    def set_up_choice_boxes(self):
        self.choice_box_l_t.set_up_position(True, False, False, False)
        self.choice_box_l_b.set_up_position(False, True, False, False)
        self.choice_box_r_t.set_up_position(False, False, True, False)
        self.choice_box_r_b.set_up_position(False, False, False, True)

    def spilt_name_from_paragraph(self):
        split_colon = self.text.current_dialog[1][0].split(':')
        name = split_colon.pop(0)
        # self.text.current_dialog[1][0] = self.text.current_dialog[1][0][4:]
        return name

    def set_up_text_position(self):
        category = self.text.current_dialog[0]
        num_paragraph = self.text.count_paragraph()
        if category == 'D':
            self.text.start_x = self.dialog_box.center_x - (self.dialog_box.width // 2) + 20

            # arcade.draw_text(self.spilt_name_from_paragraph(), self.text.start_x, 220, arcade.color.BLACK, font_size=30)
            arcade.draw_text(self.text.current_dialog[1][0], self.text.start_x, 220, arcade.color.BLACK, font_size=30)

            if num_paragraph == 1:
                self.text.start_y = self.dialog_box.center_y - 25
            elif num_paragraph == 2:
                self.text.start_y = self.dialog_box.center_y - 40
            elif num_paragraph == 3:
                self.text.start_y = self.dialog_box.center_y - 55
            elif num_paragraph == 4:
                self.text.start_y = 75
            elif num_paragraph == 5:
                self.text.start_y = 60
            # elif num_paragraph == 6:
            #     self.text.start_y = 60
        else:
            self.text.start_x = 0
            self.text.start_y = 0

    def display_dialog_box(self):
        self.dialog_box.draw()

    def display_choice_and_question_box(self):
        self.question_box.draw()

        self.choice_box_l_t.draw()
        self.choice_box_l_b.draw()
        self.choice_box_r_t.draw()
        self.choice_box_r_b.draw()

    def display_text(self):
        self.set_up_text_position()
        self.text.draw_text_paragraph()
        print('---------------------------------------------------------------------------')
        print(self.text.count_paragraph())

    def display_character(self):
        self.character.draw()


class Status:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
