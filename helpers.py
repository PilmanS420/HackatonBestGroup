import pygame
from constants import *

# There are help functions to use in the project

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
current_stage = "start"  # A variable keep current activity name to manage game screens


def mouse_on_any_button(buttons_dict, mouse_pos):
    for i in buttons_dict:
        if buttons_dict[i].mouse_on(mouse_pos):
            return True
    return False
