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

    def on_choice_box(self, x, y):
        if self.left <= x <= self.right:
            if self.bottom <= y <= self.top:
                return True
        return False


class QuestionBox(arcade.Sprite):
    def __init__(self, filename, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        super().__init__(filename)

        self.center_x = self.screen_width // 2
        self.center_y = self.screen_height - (self.height // 2) - 25


class Text:
    def __init__(self):
        self.text_reader = TextReader('story/start.txt', 'admin')
        self.current_dialog = self.text_reader.get_next_action()
        self.previous_dialog = []

        self.dialog_start_x = 0
        self.dialog_start_y = 0

        self.choice_start_x_left = 0
        self.choice_start_x_right = 0
        self.choice_start_y_top = 0
        self.choice_start_y_bottom = 0

        self.question_start_x = 0
        self.question_start_y = 0

        self.font_size = 30

        # self.index_choice = 0

    def update_dialog(self):
        self.current_dialog = self.text_reader.get_next_action()

    def draw_text_paragraph(self):
        category = self.current_dialog[0]
        # ['D', ['miina', 'nice to meet you\nline break test']]
        if category == 'D':
            arcade.draw_text(self.current_dialog[1][1], self.dialog_start_x, self.dialog_start_y,
                             arcade.color.BLACK, self.font_size)
        elif category == 'Q':
            # question part
            arcade.draw_text(self.previous_dialog[1][1], self.question_start_x, self.question_start_y,
                             arcade.color.BLACK, self.font_size - 10)
            # choice 1-4
            if len(self.current_dialog[1]) >= 1:
                arcade.draw_text(self.current_dialog[1][0], self.choice_start_x_left, self.choice_start_y_top,
                                 arcade.color.BLACK, self.font_size)
            if len(self.current_dialog[1]) >= 2:
                arcade.draw_text(self.current_dialog[1][1], self.choice_start_x_right, self.choice_start_y_top,
                                 arcade.color.BLACK, self.font_size)
            if len(self.current_dialog[1]) >= 3:
                arcade.draw_text(self.current_dialog[1][2], self.choice_start_x_left, self.choice_start_y_bottom,
                                 arcade.color.BLACK, self.font_size)
            if len(self.current_dialog[1]) >= 4:
                arcade.draw_text(self.current_dialog[1][3], self.choice_start_x_right, self.choice_start_y_bottom,
                                 arcade.color.BLACK, self.font_size)
        else:
            arcade.draw_text(self.current_dialog[1][0], 0, 0,
                             arcade.color.BLACK, self.font_size)

        # print(self.current_dialog)
        # print(f"previous {self.previous_dialog}")
        # print(self.text_reader.dialog)
        # print(self.text_reader.path)

    def next_dialog(self):
        # print("1")
        self.previous_dialog = self.current_dialog
        # print("2")
        self.current_dialog = self.text_reader.get_next_action()
        # print("3")

    def count_line_break(self):
        category = self.current_dialog[0]
        count = 0
        if category == 'D':
            paragraphs = self.current_dialog[1][1].split('\n')
            count = len(paragraphs)
        elif category == 'Q':
            max_p = 0
            for i in self.current_dialog[1]:
                paragraphs = i.split('\n')
                sub_count = len(paragraphs)
                if sub_count >= max_p:
                    max_p = sub_count
            count = max_p
        return count
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

        self.is_dialog = False
        self.is_choice = False
        self.scene_change = False

    def set_up_choice_boxes(self):
        self.choice_box_l_t.set_up_position(True, False, False, False)
        self.choice_box_l_b.set_up_position(False, True, False, False)
        self.choice_box_r_t.set_up_position(False, False, True, False)
        self.choice_box_r_b.set_up_position(False, False, False, True)

    def set_up_text_position(self):
        category = self.text.current_dialog[0]
        num_paragraph = self.text.count_line_break()
        if category == 'D':
            self.text.font_size = 30
            self.text.dialog_start_x = self.dialog_box.center_x - (self.dialog_box.width // 2) + 20

            arcade.draw_text(self.text.current_dialog[1][0], self.text.dialog_start_x, 220,
                             arcade.color.BLACK, font_size=30)

            if num_paragraph == 1:
                self.text.dialog_start_y = self.dialog_box.center_y - 25
            elif num_paragraph == 2:
                self.text.dialog_start_y = self.dialog_box.center_y - 40
            elif num_paragraph == 3:
                self.text.dialog_start_y = self.dialog_box.center_y - 55
            elif num_paragraph == 4:
                self.text.dialog_start_y = 75
            elif num_paragraph == 5:
                self.text.dialog_start_y = 60

        elif category == 'Q':
            self.text.choice_start_x_left = 90
            self.text.choice_start_x_right = 790

            self.text.question_start_x = 90
            self.text.question_start_y = 630

            if num_paragraph == 1:
                self.text.choice_start_y_top = 240
                self.text.choice_start_y_bottom = 80
            elif num_paragraph == 2:
                self.text.choice_start_y_top = 230
                self.text.choice_start_y_bottom = 70
            elif num_paragraph == 3:
                self.text.choice_start_y_top = 213
                self.text.choice_start_y_bottom = 53

        else:
            self.text.dialog_start_x = 0
            self.text.dialog_start_y = 0

    def get_scene_change(self):
        scene_index = self.text.current_dialog[1][0]
        return int(scene_index)

    def check_answer(self, x, y):
        if self.choice_box_l_t.on_choice_box(x, y):
            return 1
        elif self.choice_box_l_b.on_choice_box(x, y):
            return 3
        elif self.choice_box_r_t.on_choice_box(x, y):
            return 2
        elif self.choice_box_r_b.on_choice_box(x, y):
            return 4

    def choose_root_story(self, answer):
        print(f"############ send answer! {answer} ############")
        self.text.text_reader.change_path(answer)
        print("############ finish! ############")

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
        # print('---------------------------------------------------------------------------')
        # print(self.text.count_line_break())

    def display_character(self):
        self.character.draw()

    def update_category(self):
        if self.text.current_dialog[0] == 'D':
            self.is_dialog = True
            self.is_choice = False
            self.scene_change = False
        elif self.text.current_dialog[0] == 'Q':
            self.is_dialog = False
            self.is_choice = True
            self.scene_change = False
        elif self.text.current_dialog[0] == 'S':
            self.is_dialog = False
            self.is_choice = False
            self.scene_change = True
        elif self.text.current_dialog[0] == 'P':
            self.is_dialog = False
            self.is_choice = False
            self.scene_change = False


class Status:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
