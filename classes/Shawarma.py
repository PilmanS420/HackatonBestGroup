from helpers import *
from surfaces import laffas_images


class Shawarma:
    def __init__(self, laffa):
        self.laffa = laffa
        self.meat = []
        self.toppings = []

    def show(self, x_pos, y_pos):
        screen.blit(laffas_images[self.laffa], (x_pos, y_pos))
