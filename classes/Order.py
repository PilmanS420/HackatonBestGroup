from settings import *
from surfaces import *
from classes.Ingredient import Ingredient


class Order:
    def __init__(self, laffa, meat_count=0, ingredient_list=[]):
        self.laffa = laffa
        self.meat_count = meat_count
        self.toppings = ingredient_list

    def add_topping(self, topping):
        self.toppings.append(Ingredient(topping.name, topping.on_laffa_x_pos, topping.on_laffa_y_pos))

    def add_meat(self):
        self.meat_count += 1

    def show_like_order(self, steps):
        screen.blit(laffas_order_images[self.get_laffa()], ORDER_LOCATION)
        order_ingredient_locations = []
        for step in range(1, steps):
            if step > 1:
                order_ingredient_location = (ORDER_LOCATION[0] + ORDER_INGREDIENT_SIZE[0], ORDER_LOCATION[1])
                order_ingredient_locations.append(order_ingredient_location)
        ingredient_num = 0
        for order_ingredient_location in order_ingredient_locations:
            screen.blit(topping_order_images[self.get_ingredient(ingredient_num)], order_ingredient_location)
            ingredient_num += 1

    def show_like_shawarma(self, shawarma_position, size="medium"):
        if self.meat_count == 0:
            if size == "small":
                screen.blit(laffas_speech_box_images[self.laffa], shawarma_position)
            else:
                screen.blit(laffas_images[self.laffa], shawarma_position)
        else:
            if size == "small":
                screen.blit(laffas_with_meat_small_images[self.laffa][self.meat_count - 1], shawarma_position)
            else:
                screen.blit(laffas_with_meat_medium_images[self.laffa][self.meat_count - 1], shawarma_position)
        for topping in self.toppings:
            topping.show(shawarma_position, size)

    def get_ingredient(self, number):
        return self.toppings[number]

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
