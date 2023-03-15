from random import randint
from classes.Order import Order
from constants import *
class Customer:
    def __init__(self): # TODO: add more stuff
        self.ingredient_amount = randint(MIN_INGREDIENTS_REQUESTED, MAX_INGREDIENTS_REQUESTED)
        if MIN_INGREDIENTS_REQUESTED < self.ingredient_amount < MAX_INGREDIENTS_REQUESTED:
            self.ingredients = None # TODO: wait for ingredient class to be made so i can make customer request random ingredients
        self.patience = None # might be used later, leaving a placeholder
        self.cooking_timer = 60 # in seconds
        self.order = Order(self.ingredients, self.meat_type)

    def get_cooking_timer(self):
        return self.cooking_timer
    def get_ingredient_amount(self):
        return self.ingredient_amount

    def get_ingredients(self):
        return self.ingredients


