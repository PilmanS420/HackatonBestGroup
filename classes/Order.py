from constants import *
class Order:
    def __init__(self, ingredients = None, meat_type = None):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        if not (ingredient in self.ingredients) or not (len(self.ingredients) == MAX_INGREDIENTS_REQUESTED):
            self.ingredients.append(ingredient)

    def check_customer(self, customer):
        correct_order = True
        for order_ingredient in self.ingredients:
            if order_ingredient not in customer.get_ingredients():
                correct_order = False
        return correct_order
