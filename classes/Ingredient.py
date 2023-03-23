from surfaces import topping_images
from helpers import *


class Ingredient:
    def __init__(self, name, on_laffa_x_pos, on_laffa_y_pos):
        self.name = name
        self.on_laffa_x_pos = on_laffa_x_pos
        self.on_laffa_y_pos = on_laffa_y_pos

    def show(self, laffa_x_pos, laffa_y_pos):
        screen.blit(topping_images[self.name], (laffa_x_pos + self.on_laffa_x_pos, laffa_y_pos + self.on_laffa_y_pos))
