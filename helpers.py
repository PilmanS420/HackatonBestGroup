import pygame
from constants import *
from buttons import screen_navigation_button_dictionary
from surfaces import *
import random
from classes.Order import Order
from classes.Customer import Customer
from classes.Ingredient import Ingredient
import math
from typing import List
from collections import Counter
from math import ceil
from classes.Meat import Meat



def mouse_on_any_button(buttons_dict, mouse_pos):
    for button in buttons_dict.keys():
        if buttons_dict[button].mouse_on_button(mouse_pos):
            return True
    return False


def get_random_customer():
    criticism = random.randint(CUSTOMER_MIN_CRITICISM, CUSTOMER_MAX_CRITICISM)
    waiting = random.randint(CUSTOMER_MIN_WAIT_TIME, CUSTOMER_MAX_WAIT_TIME)
    customer_type = random.choice(CUSTOMER_TYPES)
    if customer_type == "Bob":
        customer_images = bob_customer_images
    elif customer_type == "Lucy":
        customer_images = lucy_customer_images
    elif customer_type == "Jack":
        customer_images = jack_customer_images
    else:
        customer_images = trollface_customer_images
    return Customer(get_random_order(), waiting, criticism, customer_images, CUSTOMER_START_PATH_QUEUE)


def get_random_order():
    laffa = random.choice(LAFFAS_LIST)
    meat = Meat(3, "medium")
    toppings_count = random.randint(MIN_INGREDIENTS_REQUESTED, MAX_INGREDIENTS_REQUESTED)
    potential_ingredients = list(INGREDIENTS_LIST)
    final_ingredients = []
    for i in range(toppings_count):
        topping_num = random.randint(0, len(potential_ingredients) - 1)
        for j in range(BEST_TOPPINGS_ON_LAFFA_COUNT):
            final_ingredients.append(Ingredient(potential_ingredients[topping_num],
                                                SHAWARMA_MEDIUM_SIZE[0] // 2, SHAWARMA_MEDIUM_SIZE[1] // 2))
        del potential_ingredients[topping_num]
    return Order(laffa, meat, final_ingredients)


def customer_steps_imitation(x_pos):
    return [x_pos, CUSTOMER_START_PATH_QUEUE[1] - abs(50 * math.sin(x_pos / 50))]


def mouse_on():
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


def mouse_off():
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


def set_mouse_on(mouse_pos, dictionary1, dictionary2=None, dictionary3=None, dictionary4=None):
    if dictionary2 is not None:
        dictionary_library = [dictionary1, dictionary2]
    elif dictionary3 is not None:
        dictionary_library = [dictionary1, dictionary2, dictionary3]
    elif dictionary4 is not None:
        dictionary_library = [dictionary1, dictionary2, dictionary3, dictionary4]
    else:
        dictionary_library = [dictionary1]

    for dictionary in dictionary_library:
        if mouse_on_any_button(dictionary, mouse_pos):
            mouse_on()
            return
    mouse_off()


def come_new_customer(timer_counter, difficulty_setting="MEDIUM"):
    if difficulty_setting == "HARD":
        return timer_counter % NEW_CUSTOMERS_COOLDOWN_HARD == 0 and len(waiting_to_take_away_customers) + len(waiting_to_order_customers) < 5
    elif difficulty_setting == "MEDIUM":
        return timer_counter % NEW_CUSTOMERS_COOLDOWN_MEDIUM == 0 and len(waiting_to_take_away_customers) + len(waiting_to_order_customers) < 5
    return timer_counter % NEW_CUSTOMERS_COOLDOWN_EASY == 0 and len(waiting_to_take_away_customers) + len(waiting_to_order_customers) < 5


def move_the_queue(queue, queue_first_position, queue_offset):
    for i in range(len(queue)):
        queue[i].set_position((queue_first_position[0] + queue_offset * i, queue_first_position[1]))


# Function compair two shawarmas: customer`s order and player`s shawarma
def calculate_grade(customer_order: Order, player_shawarma: Order) -> int:
    grade = 0
    # check bread type
    if customer_order.laffa == player_shawarma.laffa:
        grade += 30
        print("for laffa", 30)

    # check meat type
    if customer_order.get_meat_count() == player_shawarma.get_meat_count() and customer_order.meat.get_roasting() == player_shawarma.meat.get_roasting():
        grade += 30
        print("for meat", 30)

    # check toppings amount
    points = 0
    toppings_count_order = {}
    toppings_count_shawarma = {}
    for i in INGREDIENTS_LIST:
        toppings_count_order[i] = 0
        toppings_count_shawarma[i] = 0
    for i in customer_order.toppings:
        toppings_count_order[i.get_name()] += 1
    for i in customer_order.toppings:
        toppings_count_shawarma[i.get_name()] += 1
    for i in toppings_count_order.keys():
        if toppings_count_order[i] == toppings_count_shawarma[i]:
            points += 1
        elif not(toppings_count_order[i] == 0 and toppings_count_shawarma[i] != 0 or
                 toppings_count_order[i] != 0 and toppings_count_shawarma[i] == 0):  # Checks if there is no missing or extra ingredient type
            if toppings_count_order[i] > toppings_count_shawarma[i]:
                points += toppings_count_shawarma[i] / toppings_count_order[i]
            else:
                points += toppings_count_order[i] / toppings_count_shawarma[i]
    # # Check toppings' placement. This part of checks used to check if toppings on shawarma are spread on laffa equally
    # toppings_placements_order = {}
    # toppings_placements_shawarma = {}
    # sum_toppings_placements_order = {}
    # sum_toppings_placements_shawarma = {}
    # for i in INGREDIENTS_LIST:
    #     toppings_placements_order[i] = []
    #     toppings_placements_shawarma[i] = []
    # for i in customer_order.toppings:
    #     toppings_placements_order[i.get_name()].append(i.get_on_laffa_position())
    # for i in player_shawarma.toppings:
    #     toppings_placements_shawarma[i.get_name()].append(i.get_on_laffa_position())
    # # Sum all placements
    # for i in toppings_placements_order.keys():
    #     sum_toppings_placements_order[i] = sum_tuples(toppings_placements_order[i])
    # for i in toppings_placements_shawarma.keys():
    #     sum_toppings_placements_shawarma[i] = sum_tuples(toppings_placements_shawarma[i])
    # # Arithmetical center:
    # arithmetical_tuples_order = {}
    # arithmetical_tuples_shawarma = {}
    # for i in sum_toppings_placements_order.keys():
    #     if toppings_count_order[i] != 0:
    #         arithmetical_tuples_order[i] = (sum_toppings_placements_order[i][0] / toppings_count_order[i],
    #                                         sum_toppings_placements_order[i][0] / toppings_count_order[i])
    #     else:
    #         arithmetical_tuples_order[i] = (0, 0)
    # for i in sum_toppings_placements_shawarma.keys():
    #     if toppings_count_shawarma[i] != 0:
    #         arithmetical_tuples_shawarma[i] = (sum_toppings_placements_shawarma[i][0] / toppings_count_shawarma[i],
    #                                            sum_toppings_placements_shawarma[i][0] / toppings_count_shawarma[i])
    #     else:
    #         arithmetical_tuples_shawarma[i] = (0, 0)
    # mon = 1
    # for i in arithmetical_tuples_order.keys():
    #     if not(arithmetical_tuples_order[i][0] == 0 or arithmetical_tuples_order[i][1] == 0) and\
    #             not(arithmetical_tuples_shawarma[i][0] == 0 or arithmetical_tuples_shawarma[i][1] == 0):
    #         if arithmetical_tuples_order[i][0] > arithmetical_tuples_shawarma[i][0]:
    #             mon *= arithmetical_tuples_shawarma[i][0] / arithmetical_tuples_order[i][0]
    #         else:
    #             mon *= arithmetical_tuples_order[i][0] / arithmetical_tuples_shawarma[i][0]
    #         if arithmetical_tuples_order[i][1] > arithmetical_tuples_shawarma[i][1]:
    #             mon *= arithmetical_tuples_shawarma[i][1] / arithmetical_tuples_order[i][1]
    #         else:
    #             mon *= arithmetical_tuples_order[i][1] / arithmetical_tuples_shawarma[i][1]

    grade += points / 6 * 40
    print("for count", points / 6 * 40)
    # print("for placement", mon * 20)
    # grade += mon * 20

    return grade


def sum_tuples(ls: List) ->tuple:
    tup = [0, 0]
    for i in ls:
        tup[0] += i[0]
        tup[1] += i[1]
    return tuple(tup)



def settings_screen():
    in_settings_screen = True
    while in_settings_screen:

        in_settings_screen = False
