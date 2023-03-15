from classes.Button import Button
from constants import *

# Create buttons dictionary

# Dictionary for buttons for moving from screen to screen:
## Buttons for the screens at the bottom: TODO: replace the names of the indexes
### screen_button_dictionary = {"customer": Button(*SCREEN_BUTTON_CUSTOMER_LOCATION), "precooking": Button(*SCREEN_BUTTON_PRECOOKING_LOCATION), "cooking": Button(*SCREEN_BUTTON_COOKING_LOCATION), "finishing": Button(*SCREEN_BUTTON_FINISHING_LOCATION)}

## Buttons for the title screen:
menu_button_dictionary = {"start": Button(*START_BUTTON_LOCATION), "exit": Button(*EXIT_BUTTON_LOCATION)}

## Buttons for the kosher screen:
kosher_button_dictionary = {"kosher": Button(*KOSHER_BUTTON_LOCATION), "not kosher": Button(*NOT_KOSHER_LOCATION)}

## TODO: egor, replace this TODO with a description for this dictionary
queue_stage_button_dictionary = {"take_order": Button(*TAKE_ORDER_BUTTON_LOCATION)}
