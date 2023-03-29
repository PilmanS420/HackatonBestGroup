from settings import *

take_order_dialog_window = pygame.transform.scale(pygame.image.load("images/other/take_order_dialog_window.png"), TAKE_ORDER_SIZE)
empty_text_box = pygame.transform.scale(pygame.image.load("images/other/text_box.png"), TEXT_BOX_SIZE)

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
bob_customer_images = {
    "queue": [pygame.transform.scale(pygame.image.load("images/customers/bob/bob_hihihi.png"), CUSTOMER_QUEUE_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/bob/bob_nice.png"), CUSTOMER_QUEUE_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/bob/bob_choose.png"), CUSTOMER_QUEUE_SIZE)],
    "order": [pygame.transform.scale(pygame.image.load("images/customers/bob/bob_choose.png"), CUSTOMER_ORDER_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/bob/bob_laught.png"), CUSTOMER_ORDER_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/bob/bob_nice.png"), CUSTOMER_ORDER_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/bob/bob_talks.png"), CUSTOMER_ORDER_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/bob/bob_hihihi.png"), CUSTOMER_ORDER_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/bob/bob_thinks.png"), CUSTOMER_ORDER_SIZE)],
    "think": [pygame.transform.scale(pygame.image.load("images/customers/bob/bob_thinks.png"), CUSTOMER_ORDER_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/bob/bob_choose.png"), CUSTOMER_ORDER_SIZE)],
    "reaction": {
        "worst": [pygame.transform.scale(pygame.image.load("images/customers/bob/bob_angry.png"), CUSTOMER_ORDER_SIZE),
                  pygame.transform.scale(pygame.image.load("images/customers/bob/bob_furious.png"), CUSTOMER_ORDER_SIZE)],
        "bad": [pygame.transform.scale(pygame.image.load("images/customers/bob/bob_upset.png"), CUSTOMER_ORDER_SIZE)],
        "normal": [pygame.transform.scale(pygame.image.load("images/customers/bob/bob_no.png"), CUSTOMER_ORDER_SIZE)],
        "good": [pygame.transform.scale(pygame.image.load("images/customers/bob/bob_nice.png"), CUSTOMER_ORDER_SIZE),
                 pygame.transform.scale(pygame.image.load("images/customers/bob/bob_hihihi.png"), CUSTOMER_ORDER_SIZE)],
        "best": [pygame.transform.scale(pygame.image.load("images/customers/bob/bob_laught.png"), CUSTOMER_ORDER_SIZE)]
    }
}
jack_customer_images = {
    "queue": [pygame.transform.scale(pygame.image.load("images/customers/jack/jack_nice.png"), CUSTOMER_QUEUE_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/jack/jack_trolling.png"), CUSTOMER_QUEUE_SIZE)],
    "order": [pygame.transform.scale(pygame.image.load("images/customers/jack/jack_serious.png"), CUSTOMER_ORDER_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/jack/jack_trolling.png"), CUSTOMER_ORDER_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/jack/jack_nice.png"), CUSTOMER_ORDER_SIZE)],
    "think": [pygame.transform.scale(pygame.image.load("images/customers/jack/jack_no.png"), CUSTOMER_ORDER_SIZE)],
    "reaction": {
        "worst": [pygame.transform.scale(pygame.image.load("images/customers/jack/jack_angry.png"), CUSTOMER_ORDER_SIZE)],
        "bad": [pygame.transform.scale(pygame.image.load("images/customers/jack/jack_serious.png"), CUSTOMER_ORDER_SIZE)],
        "normal": [pygame.transform.scale(pygame.image.load("images/customers/jack/jack_sad.png"), CUSTOMER_ORDER_SIZE),
                   pygame.transform.scale(pygame.image.load("images/customers/jack/jack_no.png"), CUSTOMER_ORDER_SIZE)],
        "good": [pygame.transform.scale(pygame.image.load("images/customers/jack/jack_nice.png"), CUSTOMER_ORDER_SIZE)],
        "best": [pygame.transform.scale(pygame.image.load("images/customers/jack/jack_perfect.png"), CUSTOMER_ORDER_SIZE)]
    }
}
lucy_customer_images = {
    "queue": [pygame.transform.scale(pygame.image.load("images/customers/lucy/lucy_hihihi.png"), CUSTOMER_QUEUE_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/lucy/lucy_cute.png"), CUSTOMER_QUEUE_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/lucy/lucy_fool.png"), CUSTOMER_QUEUE_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/lucy/lucy_choose.png"), CUSTOMER_QUEUE_SIZE)],
    "order": [pygame.transform.scale(pygame.image.load("images/customers/lucy/lucy_choose.png"), CUSTOMER_ORDER_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/lucy/lucy_cute.png"), CUSTOMER_ORDER_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/lucy/lucy_fool.png"), CUSTOMER_ORDER_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/lucy/lucy_hihihi.png"), CUSTOMER_ORDER_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/lucy/lucy_talk.png"), CUSTOMER_ORDER_SIZE)],
    "think": [pygame.transform.scale(pygame.image.load("images/customers/lucy/lucy_choose.png"), CUSTOMER_ORDER_SIZE)],
    "reaction": {
        "worst": [pygame.transform.scale(pygame.image.load("images/customers/lucy/lucy_angry.png"), CUSTOMER_ORDER_SIZE)],
        "bad": [pygame.transform.scale(pygame.image.load("images/customers/lucy/lucy_serious.png"), CUSTOMER_ORDER_SIZE)],
        "normal": [pygame.transform.scale(pygame.image.load("images/customers/lucy/lucy_what.png"), CUSTOMER_ORDER_SIZE)],
        "good": [pygame.transform.scale(pygame.image.load("images/customers/lucy/lucy_fool.png"), CUSTOMER_ORDER_SIZE),
                 pygame.transform.scale(pygame.image.load("images/customers/lucy/lucy_choose.png"), CUSTOMER_ORDER_SIZE)],
        "best": [pygame.transform.scale(pygame.image.load("images/customers/lucy/lucy_cute.png"), CUSTOMER_ORDER_SIZE)]
    }
}
trollface_customer_images = {
    "queue": [pygame.transform.scale(pygame.image.load("images/customers/troll/trollface.png"), CUSTOMER_QUEUE_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/troll/troll_fool.png"), CUSTOMER_QUEUE_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/troll/troll_not_trollface.png"), CUSTOMER_QUEUE_SIZE)],
    "order": [pygame.transform.scale(pygame.image.load("images/customers/troll/troll_not_trollface.png"), CUSTOMER_ORDER_SIZE),
              pygame.transform.scale(pygame.image.load("images/customers/troll/trollface.png"), CUSTOMER_ORDER_SIZE)],
    "think": [pygame.transform.scale(pygame.image.load("images/customers/troll/troll_normal.png"), CUSTOMER_ORDER_SIZE)],
    "reaction": {
        "worst": [pygame.transform.scale(pygame.image.load("images/customers/troll/troll_very_sad.png"), CUSTOMER_ORDER_SIZE)],
        "bad": [pygame.transform.scale(pygame.image.load("images/customers/troll/troll_sad.png"), CUSTOMER_ORDER_SIZE)],
        "normal": [pygame.transform.scale(pygame.image.load("images/customers/troll/troll_normal.png"), CUSTOMER_ORDER_SIZE)],
        "good": [pygame.transform.scale(pygame.image.load("images/customers/troll/troll_not_trollface.png"), CUSTOMER_ORDER_SIZE)],
        "best": [pygame.transform.scale(pygame.image.load("images/customers/troll/troll_xd.png"), CUSTOMER_ORDER_SIZE)]
    }
}
meat_images = {}  # TODO: add meat images

checkmark_image = pygame.transform.scale(pygame.image.load("images/other/checkmark.png"), CHECKMARK_SIZE)
