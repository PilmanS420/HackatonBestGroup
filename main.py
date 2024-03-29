import time

from settings import *
from classes.Button import Button
from helpers import *
import pygame
from constants import *
from buttons import *
from surfaces import *
from classes.Ingredient import Ingredient
from classes.FallingIngredient import FallingIngredient
from classes.Order import Order
from classes.Customer import Customer
import math


def stage_settings():
    pygame.quit()


def stage_queue():
    global current_stage, waiting_to_order_customers, waiting_to_take_away_customers, new_coming_customer, has_new_coming_customer, time_counter

    background_image = pygame.transform.scale(pygame.image.load("images/background_images/background1.png"),
                                              (WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    pygame.mixer.music.stop()
    while current_stage == "queue":
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None
            if event.type == pygame.USEREVENT:
                time_counter -= 1
                if time_counter <= 0:
                    current_stage = "exit"
                    return None
                if come_new_customer(time_counter):
                    has_new_coming_customer = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if len(waiting_to_order_customers) > 0 and take_order_button["take order"].mouse_on_button(mouse_pos):
                    waiting_to_take_away_customers.append(waiting_to_order_customers[0])
                    del waiting_to_order_customers[0]
                    move_the_queue(waiting_to_order_customers, CUSTOMER_END_PATH_QUEUE, QUEUE_OFFSET)
                    current_stage = "order"
                    return None
                for button in screen_navigation_button_dictionary.keys():
                    if screen_navigation_button_dictionary[button].mouse_on_button(
                            mouse_pos) and button != current_stage:
                        current_stage = button
                        return None

        # Cursor management
        if mouse_on_any_button(screen_navigation_button_dictionary, mouse_pos) or \
                (mouse_on_any_button(take_order_button, mouse_pos) and len(
                    waiting_to_order_customers) > 0):  # Show the button only if any customer is at queue
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # Gives new customer when has a command to that (has_new_coming_customer is True)
        if has_new_coming_customer:
            new_coming_customer = get_random_customer()
            has_new_coming_customer = False

        # Cursor management
        if waiting_to_order_customers:
            set_mouse_on(mouse_pos, screen_navigation_button_dictionary, take_order_button)
        else:
            set_mouse_on(mouse_pos, screen_navigation_button_dictionary)

        # Showing scene
        screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        screen.blit(screen_buttons_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        screen.blit(timer_font.render(str(time_counter), True, TIMER_COLOR), TIMER_POSITION)

        # Showing customers at the back that are waiting to take their shawarma
        for i in waiting_to_take_away_customers:
            i.show()

        # Showing animation of new coming customer
        if new_coming_customer is not None:
            new_coming_customer.set_position(customer_steps_imitation(new_coming_customer.get_position()[0]))
            new_coming_customer.update(CUSTOMER_SPEED)
            new_coming_customer.show()
            if new_coming_customer.get_position()[0] <= CUSTOMER_END_PATH_QUEUE[0] + QUEUE_OFFSET * len(
                    waiting_to_order_customers):
                new_coming_customer.change_image("queue")
                waiting_to_order_customers.append(new_coming_customer)
                new_coming_customer = None
        if len(waiting_to_order_customers) > 0:
            screen.blit(take_order_dialog_window, TAKE_ORDER_COORDINATES)

        # Showing customers are waiting at nearest queue
        for i in waiting_to_order_customers:
            i.show()
        if waiting_to_take_away_customers:
            has_meat = 0
            if waiting_to_take_away_customers[0].get_order().has_meat():
                has_meat = 1
            waiting_to_take_away_customers[0].get_order().show_like_order(waiting_to_take_away_customers[0].get_order().get_toppings_types_count() + has_meat, ORDER_SIZE)
        pygame.display.flip()
        clock.tick(60)


def stage_kosher():
    global current_stage
    global kosher
    background = pygame.image.load("images/background_images/kosher_or_not_screen.png")
    background = pygame.transform.scale(background, (BACKGROUND_SCREENS_WIDTH, BACKGROUND_SCREENS_HEIGHT))
    while current_stage == "kosher":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None
            mouse_pos = pygame.mouse.get_pos()
            set_mouse_on(mouse_pos, kosher_button_dictionary)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if kosher_button_dictionary["kosher"].mouse_on_button(mouse_pos):
                    kosher = True
                    current_stage = "queue"
                    return None
                elif kosher_button_dictionary["not kosher"].mouse_on_button(mouse_pos):
                    kosher = False
                    current_stage = "queue"
                    return None
        screen.blit(background, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        pygame.display.flip()


def stage_start():
    global current_stage
    background = pygame.image.load("images/background_images/main_menu_screen.png")
    background = pygame.transform.scale(background, (BACKGROUND_SCREENS_WIDTH, BACKGROUND_SCREENS_HEIGHT))
    pygame.mixer.music.load("music/main menu theme.mp3")
    pygame.mixer.music.play(-1)
    while current_stage == "start":
        screen.blit(background, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None
            mouse_pos = pygame.mouse.get_pos()
            set_mouse_on(mouse_pos, menu_button_dictionary)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button_dictionary["start"].mouse_on_button(mouse_pos):
                    current_stage = "kosher"
                    return None
                if menu_button_dictionary["exit"].mouse_on_button(mouse_pos):
                    current_stage = "exit"
                    return None
        pygame.display.flip()


def stage_order():  # TODO: make queue update to show customers at queue at different locations and not at one place
    global current_stage, waiting_to_take_away_customers, time_counter

    background_image = pygame.transform.scale(pygame.image.load("images/background_images/order_background.png"),
                                              (WINDOW_WIDTH, WINDOW_HEIGHT))
    order_image = pygame.transform.scale(pygame.image.load("images/other/order.png"), ORDER_SIZE_BIG)
    waiting_to_take_away_customers[-1].change_image("order")
    waiting_to_take_away_customers[-1].set_position(CUSTOMER_POSITION_ORDER)

    # Variable keeps current ingredient (including laffa and meat) number
    showing_ingredient_type = "laffa"
    current_topping_num = 0
    # Variable keeps count of ingredients into shawarma including laffa and meat
    toppings_count = waiting_to_take_away_customers[-1].get_order().get_toppings_types_count()

    mouse_pos = pygame.mouse.get_pos()
    set_mouse_on(mouse_pos, on_text_box_button)
    screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
    screen.blit(screen_buttons_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
    waiting_to_take_away_customers[-1].show()
    waiting_to_take_away_customers[-1].show_text_window(showing_ingredient_type, current_topping_num)
    waiting_to_take_away_customers[-1].get_order().show_like_order(current_topping_num, ORDER_SIZE_BIG)

    while current_stage == "order":
        mouse_pos = pygame.mouse.get_pos()
        set_mouse_on(mouse_pos, on_text_box_button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None
            if event.type == pygame.USEREVENT:
                time_counter -= 1
                if time_counter <= 0:
                    current_stage = "exit"
                    return None
                if come_new_customer(time_counter):
                    waiting_to_order_customers.append(get_random_customer())
                    waiting_to_order_customers[-1].set_position(
                        (CUSTOMER_END_PATH_QUEUE[0] + QUEUE_OFFSET * (len(waiting_to_order_customers) - 1),
                         CUSTOMER_END_PATH_QUEUE[1]))
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
                screen.blit(screen_buttons_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
                waiting_to_take_away_customers[-1].show()
                waiting_to_take_away_customers[-1].show_text_window(showing_ingredient_type, current_topping_num)
                waiting_to_take_away_customers[-1].get_order().show_like_order(current_topping_num, ORDER_SIZE_BIG)
                print(mouse_pos)
                if on_text_box_button["text box"].mouse_on_button(mouse_pos):
                    waiting_to_take_away_customers[-1].change_image("order")
                    if showing_ingredient_type == "laffa":
                        if waiting_to_take_away_customers[-1].get_order().has_meat():
                            showing_ingredient_type = "meat"
                        else:
                            showing_ingredient_type = "topping"
                    elif showing_ingredient_type == "meat":
                        showing_ingredient_type = "topping"
                    else:
                        current_topping_num += 1
                    waiting_to_take_away_customers[-1].get_order().show_like_order(current_topping_num, ORDER_SIZE_BIG)
                    if current_topping_num == toppings_count:
                        current_stage = "queue"
                        waiting_to_take_away_customers[-1].change_image("queue")
                        waiting_to_take_away_customers[-1].set_position(
                            (TAKE_AWAY_QUEUE_X_LOCATION + QUEUE_OFFSET * (len(
                                waiting_to_take_away_customers) - 1), TAKE_AWAY_QUEUE_Y_LOCATION))
                        return None
        pygame.display.flip()


def stage_bread():
    global current_stage, time_counter, waiting_to_order_customers
    laffa_1_image = pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_1.png"),
                                           (242, 171))
    laffa_2_image = pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_2.png"),
                                           (242, 171))
    laffa_3_image = pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_3.png"),
                                           (242, 171))
    laffa_1big = pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_1.png"),
                                        (605, 428))
    laffa_2big = pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_2.png"),
                                        (605, 428))
    laffa_3big = pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_3.png"),
                                        (605, 428))
    background_image = pygame.transform.scale(pygame.image.load("images/background_images/stage_bread_start.jpg"),
                                              (WINDOW_WIDTH, WINDOW_HEIGHT))

    background_image_breadready = pygame.transform.scale(
        pygame.image.load("images/background_images/stage_bread_ready.jpg"),
        (WINDOW_WIDTH, WINDOW_HEIGHT))

    background_image_dragging = pygame.transform.scale(
        pygame.image.load("images/background_images/stage_bread_drag.jpg"),
        (WINDOW_WIDTH, WINDOW_HEIGHT))

    is_held_before = False
    laffa_list = []  # laffa images list
    laffa_1_case = False
    laffa_2_case = False
    laffa_3_case = False
    bread_on_screen = False
    currently_dragging = False
    while current_stage == "bread":
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None
            if event.type == pygame.USEREVENT:
                time_counter -= 1
                if time_counter <= 0:
                    current_stage = "exit"
                    return None
                if come_new_customer(time_counter):
                    waiting_to_order_customers.append(get_random_customer())
                    waiting_to_order_customers[-1].set_position(
                        (CUSTOMER_END_PATH_QUEUE[0] + QUEUE_OFFSET * (len(waiting_to_order_customers) - 1),
                         CUSTOMER_END_PATH_QUEUE[1]))
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(mouse_pos)
                for intent in screen_navigation_button_dictionary:
                    if screen_navigation_button_dictionary[intent].mouse_on_button(mouse_pos):
                        if intent != current_stage:
                            current_stage = intent
                            return None
                # TODO: change positions checking to Buttons checking
                if 296 >= mouse_pos[0] >= 165 and 339 >= mouse_pos[1] >= 205:  # laffa 1 pos
                    is_held_before = True
                    laffa_1_case = True
                elif 305 >= mouse_pos[0] >= 171 and 537 >= mouse_pos[1] >= 409:  # laffa 2 pos
                    is_held_before = True
                    laffa_2_case = True
                elif 301 >= mouse_pos[0] >= 170 and 745 >= mouse_pos[1] >= 612:  # laffa 3 pos
                    is_held_before = True
                    laffa_3_case = True

                if bread_on_screen:
                    if 1789 >= mouse_pos[0] >= 1592 and 725 >= mouse_pos[1] >= 530 and \
                            shawarmas_at_stages["toppings"] is None:  # TODO: change to button
                        shawarmas_at_stages["cooking"] = shawarmas_at_stages[current_stage]
                        shawarmas_at_stages[current_stage] = None
                        current_stage = "cooking"  # TODO: MOVE TO STAGE COOKING AND TROUBLESHOOT
                        return None
        # Cursor management
        if mouse_on_any_button(screen_navigation_button_dictionary, mouse_pos):  # TODO: add shawarma buttons
            mouse_on()
        else:
            mouse_off()
        if is_held_before:  # detect if the mouse was pressed on a laffa
            currently_dragging = True
            pygame.mouse.set_visible(False)
            if pygame.mouse.get_pressed(3)[0]:  # detect if the mouse is being held
                if laffa_1_case:
                    if not (laffa_1_image in laffa_list):
                        laffa_list.append(laffa_1_image)
                elif laffa_2_case:
                    if not (laffa_2_image in laffa_list):
                        laffa_list.append(laffa_2_image)
                elif laffa_3_case:
                    if not (laffa_3_image in laffa_list):
                        laffa_list.append(laffa_3_image)
            else:
                currently_dragging = False
                pygame.mouse.set_visible(True)
                hold_release_cords = mouse_pos
                if 726 >= hold_release_cords[1] >= 466 and 1309 >= hold_release_cords[
                    0] >= 721:  # TODO: change to button
                    bread_on_screen = True
                    del shawarmas_at_stages[current_stage]
                    if laffa_1_case:
                        shawarmas_at_stages[current_stage] = Order("Type 1", Meat(0))
                        print("created type 1")
                    elif laffa_2_case:
                        shawarmas_at_stages[current_stage] = Order("Type 2", Meat(0))
                        print("created type 2")
                    elif laffa_3_case:
                        shawarmas_at_stages[current_stage] = Order("Type 3", Meat(0))
                        print("created type 3")
                else:
                    bread_on_screen = False
                    shawarmas_at_stages[current_stage] = None

                if laffa_1_case:
                    laffa_list.remove(laffa_1_image)
                    laffa_1_case = False
                elif laffa_2_case:
                    laffa_list.remove(laffa_2_image)
                    laffa_2_case = False
                elif laffa_3_case:
                    laffa_list.remove(laffa_3_image)
                    laffa_3_case = False
                is_held_before = False

        if not bread_on_screen:  # blit dragging background
            if currently_dragging:
                screen.blit(background_image_dragging, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
            else:
                screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))  # blit existing background
        else:
            screen.blit(background_image_breadready,
                        (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))  # blit new background

        if shawarmas_at_stages[current_stage] is not None:
            shawarmas_at_stages[current_stage].show_like_shawarma(SHAWARMA_BREAD_STAGE_POSITION)

        screen.blit(screen_buttons_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))  # blit screen buttons
        screen.blit(timer_font.render(str(time_counter), True, TIMER_COLOR), TIMER_POSITION)
        if len(laffa_list) >= 1:
            screen.blit(laffa_list[0], mouse_pos)  # blit small dragging laffas

        # working hold mechanism for troubleshooting:

        # if is_held_before:  # detect if the mouse was pressed on a laffa
        #     print("GOT to held before")
        #     if pygame.mouse.get_pressed(3)[0]:  # detect if the mouse is being held
        #         print("got to mouse held")
        #         if not (laffa_1_image in laffa_list):
        #             laffa_list.append(laffa_1_image)
        #     else:
        #         laffa_list.remove(laffa_1_image)
        #         laffa_1_case = False
        #         is_held_before = False
        # screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        # screen.blit(screen_buttons_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        # if len(laffa_list) >= 1:
        #     screen.blit(laffa_list[0], (mouse_pos[0], mouse_pos[1]))
        if waiting_to_take_away_customers:
            has_meat = 0
            if waiting_to_take_away_customers[0].get_order().has_meat():
                has_meat = 1
            waiting_to_take_away_customers[0].get_order().show_like_order(len(waiting_to_take_away_customers[0].get_order().get_topping_types()) + has_meat, ORDER_SIZE)
        pygame.display.flip()


def stage_cooking():  # TODO: Find a way to present animation without lags
    global current_stage, time_counter, waiting_to_order_customers
    background_image = pygame.transform.scale(pygame.image.load("images/background_images/background_cooking.png"),
                                              (WINDOW_WIDTH, WINDOW_HEIGHT))
    meat_list = []
    is_held_before = False
    meat_on_screen = False
    clicked_on_cooked_meat = False
    current_meat = meat_images["raw"][0]
    secs = 0
    font = pygame.font.Font('freesansbold.ttf', 40)
    text = font.render(str(secs), True, (0, 0, 0))
    timing_text = font.render(("Cook meat between 10 and 20 seconds"), True, (0, 0, 0))
    finished_text = font.render(("Click meat"), True, (0, 255, 0))
    clock = pygame.time.Clock()
    done = False
    while current_stage == "cooking":
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None
            if event.type == pygame.USEREVENT:
                time_counter -= 1
                if time_counter <= 0:
                    current_stage = "exit"
                    return None
                if come_new_customer(time_counter):
                    waiting_to_order_customers.append(get_random_customer())
                    waiting_to_order_customers[-1].set_position(
                        (CUSTOMER_END_PATH_QUEUE[0] + QUEUE_OFFSET * (len(waiting_to_order_customers) - 1),
                         CUSTOMER_END_PATH_QUEUE[1]))
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(mouse_pos)
                for intent in screen_navigation_button_dictionary:
                    if screen_navigation_button_dictionary[intent].mouse_on_button(mouse_pos):
                        if intent != current_stage:
                            current_stage = intent
                            return None
                if 280 >= mouse_pos[0] >= 79 and 666 >= mouse_pos[1] >= 332:  # meat pos  # TODO: change to button
                    is_held_before = True
                if 1080 >= mouse_pos[0] >= 892 and 589 >= mouse_pos[1] >= 294:
                    clicked_on_cooked_meat = True

        if is_held_before:  # detect if the mouse was pressed on meat
            if pygame.mouse.get_pressed(3)[0]:  # detect if the mouse is being held
                currently_dragging = True
                pygame.mouse.set_visible(False)
                if not (meat_1_image in meat_list):
                    meat_list.append(meat_1_image)
            else:
                meat_list.remove(meat_1_image)
                is_held_before = False
                currently_dragging = False
                pygame.mouse.set_visible(True)
                hold_release_cords = mouse_pos
                if 966 >= hold_release_cords[0] >= 844 and 430 >= hold_release_cords[1] >= 270 and shawarmas_at_stages[
                    current_stage] is not None:
                    meat_on_screen = True
                else:
                    meat_on_screen = False

        screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        screen.blit(screen_buttons_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        screen.blit(timer_font.render(str(time_counter), True, TIMER_COLOR), TIMER_POSITION)

        if meat_on_screen:  # cook meat and display timer
            if secs < 10:
                text = font.render(str(secs), True, (0, 0, 0))
                current_meat = meat_images["raw"][0]
            elif 20 >= secs >= 10:
                text = font.render(str(secs), True, (0, 255, 0))
                current_meat = meat_images["medium"][0]
                screen.blit(finished_text, (1370, 460))
            elif secs > 20:
                text = font.render(str(secs), True, (200, 0, 0))
                current_meat = meat_images["well done"][0]
                screen.blit(finished_text, (1370, 460))

            if clicked_on_cooked_meat:  # animation of clicked meat
                if current_meat == meat_images["raw"][0]:
                    screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
                    screen.blit(meat_images["raw"][1], (766, 214))
                    pygame.display.flip()

                    pygame.time.wait(1000)
                    screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
                    screen.blit(meat_images["raw"][2], (766, 214))
                    pygame.display.flip()

                    pygame.time.wait(1000)
                    screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
                    screen.blit(meat_images["raw"][3], (766, 214))
                    pygame.display.flip()

                    # pygame.time.wait(1000)
                    # for i in range(60):
                    #     screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
                    #     shawarmas_at_stages[current_stage].show_like_shawarma((720, (1100-(5*i))))
                    #     clock.tick(60)
                    #     pygame.display.flip()
                elif current_meat == meat_images["medium"][0]:
                    screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
                    screen.blit(meat_images["medium"][1], (766, 214))
                    pygame.display.flip()

                    pygame.time.wait(1000)
                    screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
                    screen.blit(meat_images["medium"][2], (766, 214))
                    pygame.display.flip()

                    pygame.time.wait(1000)
                    screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
                    screen.blit(meat_images["medium"][3], (766, 214))
                    pygame.display.flip()

                    # pygame.time.wait(1000)
                    # for i in range(420):
                    #     screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
                    #     shawarmas_at_stages[current_stage].show_like_shawarma((720, (1100-(2*i))))
                    #     pygame.display.flip()

                elif current_meat == meat_images["well done"][0]:
                    screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
                    screen.blit(meat_images["well done"][1], (766, 214))
                    pygame.display.flip()

                    pygame.time.wait(1000)
                    screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
                    screen.blit(meat_images["well done"][2], (766, 214))
                    pygame.display.flip()

                    pygame.time.wait(1000)
                    screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
                    screen.blit(meat_images["well done"][3], (766, 214))
                    pygame.display.flip()

                    # pygame.time.wait(1000)
                    # for i in range(420):
                    #     screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
                    #     shawarmas_at_stages[current_stage].show_like_shawarma(720, (1100-(2*i)))
                    #     pygame.display.flip()

                pygame.time.wait(500)
                screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
                shawarmas_at_stages[current_stage].add_meat()
                shawarmas_at_stages[current_stage].show_like_shawarma((720, 200))
                pygame.display.flip()

                pygame.time.wait(1000)
                screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
                shawarmas_at_stages[current_stage].add_meat()
                shawarmas_at_stages[current_stage].show_like_shawarma((720, 200))
                pygame.display.flip()

                pygame.time.wait(1000)
                screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
                shawarmas_at_stages[current_stage].add_meat()
                shawarmas_at_stages[current_stage].show_like_shawarma((720, 200))
                pygame.display.flip()

                pygame.time.wait(1000)
                shawarmas_at_stages["toppings"] = shawarmas_at_stages[current_stage]
                shawarmas_at_stages[current_stage] = None
                current_stage = "toppings"
                pygame.display.flip()
                return None

            screen.blit(timing_text, (1100, 400))
            screen.blit(current_meat, (766, 214))
            screen.blit(timer_border, (876, 74))
            clock.tick(1)
            secs += 1
            screen.blit(text, (970, 96))
            print(secs)

        if len(meat_list) >= 1:
            screen.blit(meat_list[0], (mouse_pos[0] - 100, mouse_pos[1] - 100))
        if waiting_to_take_away_customers:
            has_meat = 0
            if waiting_to_take_away_customers[0].get_order().has_meat():
                has_meat = 1
            waiting_to_take_away_customers[0].get_order().show_like_order(waiting_to_take_away_customers[0].get_order().get_toppings_types_count() + has_meat, ORDER_SIZE)
        pygame.display.flip()


def stage_toppings():
    global current_stage, time_counter, waiting_to_order_customers

    background_image = pygame.transform.scale(pygame.image.load("images/background_images/kosher_toppy.jpg"),
                                              (WINDOW_WIDTH, WINDOW_HEIGHT))
    current_topping = "None"
    spoon_cursor = False  # Variable presenting if user holds a spoon and don't need a default cursor
    falling_ingredients = []
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None
            if event.type == pygame.USEREVENT:
                time_counter -= 1
                if time_counter <= 0:
                    current_stage = "exit"
                    return None
                if come_new_customer(time_counter):
                    waiting_to_order_customers.append(get_random_customer())
                    waiting_to_order_customers[-1].set_position((CUSTOMER_END_PATH_QUEUE[0] + QUEUE_OFFSET * (
                                len(waiting_to_order_customers) - 1), CUSTOMER_END_PATH_QUEUE[1]))
            if event.type == pygame.MOUSEBUTTONDOWN:
                for topping in toppings_stage_button_dictionary:  # A cycle checking if one of toppings has taken
                    if toppings_stage_button_dictionary[topping].mouse_on_button(mouse_pos):
                        if topping == current_topping:
                            current_topping = "None"
                            spoon_cursor = False
                        else:
                            current_topping = topping
                            spoon_cursor = True
                for intent in screen_navigation_button_dictionary:
                    if screen_navigation_button_dictionary[intent].mouse_on_button(mouse_pos):
                        if intent != current_stage:
                            current_stage = intent
                            return None
                if shawarmas_at_stages[current_stage] is not None and \
                        toppings_falling_area_button.mouse_on_button(mouse_pos) and spoon_cursor:
                    falling_ingredients.append(FallingIngredient(current_topping, mouse_pos[0] - LAFFA_X_POS,
                                                                 mouse_pos[
                                                                     1] - LAFFA_Y_POS + TOPPINGS_ABOVE_LAFFA_OFFSET,
                                                                 mouse_pos[1]))
                if not spoon_cursor and checkmark_button.mouse_on_button(mouse_pos) and len(
                        waiting_to_take_away_customers) > 0 and shawarmas_at_stages[current_stage] is not None:
                    shawarmas_at_stages["take order"] = shawarmas_at_stages[current_stage]
                    shawarmas_at_stages[current_stage] = None
                    current_stage = "take order"
                    waiting_to_take_away_customers[0].change_image("think")
                    waiting_to_take_away_customers[0].set_position(CUSTOMER_POSITION_ORDER)
                    return None

        screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        screen.blit(screen_buttons_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        screen.blit(timer_font.render(str(time_counter), True, TIMER_COLOR), TIMER_POSITION)
        if len(waiting_to_take_away_customers) > 0 and shawarmas_at_stages[current_stage] is not None:
            screen.blit(checkmark_image, CHECKMARK_POSITION)
        if shawarmas_at_stages[current_stage] is not None:
            shawarmas_at_stages[current_stage].show_like_shawarma((LAFFA_X_POS, LAFFA_Y_POS))

        # Falling toppings updating and bliting
        indexes_to_delete = []
        for i in range(len(falling_ingredients)):
            if falling_ingredients[i].is_landed(LAFFA_Y_POS):
                shawarmas_at_stages[current_stage].add_topping(falling_ingredients[i])
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
            if mouse_on_any_button(toppings_stage_button_dictionary, mouse_pos) or \
                    toppings_falling_area_button.mouse_on_button(mouse_pos) and \
                    shawarmas_at_stages[current_stage] is not None:
                screen.blit(rotated_spoon_images[current_topping], (mouse_pos[0], mouse_pos[1] - SPOON_HEIGHT * 3))
            else:
                screen.blit(spoon_images[current_topping], mouse_pos)
        else:
            pygame.mouse.set_visible(True)

            if mouse_on_any_button(screen_navigation_button_dictionary, mouse_pos) or \
                    mouse_on_any_button(toppings_stage_button_dictionary, mouse_pos) or \
                    checkmark_button.mouse_on_button(mouse_pos) and len(waiting_to_take_away_customers) > 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if waiting_to_take_away_customers:
            has_meat = 0
            if waiting_to_take_away_customers[0].get_order().has_meat():
                has_meat = 1
            waiting_to_take_away_customers[0].get_order().show_like_order(waiting_to_take_away_customers[0].get_order().get_toppings_types_count() + has_meat, ORDER_SIZE)
        pygame.display.flip()


def stage_take_order():
    global current_stage
    background_image = pygame.transform.scale(pygame.image.load("images/background_images/order_background.png"),
                                              (WINDOW_WIDTH, WINDOW_HEIGHT))
    my_timer = 500
    pygame.mixer.Sound("sound/drum roll.mp3").play()
    while current_stage == "take order":
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if my_timer < 0 and checkmark_button.mouse_on_button(mouse_pos):
                    del waiting_to_take_away_customers[0]
                    move_the_queue(waiting_to_take_away_customers,
                                   (TAKE_AWAY_QUEUE_X_LOCATION, TAKE_AWAY_QUEUE_Y_LOCATION), QUEUE_OFFSET)
                    current_stage = "queue"
                    shawarmas_at_stages[current_stage] = None
                    return None
        if my_timer < 0 and checkmark_button.mouse_on_button(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        screen.blit(background_image, (BACKGROUND_SCREENS_X, BACKGROUND_SCREENS_Y))
        shawarmas_at_stages[current_stage].show_like_shawarma(SHAWARMA_TAKE_ORDER_STAGE_POSITION, True)
        waiting_to_take_away_customers[0].show()
        if my_timer > 0:
            my_timer -= 1
        elif my_timer == 0:
            my_timer -= 1
            grade = calculate_grade(waiting_to_take_away_customers[0].get_order(), shawarmas_at_stages[current_stage])
            print(grade)
            if 80 < grade <= 100:
                waiting_to_take_away_customers[0].change_image("reaction", "best")
            elif 60 < grade <= 80:
                waiting_to_take_away_customers[0].change_image("reaction", "good")
            elif 40 < grade <= 60:
                waiting_to_take_away_customers[0].change_image("reaction", "normal")
            elif 20 < grade <= 40:
                waiting_to_take_away_customers[0].change_image("reaction", "bad")
            elif 0 <= grade <= 20:
                waiting_to_take_away_customers[0].change_image("reaction", "worst")
        else:
            screen.blit(checkmark_image, CHECKMARK_POSITION)
        if waiting_to_take_away_customers:
            has_meat = 0
            if waiting_to_take_away_customers[0].get_order().has_meat():
                has_meat = 1
            waiting_to_take_away_customers[0].get_order().show_like_order(waiting_to_take_away_customers[0].get_order().get_toppings_types_count() + has_meat, ORDER_SIZE)
        pygame.display.flip()


def stage_difficulty_select():
    pass


# Main function to manage stages
def main():
    global current_stage
    global kosher

    # Game stages loop
    while current_stage != "exit":
        if current_stage == "start":
            stage_start()
        elif current_stage == "kosher":
            stage_kosher()
        elif current_stage == "difficulty select":
            stage_difficulty_select()
        elif current_stage == "queue":
            stage_queue()
        elif current_stage == "order":
            stage_order()
        elif current_stage == "bread":
            stage_bread()
        elif current_stage == "cooking":
            stage_cooking()
        elif current_stage == "toppings":
            stage_toppings()
        elif current_stage == "take order":
            stage_take_order()
        elif current_stage == "settings":
            stage_settings()
    pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    global difficulty_setting
    global current_stage
    global new_coming_customer
    global waiting_to_order_customers
    global waiting_to_take_away_customers
    global has_new_coming_customer
    main()
