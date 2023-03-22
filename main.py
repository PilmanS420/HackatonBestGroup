from classes.Button import Button
import pygame
from constants import *
from helpers import *
from buttons import *


def stage_queue():
    global current_stage

    background_image = pygame.transform.scale(pygame.image.load("images/background_images/background1.png"),
                                              (WINDOW_WIDTH, WINDOW_HEIGHT))
    take_order_dialog_window = pygame.image.load("images/other/take_order_dialog_window.png")
    while current_stage == "queue":
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if queue_stage_button_dictionary["take_order"].clicked_on(mouse_pos):
                    current_stage = "order"
                    return None
        screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        screen.blit(take_order_dialog_window, (TAKE_ORDER_X, TAKE_ORDER_Y))
        current_stage = level_buttons(current_stage)
        pygame.display.flip()


def stage_kosher():
    global current_stage
    global kosher
    """
    stage settings
    
    """
    background = pygame.image.load("images/background_images/kosher_or_not_screen.png")
    background = pygame.transform.scale(background, (BACKGROUND_SCREENS_WIDTH, BACKGROUND_SCREENS_HEIGHT))
    while current_stage == "kosher":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None
            mouse_pos = pygame.mouse.get_pos()
            found_mouse_on = False
            for button in kosher_button_dictionary.values():
                if not found_mouse_on:
                    found_mouse_on = button.mouse_on(mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if kosher_button_dictionary["kosher"].clicked_on(mouse_pos):
                    kosher = True
                    current_stage = "queue"
                    return None
                elif kosher_button_dictionary["not kosher"].clicked_on(mouse_pos):
                    kosher = False
                    current_stage = "queue"
                    return None
        screen.blit(background, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        pygame.display.flip()


def stage_start():
    global current_stage
    """
    stage settings

    """
    background = pygame.image.load("images/background_images/main_menu_screen.png")
    background = pygame.transform.scale(background, (BACKGROUND_SCREENS_WIDTH, BACKGROUND_SCREENS_HEIGHT))
    while current_stage == "start":
        screen.blit(background, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None
            mouse_pos = pygame.mouse.get_pos()
            found_mouse_on = False
            for button in menu_button_dictionary.values():
                if not found_mouse_on:
                    found_mouse_on = button.mouse_on(mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button_dictionary["start"].clicked_on(mouse_pos):
                    current_stage = "kosher"
                    return None
                if menu_button_dictionary["exit"].clicked_on(mouse_pos):
                    current_stage = "exit"
                    return None
        pygame.display.flip()


def stage_order():
    global current_stage

    background_image = pygame.transform.scale(pygame.image.load("images/background_images/order_background.png"),
                                              (WINDOW_WIDTH, WINDOW_HEIGHT))
    order_image = pygame.transform.scale(pygame.image.load("images/other/order.png"), ORDER_SIZE)

    while current_stage == "order":
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(mouse_pos)
        screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        screen.blit(order_image, ORDER_POS)
        current_stage = level_buttons(current_stage)
        pygame.display.flip()


def stage_ingredients():
    global current_stage

    background_image = pygame.transform.scale(pygame.image.load("images/background_images/kosher_toppy.jpg"),
                                              (WINDOW_WIDTH, WINDOW_HEIGHT))
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(mouse_pos)
        if mouse_on_any_button(screen_navigation_button_dictionary, mouse_pos) or\
                mouse_on_any_button(toppings_stage_button_dictionary, mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        screen.blit(background_image, (0, 0))
        # screen.blit(spoon_image, mouse_pos)
        pygame.display.flip()


# Main function to manage stages
def main():
    global current_stage
    global kosher
    # Setting up pygame window
    pygame.init()
    pygame.display.set_caption("Shawarmaria")

    # Game stages loop
    while current_stage != "exit":
        if current_stage == "start":
            stage_start()
        elif current_stage == "kosher":
            stage_kosher()
        elif current_stage == "queue":
            stage_queue()
        elif current_stage == "order":
            stage_order()
        elif current_stage == "ingredients":
            stage_ingredients()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    global current_stage
    main()
