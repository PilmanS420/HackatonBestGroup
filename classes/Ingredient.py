from settings import *
from surfaces import topping_images


class Ingredient:
    def __init__(self, name, on_laffa_x_pos, on_laffa_y_pos):
        self.name = name
        self.on_laffa_x_pos = on_laffa_x_pos
        self.on_laffa_y_pos = on_laffa_y_pos

    def show(self, shawarma_position):
        screen.blit(topping_images[self.name], (shawarma_position[0] + self.on_laffa_x_pos,
                                                shawarma_position[1] + self.on_laffa_y_pos))
