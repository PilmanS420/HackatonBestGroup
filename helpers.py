import pygame
from constants import *
from buttons import screen_navigation_button_dictionary
from surfaces import *
import random
from classes.Order import Order
from classes.Customer import Customer

# There are help functions to use in the project

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
current_stage = "start"  # A variable keep current activity name to manage game screens


def mouse_on_any_button(buttons_dict, mouse_pos):
    for i in buttons_dict:
        if buttons_dict[i].clicked_on(mouse_pos):
            return True
    return False


def level_buttons(mouse_pos):  # always drawn over background TODO: figure out why the buttons sometimes dont work
    if screen_navigation_button_dictionary["queue"].mouse_on(mouse_pos):
        return "queue"
    elif screen_navigation_button_dictionary["bread station"].mouse_on(mouse_pos):
        return "exit"
    elif screen_navigation_button_dictionary["cooking station"].mouse_on(mouse_pos):
        return "exit"
    elif screen_navigation_button_dictionary["topping station"].mouse_on(mouse_pos):
        return "toppings"
    return current_stage


def get_random_customer():
    criticism = random.randint(CUSTOMER_MIN_CRITICISM, CUSTOMER_MAX_CRITICISM)
    waiting = random.randint(CUSTOMER_MIN_WAIT_TIME, CUSTOMER_MAX_WAIT_TIME)
    customer_type = random.choice(CUSTOMER_TYPES)
    if customer_type == "Bob":
        customer_images = bob_customer_images
    else:
        customer_images = bob_customer_images  # TODO: edit to other types
    return Customer(get_random_order(), waiting, criticism, customer_images)


def get_random_order():
    laffa = random.choice(LAFFAS_LIST)
    has_meat = random.randint(1, 5)
    if has_meat >= 4:
        meat = True
    else:
        meat = False
    toppings_count = random.randint(MIN_INGREDIENTS_REQUESTED, MAX_INGREDIENTS_REQUESTED)
    potential_ingredients = list(INGREDIENTS_LIST)
    final_ingredients = []
    for i in range(toppings_count):
        topping_num = random.randint(0, len(potential_ingredients) - 1)
        final_ingredients.append(potential_ingredients[topping_num])
        del potential_ingredients[topping_num]
    return Order(laffa, meat, final_ingredients)
