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
    while True:
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(mouse_pos)
                if queue_stage_button_dictionary["take_order"].mouse_on(mouse_pos):
                    current_stage = "order"
                    return None
            if mouse_on_any_button(queue_stage_button_dictionary, mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        screen.blit(background_image, (0, 0))
        screen.blit(take_order_dialog_window, (TAKE_ORDER_X_POS, TAKE_ORDER_Y_POS))
        pygame.display.flip()


def stage_kosher():
    global current_stage
    global kosher
    """
    stage settings
    
    """
    background = pygame.image.load("images/background_images/kosher_or_not_screen.png")
    background = pygame.transform.scale(background, (BACKGROUND_SCREENS_WIDTH, BACKGROUND_SCREENS_HEIGHT))
    while True:
        screen.blit(background, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if kosher_button_dictionary["kosher"].mouse_on(pos):
                    kosher = True
                    current_stage = "exit"
                    return None
                elif kosher_button_dictionary["not kosher"].mouse_on(pos):
                    kosher = False
                    current_stage = "exit"
                    return None
        pygame.display.flip()


def stage_start():
    global current_stage
    """
    stage settings

    """
    background = pygame.image.load("images/background_images/main menu screen.png")
    background = pygame.transform.scale(background, (BACKGROUND_SCREENS_WIDTH, BACKGROUND_SCREENS_HEIGHT))
    while True:
        screen.blit(background, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if menu_button_dictionary["start"].mouse_on(pos):
                    current_stage = "kosher"
                    return None
                if menu_button_dictionary["exit"].mouse_on(pos):
                    current_stage = "exit"
                    return None
        pygame.display.flip()


# Main function to manage stages
def main():
    global current_stage
    global kosher
    # Setting up pygame window
    pygame.init()
    pygame.display.set_caption("Shawarmaria")

    current_stage = "start"
    # Game stages loop
    while current_stage != "exit":
        if current_stage == "start":
            stage_start()
        elif current_stage == "kosher":
            stage_kosher()
        elif current_stage == "queue":
            stage_queue()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    global current_stage
    main()
