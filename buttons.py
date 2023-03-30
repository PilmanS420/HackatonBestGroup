from classes.Button import Button
from constants import *

# Create buttons dictionary

# Dictionary for buttons for moving from screen to screen:
# Buttons for the screens at the bottom:
screen_navigation_button_dictionary = {"queue": Button(*SCREEN_BUTTON_ORDER_LOCATION),
                                       "bread": Button(*SCREEN_BUTTON_BREAD_LOCATION),
                                       "cooking": Button(*SCREEN_BUTTON_COOKING_LOCATION),
                                       "toppings": Button(*SCREEN_BUTTON_TOPPING_LOCATION),
                                       "settings": Button(*SCREEN_BUTTON_SETTINGS),
                                       "exit": Button(*SCREEN_BUTTON_EXIT)}

# Buttons for the title screen:
menu_button_dictionary = {"start": Button(*START_BUTTON_LOCATION),
                          "exit": Button(*EXIT_BUTTON_LOCATION),
                          "settings": Button(*SETTINGS_BUTTON_LOCATION)}

# Buttons for the setting screen:
settings_button_dictionary = {"exit": Button(*EXIT_BUTTON_LOCATION),
                              "settings": Button(*SETTINGS_BUTTON_LOCATION)}

# Buttons for the kosher screen:
kosher_button_dictionary = {"kosher": Button(*KOSHER_BUTTON_LOCATION),
                            "not kosher": Button(*NOT_KOSHER_LOCATION)}

# A button represents a text window to take order of a customer at the queue
take_order_button = {"take order": Button(*TAKE_ORDER_BUTTON_LOCATION)}

# Buttons for topping bowls in the topping stage
toppings_stage_button_dictionary = {
    "harif": Button(LEFT_TOPPINGS_X_POS, TOPPINGS_Y_POS, TOPPING_BOX_WIDTH, TOPPING_BOX_HEIGHT),
    "humus": Button(LEFT_TOPPINGS_X_POS, TOPPINGS_Y_POS + TOPPING_BOX_HEIGHT + TOPPINGS_OFFSET, TOPPING_BOX_WIDTH, TOPPING_BOX_HEIGHT),
    "cucumber": Button(LEFT_TOPPINGS_X_POS, TOPPINGS_Y_POS + 2 * (TOPPING_BOX_HEIGHT + TOPPINGS_OFFSET), TOPPING_BOX_WIDTH, TOPPING_BOX_HEIGHT),
    "thina": Button(RIGHT_TOPPINGS_X_POS, TOPPINGS_Y_POS, TOPPING_BOX_WIDTH, TOPPING_BOX_HEIGHT),
    "salat": Button(RIGHT_TOPPINGS_X_POS, TOPPINGS_Y_POS + TOPPING_BOX_HEIGHT + TOPPINGS_OFFSET, TOPPING_BOX_WIDTH, TOPPING_BOX_HEIGHT),
    "onion": Button(RIGHT_TOPPINGS_X_POS, TOPPINGS_Y_POS + 2 * (TOPPING_BOX_HEIGHT + TOPPINGS_OFFSET), TOPPING_BOX_WIDTH, TOPPING_BOX_HEIGHT)}

checkmark_button = Button(CHECKMARK_POSITION[0], CHECKMARK_POSITION[1], CHECKMARK_SIZE[0], CHECKMARK_SIZE[1])

# Variable keeps area for toppings station, where you can throw ingredients on lafa
toppings_falling_area_button = Button(LAFFA_X_POS, LAFFA_Y_POS - TOPPINGS_ABOVE_LAFFA_OFFSET, SHAWARMA_SIZE[0], SHAWARMA_SIZE[1])

# Order stage
on_text_box_button = {"text box": Button(TEXT_BOX_COORDINATES[0], TEXT_BOX_COORDINATES[1], TEXT_BOX_SIZE[0], TEXT_BOX_SIZE[1])}
