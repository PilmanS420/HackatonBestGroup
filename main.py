from classes.Button import Button
import pygame
from constants import *
from helpers import *
from buttons import *
from surfaces import *
from classes.Ingredient import Ingredient
from classes.FallingIngredient import FallingIngredient
from classes.Order import Order


def stage_queue():
    global current_stage

    background_image = pygame.transform.scale(pygame.image.load("images/background_images/background1.png"),
                                              (WINDOW_WIDTH, WINDOW_HEIGHT))

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
                for intent in screen_navigation_button_dictionary:
                    if screen_navigation_button_dictionary[intent].mouse_on(mouse_pos):
                        if intent != current_stage:
                            current_stage = intent
                            return None
        if mouse_on_any_button(screen_navigation_button_dictionary, mouse_pos) or \
                mouse_on_any_button(queue_stage_button_dictionary, mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        screen.blit(screen_buttons_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        screen.blit(take_order_dialog_window, (TAKE_ORDER_X, TAKE_ORDER_Y))
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
                for intent in screen_navigation_button_dictionary:
                    if screen_navigation_button_dictionary[intent].mouse_on(mouse_pos):
                        if intent != current_stage:
                            current_stage = intent
                            return None
        screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        screen.blit(screen_buttons_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        screen.blit(order_image, ORDER_POS)
        pygame.display.flip()


def stage_toppings():
    global current_stage

    background_image = pygame.transform.scale(pygame.image.load("images/background_images/kosher_toppy.jpg"),
                                              (WINDOW_WIDTH, WINDOW_HEIGHT))
    current_topping = "None"
    spoon_cursor = False  # Variable presenting if user holds a spoon and don't need a default cursor
    falling_ingredients = []
    shawarma = Order("Laffa 1")
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(mouse_pos)  # TODO: delete this print
                for topping in toppings_stage_button_dictionary:  # A cycle checking if one of toppings has taken
                    if toppings_stage_button_dictionary[topping].mouse_on(mouse_pos):
                        if topping == current_topping:
                            current_topping = "None"
                            spoon_cursor = False
                        else:
                            current_topping = topping
                            spoon_cursor = True
                for intent in screen_navigation_button_dictionary:
                    if screen_navigation_button_dictionary[intent].mouse_on(mouse_pos):
                        if intent != current_stage:
                            current_stage = intent
                            return None
                if toppings_falling_area_button.mouse_on(mouse_pos) and spoon_cursor:
                    falling_ingredients.append(FallingIngredient(current_topping, mouse_pos[0] - LAFFA_X_POS,
                                                                 mouse_pos[1] - LAFFA_Y_POS + TOPPINGS_ABOVE_LAFFA_OFFSET, mouse_pos[1]))

        screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        screen.blit(screen_buttons_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        screen.blit(laffas_images["Type 1"], (LAFFA_X_POS, LAFFA_Y_POS))

        # Falling toppings updating and bliting
        indexes_to_delete = []
        for i in range(len(falling_ingredients)):
            if falling_ingredients[i].is_landed(LAFFA_Y_POS):
                shawarma.add_topping(falling_ingredients[i])
                indexes_to_delete.append(i)
            falling_ingredients[i].update(LAFFA_Y_POS)
            falling_ingredients[i].show(LAFFA_X_POS, falling_ingredients[i].real_y_pos)
        # Cleaning - already felt toppings are removing
        for i in range(len(falling_ingredients), -1, -1):
            if i in indexes_to_delete:
                del falling_ingredients[i]

        # At the bottom of the screen need to be a default cursor and not a spoon
        if mouse_pos[1] > 940:
            spoon_cursor = False
        elif current_topping != "None":
            # When mouse comes back from the bottom navigation bar, cursor turns to spoon if there is any ingredient on it
            spoon_cursor = True

        # Custom cursor bliting and default cursor changing
        if spoon_cursor:
            pygame.mouse.set_visible(False)
            if mouse_on_any_button(toppings_stage_button_dictionary, mouse_pos) or toppings_falling_area_button.mouse_on(mouse_pos):
                screen.blit(rotated_spoon_images[current_topping], (mouse_pos[0], mouse_pos[1] - SPOON_HEIGHT * 3))
            else:
                screen.blit(spoon_images[current_topping], mouse_pos)
        else:
            pygame.mouse.set_visible(True)
            if mouse_on_any_button(screen_navigation_button_dictionary, mouse_pos) or\
                    mouse_on_any_button(toppings_stage_button_dictionary, mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
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
        elif current_stage == "toppings":
            stage_toppings()
    pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    global current_stage
    main()
