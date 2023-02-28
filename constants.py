# Width and Height of the project window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Title screen size and location on the screen
TITLE_SCREEN_WIDTH = int(WINDOW_WIDTH / (2 + (2 / 3)))
TITLE_SCREEN_HEIGHT = int(WINDOW_HEIGHT / 3)
TITLE_SCREEN_X = int(WINDOW_WIDTH / (5 + (1 / 3)))
TITLE_SCREEN_Y = int(WINDOW_WIDTH / 8)

# Main menu button sizes and locations on the screen
MENU_BUTTON_OFFSET = int(WINDOW_HEIGHT / 12)
MENU_BUTTON_WIDTH = int(WINDOW_WIDTH / 8)
MENU_BUTTON_HEIGHT = int(WINDOW_HEIGHT / 7.5)
MENU_BUTTON_X = int(MENU_BUTTON_WIDTH - (WINDOW_WIDTH / 16))
MENU_BUTTON_Y = int(WINDOW_WIDTH / 4)
MENU_START = (MENU_BUTTON_X, MENU_BUTTON_Y, MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT)
MENU_EXIT = (MENU_BUTTON_X, MENU_BUTTON_Y + MENU_BUTTON_OFFSET, MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT)

# Screen movement button sizes and locations on the screen
SCREEN_BUTTON_OFFSET = int(WINDOW_WIDTH / 4)
SCREEN_BUTTON_X = int(WINDOW_WIDTH / 8)
SCREEN_BUTTON_WIDTH = int(WINDOW_WIDTH / 10)
SCREEN_BUTTON_HEIGHT = int(WINDOW_HEIGHT / 10)
SCREEN_BUTTON_Y = WINDOW_WIDTH - SCREEN_BUTTON_HEIGHT
SCREEN_BUTTON_CUSTOMER_LOCATION = (SCREEN_BUTTON_X, SCREEN_BUTTON_Y, SCREEN_BUTTON_WIDTH, SCREEN_BUTTON_HEIGHT)
SCREEN_BUTTON_PRECOOKING_LOCATION = (SCREEN_BUTTON_X + SCREEN_BUTTON_OFFSET, SCREEN_BUTTON_Y, SCREEN_BUTTON_WIDTH, SCREEN_BUTTON_HEIGHT)
SCREEN_BUTTON_COOKING_LOCATION = (SCREEN_BUTTON_X + (SCREEN_BUTTON_OFFSET * 2), SCREEN_BUTTON_Y, SCREEN_BUTTON_WIDTH, SCREEN_BUTTON_HEIGHT)
SCREEN_BUTTON_FINISHING_LOCATION = (SCREEN_BUTTON_X + (SCREEN_BUTTON_OFFSET * 3), SCREEN_BUTTON_Y, SCREEN_BUTTON_WIDTH, SCREEN_BUTTON_HEIGHT)