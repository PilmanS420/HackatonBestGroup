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
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
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


def stage_start():
    global current_stage
    """
    stage settings

    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None


def stage_order():
    global current_stage

    background_image = pygame.transform.scale(pygame.image.load("images/background_images/33333.jpg"),
                                              (WINDOW_WIDTH, WINDOW_HEIGHT))
    order_image = pygame.transform.scale(pygame.image.load("images/other/order.png"), ORDER_SIZE)

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(mouse_pos)
        if mouse_on_any_button(stages_navigation_button_dictionary, mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        screen.blit(background_image, (0, 0))
        screen.blit(order_image, ORDER_POS)
        pygame.display.flip()


# Main function to manage stages
def main():
    global current_stage
    # Setting up pygame window
    pygame.init()
    pygame.display.set_caption("Shawarmaria")

    current_stage = "queue"
    # Game stages loop
    while current_stage != "exit":
        if current_stage == "start":
            stage_start()
        elif current_stage == "queue":
            stage_queue()
        elif current_stage == "order":
            stage_order()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    global current_stage
    main()
