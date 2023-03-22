import pygame
from constants import *
from buttons import screen_navigation_button_dictionary
from surfaces import screen_buttons_image

# There are help functions to use in the project

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
current_stage = "toppings"  # A variable keep current activity name to manage game screens


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
