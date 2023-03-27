from settings import *
from classes.Order import Order
import random
from surfaces import empty_text_box, laffas_images, topping_images


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

    def show_text_window(self, to_show, ingredient_num=0):  # TODO: add new images to present ingredients better
        screen.blit(empty_text_box, TEXT_BOX_COORDINATES)
        if to_show == "meat":
            pass
        elif to_show == "laffa":
            screen.blit(laffas_images[self.order.get_laffa()], TEXT_BOX_COORDINATES)
        else:
            screen.blit(topping_images[self.order.get_ingredient(ingredient_num)], TEXT_BOX_COORDINATES)


