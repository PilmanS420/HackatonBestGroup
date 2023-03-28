from settings import *
from surfaces import topping_images
from classes.Ingredient import Ingredient


ACCELERATION = 2


class FallingIngredient(Ingredient):
    def __init__(self, name, on_laffa_x_pos, on_laffa_y_pos, real_y_pos):
        super().__init__(name, on_laffa_x_pos, on_laffa_y_pos)
        self.real_y_pos = real_y_pos
        self.speed = 0.1

    def show(self, laffa_x_pos, real_y_pos):
        screen.blit(topping_images[self.name], (self.on_laffa_x_pos + laffa_x_pos, self.real_y_pos))

    def update(self, laffa_y_pos):
        self.speed *= ACCELERATION
        self.real_y_pos += self.speed
        if self.real_y_pos > laffa_y_pos + self.on_laffa_y_pos:
            self.real_y_pos = laffa_y_pos + self.on_laffa_y_pos
            self.speed = 0

    def is_landed(self, shawarma_y_pos):
        return self.real_y_pos == shawarma_y_pos + self.on_laffa_y_pos

