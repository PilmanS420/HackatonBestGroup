from settings import *
from classes.Order import Order
import random


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
        self.position[0] += move_by_x
        self.position[1] += move_by_y

    def change_image(self, action, reaction="normal"):
        if action == "reaction":
            self.current_image = random.choice(self.images[action][reaction])
        else:
            self.current_image = random.choice(self.images[action])
