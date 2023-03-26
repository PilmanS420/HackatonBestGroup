import pygame
from constants import *

# There are first pygame window settings
pygame.init()
pygame.display.set_caption("Shawarmaria")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
current_stage = "start"  # A variable keep current activity name to manage game screens
