from settings import *
from surfaces import *


class Order:
    def __init__(self, laffa, meat=True, ingredient_list=[]):
        self.laffa = laffa
        self.meat = meat
        self.toppings = ingredient_list

    def show(self, x_pos, y_pos):
        screen.blit(laffas_images[self.laffa], (x_pos, y_pos))

    def add_topping(self, topping):
        self.toppings.append(topping)

    def add_ingredient(self, ingredient):
        self.toppings.append(ingredient)

    def show_like_order(self):
        pass

    def show_like_shawarma(self):
        pass

    def get_ingredient(self, number):
        return self.toppings[number]

    def get_toppings_count(self):
        return len(self.toppings)

    def get_laffa(self):
        return self.laffa

    def has_meat(self):
        return self.meat

    def compare(self, my_shawarma):
        """
        Future function compares THIS imagination shawarma and shawarma the user did

        :param my_shawarma:
        :return: percent 0 to 100
        """
        pass
