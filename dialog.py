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
    pass


class ChoiceBox(arcade.Sprite):
    pass


class Text:
    pass


class DialogDrawer(arcade.Sprite):
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        # self.background_pics = ["images/forest_background.jpg", "images/forest_background_2.jpg"]
        # self.background_pic = self.background_pics[0]
        # self.character_pic = ""

    # def change_background(self):
    #     next_index = self.background_pics.index(self.background_pic) + 1
    #     if next_index < len(self.background_pics):
    #         self.background_pic = self.background_pics[next_index]
    #     else:
    #         return

    def display_dialog_box(self):
        width = self.screen_width - 150     # 1350
        height = self.screen_height // 3    # 240
        center_x = self.screen_width // 2
        center_y = (height // 2) + 30
        arcade.draw_rectangle_filled(center_x, center_y, width, height, arcade.color.WHITE)

    def display_choice_box(self):
        width = self.screen_width // 2.3    # 652
        height = self.screen_height // 4    # 180
        top_margin = height // 2
        left_margin = width // 2

        center_x_left = left_margin + (self.screen_width - (self.screen_width - 75))
        center_x_right = self.screen_width - left_margin - 75

        # center_y_bottom = (self.screen_height // 3) + (self.screen_height // 3) // 2 + top_margin
        center_y_bottom = self.screen_height // 2 + 25
        center_y_top = center_y_bottom + top_margin + 125

        arcade.draw_rectangle_filled(center_x_left, center_y_bottom, width, height, arcade.color.BLACK)
        arcade.draw_rectangle_filled(center_x_left, center_y_top, width, height, arcade.color.BLACK)
        arcade.draw_rectangle_filled(center_x_right, center_y_top, width, height, arcade.color.BLACK)
        arcade.draw_rectangle_filled(center_x_right, center_y_bottom, width, height, arcade.color.BLACK)
