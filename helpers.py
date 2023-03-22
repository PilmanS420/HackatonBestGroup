import pygame
from constants import *
from buttons import screen_navigation_button_dictionary

# There are help functions to use in the project

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
current_stage = "ingredients"  # A variable keep current activity name to manage game screens


def mouse_on_any_button(buttons_dict, mouse_pos):
    for i in buttons_dict:
        if buttons_dict[i].clicked_on(mouse_pos):
            return True
    return False


def level_buttons(current_stage):  # always drawn over background TODO: figure out why the buttons sometimes dont work
    screen_buttons_image = pygame.image.load("images/background_images/screen_buttons.png")
    screen_buttons_image = pygame.transform.scale(screen_buttons_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "exit"
        if event.type == pygame.MOUSEBUTTONDOWN:
            if screen_navigation_button_dictionary["order station"].clicked_on(pos):
                return "queue"
            elif screen_navigation_button_dictionary["bread station"].clicked_on(pos):
                return "exit"
            elif screen_navigation_button_dictionary["cooking station"].clicked_on(pos):
                return "exit"
            elif screen_navigation_button_dictionary["topping station"].clicked_on(pos):
                return "exit"
    if mouse_on_any_button(screen_navigation_button_dictionary, pos):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    screen.blit(screen_buttons_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
    return current_stage
