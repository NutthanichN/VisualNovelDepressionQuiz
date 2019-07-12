"""
12/7/19 4:17
1.change dialog&choice box to sprite or not? --> yes consider size
2.build mouse motion (try to use only this file) --> check is mouse at choice box
3.think how to change first dialog to others dialog with/without background change
4.ask whose file will use as a main (to run game window) --> do I have to write it my self?
5.ask size of game window
"""
import arcade


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
    pass


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

        # self.background_pics = ["images/forest_background.jpg", "images/forest_background_2.jpg"]
        # self.background_pic = self.background_pics[0]
        # self.character_pic = ""

    # def change_background(self):
    #     next_index = self.background_pics.index(self.background_pic) + 1
    #     if next_index < len(self.background_pics):
    #         self.background_pic = self.background_pics[next_index]
    #     else:
    #         return

    def set_up_choice_boxes(self):
        self.choice_box_l_t.set_up_position(True, False, False, False)
        self.choice_box_l_b.set_up_position(False, True, False, False)
        self.choice_box_r_t.set_up_position(False, False, True, False)
        self.choice_box_r_b.set_up_position(False, False, False, True)

    def display_dialog_box(self):
        self.dialog_box.draw()
        # width = self.screen_width - 150     # 1350
        # height = self.screen_height // 3    # 240
        # center_x = self.screen_width // 2
        # center_y = (height // 2) + 30
        # arcade.draw_rectangle_filled(center_x, center_y, width, height, arcade.color.WHITE)

    def display_choice_and_question_box(self):
        # width = self.screen_width // 2.3    # 652
        # height = self.screen_height // 4    # 180
        # top_margin = height // 2            # 90
        # left_margin = width // 2            # 326
        #
        # center_x_left = left_margin + (self.screen_width - (self.screen_width - 75))    # 251
        # center_x_right = self.screen_width - left_margin - 75       #
        #
        # center_y_bottom = self.screen_height // 2 + 25      # 385
        # center_y_top = center_y_bottom + top_margin + 125   # 600
        #
        # arcade.draw_rectangle_filled(center_x_left, center_y_bottom, width, height, arcade.color.BLACK)
        # arcade.draw_rectangle_filled(center_x_left, center_y_top, width, height, arcade.color.BLACK)
        # arcade.draw_rectangle_filled(center_x_right, center_y_top, width, height, arcade.color.BLACK)
        # arcade.draw_rectangle_filled(center_x_right, center_y_bottom, width, height, arcade.color.BLACK)
        self.question_box.draw()

        self.choice_box_l_t.draw()
        self.choice_box_l_b.draw()
        self.choice_box_r_t.draw()
        self.choice_box_r_b.draw()