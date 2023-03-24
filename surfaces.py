from helpers import *

spoon_images = {
    "harif": pygame.transform.scale(pygame.image.load("images/spoons_with_ingredients/spoon_harif.png"), (SPOON_WIDTH, SPOON_HEIGHT)),
    "humus": pygame.transform.scale(pygame.image.load("images/spoons_with_ingredients/spoon_humus.png"), (SPOON_WIDTH, SPOON_HEIGHT)),
    "cucumber": pygame.transform.scale(pygame.image.load("images/spoons_with_ingredients/spoon_cucumber.png"),
                                       (SPOON_WIDTH, SPOON_HEIGHT)),
    "thina": pygame.transform.scale(pygame.image.load("images/spoons_with_ingredients/spoon_thina.png"), (SPOON_WIDTH, SPOON_HEIGHT)),
    "salat": pygame.transform.scale(pygame.image.load("images/spoons_with_ingredients/spoon_salat.png"), (SPOON_WIDTH, SPOON_HEIGHT)),
    "onion": pygame.transform.scale(pygame.image.load("images/spoons_with_ingredients/spoon_onion.png"), (SPOON_WIDTH, SPOON_HEIGHT)),
    "none": pygame.transform.scale(pygame.image.load("images/spoons_with_ingredients/spoon.png"), (SPOON_WIDTH, SPOON_HEIGHT))
}
rotated_spoon_images = {}
for spoon in spoon_images:
    rotated_spoon_images[spoon] = pygame.transform.rotozoom(spoon_images[spoon], 30, 1)

topping_images = {
    "harif": pygame.transform.scale(pygame.image.load("images/ingredients/harif.png"), (TOPPING_WIDTH, TOPPING_HEIGHT)),
    "humus": pygame.transform.scale(pygame.image.load("images/ingredients/humus.png"), (TOPPING_WIDTH, TOPPING_HEIGHT)),
    "cucumber": pygame.transform.scale(pygame.image.load("images/ingredients/cucumber.png"), (TOPPING_WIDTH, TOPPING_HEIGHT)),
    "thina": pygame.transform.scale(pygame.image.load("images/ingredients/thina.png"), (TOPPING_WIDTH, TOPPING_HEIGHT)),
    "salat": pygame.transform.scale(pygame.image.load("images/ingredients/salat.png"), (TOPPING_WIDTH, TOPPING_HEIGHT)),
    "onion": pygame.transform.scale(pygame.image.load("images/ingredients/onion.png"), (TOPPING_WIDTH, TOPPING_HEIGHT))
}
laffas_images = {
    "Type 1": pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_1.png"), (LAFFA_WIDTH, LAFFA_HEIGHT)),
    "Type 2": pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_2.png"), (LAFFA_WIDTH, LAFFA_HEIGHT)),
    "Type 3": pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_3.png"), (LAFFA_WIDTH, LAFFA_HEIGHT)),
}
screen_buttons_image = pygame.transform.scale(pygame.image.load("images/background_images/screen_buttons.png"),
                                              (WINDOW_WIDTH, WINDOW_HEIGHT))

# Customers
bob_customer = {"come": []}
