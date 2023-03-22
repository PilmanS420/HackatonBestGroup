from helpers import *

spoon_images = {
    "harif": pygame.transform.scale(pygame.image.load("images/spoons_with_ingredients/spoon_harif.png"), (SPOON_WIDTH, SPOON_HEIGHT)),
    "humus": pygame.transform.scale(pygame.image.load("images/spoons_with_ingredients/spoon_humus.png"), (SPOON_WIDTH, SPOON_HEIGHT)),
    "cucumber": pygame.transform.scale(pygame.image.load("images/spoons_with_ingredients/spoon_cucumber.png"),
                                       (160, 25)),
    "thina": pygame.transform.scale(pygame.image.load("images/spoons_with_ingredients/spoon_thina.png"), (SPOON_WIDTH, SPOON_HEIGHT)),
    "salat": pygame.transform.scale(pygame.image.load("images/spoons_with_ingredients/spoon_salat.png"), (SPOON_WIDTH, SPOON_HEIGHT)),
    "onion": pygame.transform.scale(pygame.image.load("images/spoons_with_ingredients/spoon_onion.png"), (SPOON_WIDTH, SPOON_HEIGHT))}

topping_images = {
    "harif": pygame.transform.scale(pygame.image.load("images/ingredients/harif.png"), (TOPPING_WIDTH, TOPPING_HEIGHT)),
    "humus": pygame.transform.scale(pygame.image.load("images/ingredients/humus.png"), (TOPPING_WIDTH, TOPPING_HEIGHT)),
    "cucumber": pygame.transform.scale(pygame.image.load("images/ingredients/cucumber.png"), (TOPPING_WIDTH, TOPPING_HEIGHT)),
    "thina": pygame.transform.scale(pygame.image.load("images/ingredients/thina.png"), (TOPPING_WIDTH, TOPPING_HEIGHT)),
    "salat": pygame.transform.scale(pygame.image.load("images/ingredients/salat.png"), (TOPPING_WIDTH, TOPPING_HEIGHT)),
    "onion": pygame.transform.scale(pygame.image.load("images/ingredients/onion.png"), (TOPPING_WIDTH, TOPPING_HEIGHT))
}
