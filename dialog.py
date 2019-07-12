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


class QuestionBox(arcade.Sprite):
    def __init__(self, filename, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        super().__init__(filename)

        self.center_x = self.screen_width // 2
        self.center_y = self.screen_height - (self.height // 2) - 25


class Text:
    def __init__(self):
        self.text_reader = TextReader('test story 1.txt')
        self.text_reader.read_text('test story 1.txt')
        self.current_dialog = self.text_reader.get_next_action()

    def draw_text(self):
        print(self.current_dialog)

    def next_dialog(self):
        self.current_dialog = self.text_reader.get_next_action()


class DialogDrawer(arcade.Sprite):
    def __init__(self, screen_width, screen_height, dialog_box_pic, choice_box_pic, question_box_pic):
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

    def set_up_choice_boxes(self):
        self.choice_box_l_t.set_up_position(True, False, False, False)
        self.choice_box_l_b.set_up_position(False, True, False, False)
        self.choice_box_r_t.set_up_position(False, False, True, False)
        self.choice_box_r_b.set_up_position(False, False, False, True)

    def display_dialog_box(self):
        self.dialog_box.draw()

    def display_choice_and_question_box(self):
        self.question_box.draw()

        self.choice_box_l_t.draw()
        self.choice_box_l_b.draw()
        self.choice_box_r_t.draw()
        self.choice_box_r_b.draw()

    def display_text(self):
        self.text.draw_text()


class Status:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
