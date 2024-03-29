from settings import *
from classes.Order import Order
import random
from surfaces import empty_text_box, laffas_speech_box_images, topping_speech_box_images, meat_to_present_in_speech


class Customer:
    def __init__(self, order, waiting_timer, criticism, images_dict, position):
        self.order = order
        self.waiting_timer = waiting_timer
        self.criticism = criticism
        self.images = images_dict
        self.current_image = random.choice(self.images["queue"])
        self.position = list(position)

    def get_cooking_timer(self):
        return self.waiting_timer

    def get_order(self):
        return self.order

    def get_criticism(self):
        return self.criticism

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = list(position)

    def show(self):
        screen.blit(self.current_image, self.position)

    def update(self, move_by_x=0, move_by_y=0):
        self.position[0] += float(move_by_x)
        self.position[1] += float(move_by_y)

    def change_image(self, action, reaction="normal"):
        if action == "reaction":
            self.current_image = random.choice(self.images[action][reaction])
        else:
            self.current_image = random.choice(self.images[action])

    def show_text_window(self, to_show, ingredient_num=0):  # TODO: add new images to present ingredients better (Aviel)
        screen.blit(empty_text_box, TEXT_BOX_COORDINATES)
        if to_show == "meat":
            screen.blit(meat_to_present_in_speech["meat"], (TEXT_BOX_COORDINATES[0] + 43, TEXT_BOX_COORDINATES[1] + 35))
        elif to_show == "laffa":
            screen.blit(laffas_speech_box_images[self.order.get_laffa()], (TEXT_BOX_COORDINATES[0] + 43, TEXT_BOX_COORDINATES[1] + 35))
        else:
            screen.blit(topping_speech_box_images[self.order.get_uniqe_ingredient_name(ingredient_num)], (TEXT_BOX_COORDINATES[0] + 43, TEXT_BOX_COORDINATES[1] + 35))


