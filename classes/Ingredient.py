from settings import *
from surfaces import topping_images


class Ingredient:
    def __init__(self, name, on_laffa_x_pos, on_laffa_y_pos):
        self.name = name
        self.on_laffa_x_pos = on_laffa_x_pos
        self.on_laffa_y_pos = on_laffa_y_pos

    def show(self, shawarma_position, size):
        if size == "small":
            screen.blit(topping_images[self.name], (shawarma_position[0] + self.on_laffa_x_pos * (SHAWARMA_SMALL_SIZE[0] / SHAWARMA_MEDIUM_SIZE[0]),
                                                    shawarma_position[1] + self.on_laffa_y_pos * (SHAWARMA_SMALL_SIZE[1] / SHAWARMA_MEDIUM_SIZE[1])))
        else:
            screen.blit(topping_images[self.name], (shawarma_position[0] + self.on_laffa_x_pos,
                                                    shawarma_position[1] + self.on_laffa_y_pos))

    def get_on_laffa_position(self):
        position = (self.on_laffa_x_pos, self.on_laffa_y_pos)
        return position

    def get_name(self):
        return self.name
