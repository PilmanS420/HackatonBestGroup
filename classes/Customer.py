from random import randint
from classes.Order import Order
from constants import *
import random
from helpers import *


class Customer:
    def __init__(self, order, waiting_timer, criticism, images_dict):
        self.order = order
        self.waiting_timer = waiting_timer
        self.criticism = criticism
        self.images = images_dict
        self.current_image = random.choice(self.images["come"])

    def get_cooking_timer(self):
        return self.waiting_timer

    def get_order(self):
        return self.order

    def show(self, position, action):
        screen.blit(random.choice(self.images[action]), position)
