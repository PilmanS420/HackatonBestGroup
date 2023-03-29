from settings import *
from surfaces import *
from classes.Ingredient import Ingredient


class Order:
    def __init__(self, laffa, meat_count=0, ingredient_list=[]):
        self.laffa = laffa
        self.meat_count = meat_count
        self.toppings = []
        for i in ingredient_list:
            self.toppings.append(Ingredient(i.name, i.on_laffa_x_pos, i.on_laffa_y_pos))

    def add_topping(self, topping):
        self.toppings.append(Ingredient(topping.name, topping.on_laffa_x_pos, topping.on_laffa_y_pos))

    def add_meat(self):
        self.meat_count += 1

    def show_like_order(self):
        pass

    def show_like_shawarma(self, shawarma_position, size="medium"):
        if self.meat_count == 0:
            if size == "small":
                screen.blit(laffas_medium_images[self.laffa], shawarma_position)
            else:
                screen.blit(laffas_small_images[self.laffa], shawarma_position)
        else:
            if size == "small":
                screen.blit(laffas_with_meat_small_images[self.laffa][self.meat_count - 1], shawarma_position)
            else:
                screen.blit(laffas_with_meat_medium_images[self.laffa][self.meat_count - 1], shawarma_position)
        for topping in self.toppings:
            topping.show(shawarma_position, size)

    def get_ingredient_name(self, number):
        return self.toppings[number].name

    def get_toppings_count(self):
        return len(self.toppings)

    def get_laffa(self):
        return self.laffa

    def has_meat(self):
        return self.meat_count != 0

    def compare(self, my_shawarma):
        """
        Future function compares THIS imagination shawarma and shawarma the user did

        :param my_shawarma:
        :return: percent 0 to 100
        """
        pass
