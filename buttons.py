from classes.Button import Button
from constants import *

# Create buttons dictionary

# Dictionary for buttons for moving from screen to screen:
# Buttons for the screens at the bottom: TODO: replace the names of the indexes
screen_navigation_button_dictionary = {"queue": Button(*SCREEN_BUTTON_ORDER_LOCATION), "bread": Button(*SCREEN_BUTTON_BREAD_LOCATION), "cooking": Button(*SCREEN_BUTTON_COOKING_LOCATION), "toppings": Button(*SCREEN_BUTTON_TOPPING_LOCATION)}

# Buttons for the title screen:
menu_button_dictionary = {"start": Button(*START_BUTTON_LOCATION), "exit": Button(*EXIT_BUTTON_LOCATION)}

# Buttons for the kosher screen:
kosher_button_dictionary = {"kosher": Button(*KOSHER_BUTTON_LOCATION), "not kosher": Button(*NOT_KOSHER_LOCATION)}

# TODO: egor, replace this TODO with a description for this dictionary
queue_stage_button_dictionary = {"take_order": Button(*TAKE_ORDER_BUTTON_LOCATION)}

toppings_stage_button_dictionary = {"harif": Button(LEFT_TOPPINGS_X_POS, TOPPINGS_Y_POS, TOPPING_BOX_WIDTH, TOPPING_BOX_HEIGHT),
                                    "humus": Button(LEFT_TOPPINGS_X_POS, TOPPINGS_Y_POS + TOPPING_BOX_HEIGHT + TOPPINGS_OFFSET,
                                                    TOPPING_BOX_WIDTH, TOPPING_BOX_HEIGHT),
                                    "cucumber": Button(LEFT_TOPPINGS_X_POS,
                                                       TOPPINGS_Y_POS + 2 * (TOPPING_BOX_HEIGHT + TOPPINGS_OFFSET),
                                                       TOPPING_BOX_WIDTH, TOPPING_BOX_HEIGHT),
                                    "thina": Button(RIGHT_TOPPINGS_X_POS, TOPPINGS_Y_POS, TOPPING_BOX_WIDTH, TOPPING_BOX_HEIGHT),
                                    "salat": Button(RIGHT_TOPPINGS_X_POS, TOPPINGS_Y_POS + TOPPING_BOX_HEIGHT + TOPPINGS_OFFSET,
                                                    TOPPING_BOX_WIDTH, TOPPING_BOX_HEIGHT),
                                    "onion": Button(RIGHT_TOPPINGS_X_POS,
                                                    TOPPINGS_Y_POS + 2 * (TOPPING_BOX_HEIGHT + TOPPINGS_OFFSET),
                                                    TOPPING_BOX_WIDTH, TOPPING_BOX_HEIGHT)}

# Variable keeps area for toppings station, where you can throw ingredients on lafa
toppings_falling_area_button = Button(LAFA_X_POS, LAFA_Y_POS - TOPPINGS_ABOVE_LAFA_OFFSET, LAFA_WIDTH, LAFA_HEIGHT)
