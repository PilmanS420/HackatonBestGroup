import pygame
from constants import *

# There are first pygame window settings
pygame.init()
pygame.display.set_caption("Shawarmaria")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Global variables
current_stage = "start"  # A variable keep current activity name to manage game screens
current_customer = None
new_coming_customer = None
waiting_to_order_customers = []
waiting_to_take_away_customers = []
has_new_coming_customer = True
shawarmas_at_stages = {"bread": None, "cooking": None, "toppings": None, "take order": None}
