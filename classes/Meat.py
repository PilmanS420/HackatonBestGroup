from settings import *
from surfaces import meat_images


class Meat:
    def __init__(self, roasting, on_laffa_x_pos, on_laffa_y_pos):
        self.roasting = roasting
        self.on_laffa_x_pos = on_laffa_x_pos
        self.on_laffa_y_pos = on_laffa_y_pos

    def show(self, laffa_x_pos, laffa_y_pos):
        screen.blit(meat_images[self.roasting], (laffa_x_pos + self.on_laffa_x_pos, laffa_y_pos + self.on_laffa_y_pos))
