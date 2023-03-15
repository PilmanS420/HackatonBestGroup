from constants import *


class Order:
    def __init__(self, ingredients_left=None, ingredients_middle=None, ingredients_right=None):
        # The shawarma consists of 3 invisible parts, to ensure you putted same ingredients count on all shawarma

        self.ingredients = [ingredients_left, ingredients_middle, ingredients_right]  # Three parts are dictionaries

    def add_ingredient(self, ingredient, amount, zone):
        if ingredient in self.ingredients[zone]:
            self.ingredients[zone][ingredient] += amount
        else:
            self.ingredients[zone][ingredient] = amount

    def order_to_present(self):
        ingredients_to_display = []
        for ingredient in self.ingredients:
            ingredients_to_display.append(ingredient)
        return ingredients_to_display

    def compare(self, my_shawarma):
        """
        Future function compares THIS imagination shawarma and shawarma the user did

        :param my_shawarma:
        :return: percent 0 to 100
        """
        pass
