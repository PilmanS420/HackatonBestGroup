from classes.Button import Button
from constants import *

# Create buttons dictionary

# Dictionary for buttons for moving from screen to screen:
screen_button_dictionary = {"customer": Button(*SCREEN_BUTTON_CUSTOMER_LOCATION), "precooking": Button(*SCREEN_BUTTON_PRECOOKING_LOCATION), "cooking": Button(*SCREEN_BUTTON_COOKING_LOCATION), "finishing": Button(*SCREEN_BUTTON_FINISHING_LOCATION)}