# Width and Height of the project window
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

# Timer
TIMER_POSITION = (22, 954)
TIMER_COLOR = (255, 255, 255)

# Constants for order creation
MIN_INGREDIENTS_REQUESTED = 1
MAX_INGREDIENTS_REQUESTED = 5
INGREDIENTS_LIST = ("harif", "humus", "cucumber", "thina", "salat", "onion")
LAFFAS_LIST = ("Type 1", "Type 2", "Type 3")

# Background screens size and location on the screen
BACKGROUND_SCREENS_X = 0
BACKGROUND_SCREENS_Y = 0
BACKGROUND_SCREENS_WIDTH = WINDOW_WIDTH
BACKGROUND_SCREENS_HEIGHT = WINDOW_HEIGHT

# Main menu button sizes and locations on the screen
START_BUTTON_X = 720
START_BUTTON_Y = 780
START_BUTTON_WIDTH = 1275 - START_BUTTON_X
START_BUTTON_HEIGHT = 980 - START_BUTTON_Y
START_BUTTON_LOCATION = (START_BUTTON_X, START_BUTTON_Y, START_BUTTON_WIDTH, START_BUTTON_HEIGHT)
## The exit and settings buttons
MENU_BUTTON_OFFSET = 39
MENU_BUTTON_X = 24
MENU_BUTTON_Y = 24
MENU_BUTTON_WIDTH = 168 - MENU_BUTTON_X
MENU_BUTTON_HEIGHT = 157 - MENU_BUTTON_Y
EXIT_BUTTON_LOCATION = (MENU_BUTTON_X, MENU_BUTTON_Y, MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT)
SETTINGS_BUTTON_LOCATION = (
    MENU_BUTTON_X, MENU_BUTTON_Y + MENU_BUTTON_HEIGHT + MENU_BUTTON_OFFSET, MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT)

# Kosher screen button sizes and locations on the screen
KOSHER_BUTTON_X = 251
KOSHER_BUTTON_Y = 453
KOSHER_BUTTON_WIDTH = 836 - KOSHER_BUTTON_X
KOSHER_BUTTON_HEIGHT = 754 - KOSHER_BUTTON_Y
KOSHER_BUTTON_LOCATION = (KOSHER_BUTTON_X, KOSHER_BUTTON_Y, KOSHER_BUTTON_WIDTH, KOSHER_BUTTON_HEIGHT)

NOT_KOSHER_BUTTON_X = 1082
NOT_KOSHER_BUTTON_Y = 454
NOT_KOSHER_BUTTON_WIDTH = 1665 - NOT_KOSHER_BUTTON_X
NOT_KOSHER_BUTTON_HEIGHT = 754 - NOT_KOSHER_BUTTON_Y
NOT_KOSHER_LOCATION = (NOT_KOSHER_BUTTON_X, NOT_KOSHER_BUTTON_Y, NOT_KOSHER_BUTTON_WIDTH, NOT_KOSHER_BUTTON_HEIGHT)

# Screen movement button sizes and locations on the screen
SCREEN_BUTTON_OFFSET = 35
SCREEN_BUTTON_X = 464
SCREEN_BUTTON_Y = 965
SCREEN_BUTTON_WIDTH = 700 - SCREEN_BUTTON_X
SCREEN_BUTTON_HEIGHT = 1064 - SCREEN_BUTTON_Y
SCREEN_BUTTON_ORDER_LOCATION = (SCREEN_BUTTON_X, SCREEN_BUTTON_Y, SCREEN_BUTTON_WIDTH, SCREEN_BUTTON_HEIGHT)
SCREEN_BUTTON_BREAD_LOCATION = (
    SCREEN_BUTTON_X + SCREEN_BUTTON_WIDTH + SCREEN_BUTTON_OFFSET, SCREEN_BUTTON_Y, SCREEN_BUTTON_WIDTH,
    SCREEN_BUTTON_HEIGHT)
SCREEN_BUTTON_COOKING_LOCATION = (
    SCREEN_BUTTON_X + 2 * (SCREEN_BUTTON_WIDTH + SCREEN_BUTTON_OFFSET), SCREEN_BUTTON_Y, SCREEN_BUTTON_WIDTH,
    SCREEN_BUTTON_HEIGHT)
SCREEN_BUTTON_TOPPING_LOCATION = (
    SCREEN_BUTTON_X + 3 * (SCREEN_BUTTON_WIDTH + SCREEN_BUTTON_OFFSET), SCREEN_BUTTON_Y, SCREEN_BUTTON_WIDTH,
    SCREEN_BUTTON_HEIGHT)
## The exit and settings buttons
SCREEN_BUTTON_SPECIAL_OFFSET = 22
SCREEN_BUTTON_SPECIAL_X = 1708
SCREEN_BUTTON_SPECIAL_Y = 972
SCREEN_BUTTON_SPECIAL_WIDTH = 1781 - SCREEN_BUTTON_SPECIAL_X
SCREEN_BUTTON_SPECIAL_HEIGHT = 1043 - SCREEN_BUTTON_SPECIAL_Y
SCREEN_BUTTON_SETTINGS = (
    SCREEN_BUTTON_SPECIAL_X, SCREEN_BUTTON_SPECIAL_Y, SCREEN_BUTTON_SPECIAL_WIDTH, SCREEN_BUTTON_SPECIAL_HEIGHT)
SCREEN_BUTTON_EXIT = (
    SCREEN_BUTTON_SPECIAL_X + SCREEN_BUTTON_SPECIAL_WIDTH + SCREEN_BUTTON_SPECIAL_OFFSET, SCREEN_BUTTON_SPECIAL_Y,
    SCREEN_BUTTON_SPECIAL_WIDTH, SCREEN_BUTTON_SPECIAL_HEIGHT)

# Queue stage locations
TAKE_ORDER_COORDINATES = (380, 420)
TAKE_ORDER_SIZE = (160, 150)
TAKE_ORDER_BUTTON_LOCATION = (400, 450, 120, 60)
TAKE_AWAY_QUEUE_X_LOCATION = 340
TAKE_AWAY_QUEUE_Y_LOCATION = 432
QUEUE_OFFSET = 250
NEW_CUSTOMERS_COOLDOWN = 10

# Order stage
ORDER_SIZE_BIG = (450, 600)
ORDER_SIZE = (225, 300)
ORDER_POS_BIG = (1450, 10)
ORDER_POS = (1675, 10)
TEXT_BOX_SIZE = (300, 280)
TEXT_BOX_COORDINATES = (400, 80)

# Topping station
LEFT_TOPPINGS_X_POS = 275
RIGHT_TOPPINGS_X_POS = 1330
TOPPINGS_Y_POS = 470
TOPPINGS_OFFSET = 80
TOPPING_BOX_WIDTH = 240
TOPPING_BOX_HEIGHT = 95
CHECKMARK_POSITION = (1650, 25)
CHECKMARK_SIZE = (200, 200)

# Spoon
SPOON_WIDTH = 220
SPOON_HEIGHT = 44

# Topping
TOPPING_WIDTH = 55
TOPPING_HEIGHT = 40
TOPPING_SPEECH_BOX_SIZE = (224, 149)

# Order coordinates
ORDER_LOCATION_BIG = (1452, 483)
ORDER_LAFFA_SIZE_BIG = (1897 - ORDER_LOCATION_BIG[0], 607 - ORDER_LOCATION_BIG[1])  # Basically the size of the entire big order screen
ORDER_ROW_OFFSET_BIG = ORDER_LAFFA_SIZE_BIG[1] * 0.25
ORDER_INGREDIENT_WIDTH_BIG = ORDER_LOCATION_BIG[0] + int(ORDER_LAFFA_SIZE_BIG[0] * 2 / 3)
ORDER_INGREDIENT_SIZE_BIG = (1897 - ORDER_INGREDIENT_WIDTH_BIG, 607 - ORDER_LOCATION_BIG[1] - ORDER_ROW_OFFSET_BIG * 2)

ORDER_LOCATION = (1676, 246)
ORDER_LAFFA_SIZE = (1899 - ORDER_LOCATION[0], 309 - ORDER_LOCATION[1])
ORDER_ROW_OFFSET = ORDER_LAFFA_SIZE[1] * 0.25
ORDER_INGREDIENT_WIDTH = ORDER_LOCATION[0] + int(ORDER_LAFFA_SIZE[0] * 2 / 3)
ORDER_INGREDIENT_SIZE = (1899 - ORDER_INGREDIENT_WIDTH, 309 - ORDER_LOCATION[1] - ORDER_ROW_OFFSET * 2)

# Lafa on table
SHAWARMA_SPEECH_BOX_SIZE = (224, 149)
SHAWARMA_SIZE = (300, 250)
LAFFA_X_POS = 650
LAFFA_Y_POS = 500
TOPPINGS_ABOVE_LAFFA_OFFSET = 60

# Customers - size
CUSTOMER_QUEUE_SIZE = (240, 240)
CUSTOMER_ORDER_SIZE = (397, 397)

# Customers - coordinates
CUSTOMER_START_PATH_QUEUE = (1885, 620)
CUSTOMER_END_PATH_QUEUE = (335, 620)
CUSTOMER_SPEED = -10
CUSTOMER_POSITION_ORDER = (550, 265)

# Customers - settings
CUSTOMER_TYPES = ("Bob", "Jack", "Lucy", "Troll")
CUSTOMER_MIN_CRITICISM = 1
CUSTOMER_MAX_CRITICISM = 5
CUSTOMER_MIN_WAIT_TIME = 60
CUSTOMER_MAX_WAIT_TIME = 120

# Bread stage
SHAWARMA_BREAD_STAGE_POSITION = (640, 446)

# Cooking stage
PRESENTING_MEAT_SIZE = (400, 400)
MEAT_SIZE = (450, 450)

# Take order stage
SHAWARMA_TAKE_ORDER_STAGE_POSITION = (200, 600)
MAX_DIFFERENCE_BETWEEN_ORDER_AND_RESULT_TOPPINGS_COUNT = 10

