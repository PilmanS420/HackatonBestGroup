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
topping_speech_box_images = {
    "harif": pygame.transform.scale(pygame.image.load("images/ingredients/harif.png"), TOPPING_SPEECH_BOX_SIZE),
    "humus": pygame.transform.scale(pygame.image.load("images/ingredients/humus.png"), TOPPING_SPEECH_BOX_SIZE),
    "cucumber": pygame.transform.scale(pygame.image.load("images/ingredients/cucumber.png"), TOPPING_SPEECH_BOX_SIZE),
    "thina": pygame.transform.scale(pygame.image.load("images/ingredients/thina.png"), TOPPING_SPEECH_BOX_SIZE),
    "salat": pygame.transform.scale(pygame.image.load("images/ingredients/salat.png"), TOPPING_SPEECH_BOX_SIZE),
    "onion": pygame.transform.scale(pygame.image.load("images/ingredients/onion.png"), TOPPING_SPEECH_BOX_SIZE)
}
meat_to_present_in_speech = {
    "meat": pygame.transform.scale(pygame.image.load("images/ingredients/meat_to_present_in_order.png"), TOPPING_SPEECH_BOX_SIZE)
}
topping_order_images_big = {
    "harif": pygame.transform.scale(pygame.image.load("images/ingredients/harif.png"), ORDER_INGREDIENT_SIZE_BIG),
    "humus": pygame.transform.scale(pygame.image.load("images/ingredients/humus.png"), ORDER_INGREDIENT_SIZE_BIG),
    "cucumber": pygame.transform.scale(pygame.image.load("images/ingredients/cucumber.png"), ORDER_INGREDIENT_SIZE_BIG),
    "thina": pygame.transform.scale(pygame.image.load("images/ingredients/thina.png"), ORDER_INGREDIENT_SIZE_BIG),
    "salat": pygame.transform.scale(pygame.image.load("images/ingredients/salat.png"), ORDER_INGREDIENT_SIZE_BIG),
    "onion": pygame.transform.scale(pygame.image.load("images/ingredients/onion.png"), ORDER_INGREDIENT_SIZE_BIG)
}
topping_order_images = {
    "harif": pygame.transform.scale(pygame.image.load("images/ingredients/harif.png"), ORDER_INGREDIENT_SIZE),
    "humus": pygame.transform.scale(pygame.image.load("images/ingredients/humus.png"), ORDER_INGREDIENT_SIZE),
    "cucumber": pygame.transform.scale(pygame.image.load("images/ingredients/cucumber.png"), ORDER_INGREDIENT_SIZE),
    "thina": pygame.transform.scale(pygame.image.load("images/ingredients/thina.png"), ORDER_INGREDIENT_SIZE),
    "salat": pygame.transform.scale(pygame.image.load("images/ingredients/salat.png"), ORDER_INGREDIENT_SIZE),
    "onion": pygame.transform.scale(pygame.image.load("images/ingredients/onion.png"), ORDER_INGREDIENT_SIZE)
}
meat_to_present_in_order_big = {
    "meat": pygame.transform.scale(pygame.image.load("images/ingredients/meat_to_present_in_order.png"), ORDER_INGREDIENT_SIZE_BIG)
}
meat_to_present_in_order = {
    "meat": pygame.transform.scale(pygame.image.load("images/ingredients/meat_to_present_in_order.png"), ORDER_INGREDIENT_SIZE)
}
laffas_images = {
    "Type 1": pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_1.png"), SHAWARMA_MEDIUM_SIZE),
    "Type 2": pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_2.png"), SHAWARMA_MEDIUM_SIZE),
    "Type 3": pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_3.png"), SHAWARMA_MEDIUM_SIZE),
}
laffas_speech_box_images = {
    "Type 1": pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_1.png"), SHAWARMA_SPEECH_BOX_SIZE),
    "Type 2": pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_2.png"), SHAWARMA_SPEECH_BOX_SIZE),
    "Type 3": pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_3.png"), SHAWARMA_SPEECH_BOX_SIZE),
}
laffas_order_images_big = {
    "Type 1": pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_1.png"), ORDER_LAFFA_SIZE_BIG),
    "Type 2": pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_2.png"), ORDER_LAFFA_SIZE_BIG),
    "Type 3": pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_3.png"), ORDER_LAFFA_SIZE_BIG),
}
laffas_order_images = {
    "Type 1": pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_1.png"), ORDER_LAFFA_SIZE),
    "Type 2": pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_2.png"), ORDER_LAFFA_SIZE),
    "Type 3": pygame.transform.scale(pygame.image.load("images/laffas/laffa_cutted_3.png"), ORDER_LAFFA_SIZE),
}
laffas_with_meat_medium_images = {
    "Type 1": [
        pygame.transform.scale(pygame.image.load("images/laffas/laffa_1_p1.png"), SHAWARMA_MEDIUM_SIZE),
        pygame.transform.scale(pygame.image.load("images/laffas/laffa_1_p2.png"), SHAWARMA_MEDIUM_SIZE),
        pygame.transform.scale(pygame.image.load("images/laffas/laffa_1_p3.png"), SHAWARMA_MEDIUM_SIZE)],
    "Type 2": [
        pygame.transform.scale(pygame.image.load("images/laffas/laffa_2_p1.png"), SHAWARMA_MEDIUM_SIZE),
        pygame.transform.scale(pygame.image.load("images/laffas/laffa_2_p2.png"), SHAWARMA_MEDIUM_SIZE),
        pygame.transform.scale(pygame.image.load("images/laffas/laffa_2_p3.png"), SHAWARMA_MEDIUM_SIZE)],
    "Type 3": [
        pygame.transform.scale(pygame.image.load("images/laffas/laffa_3_p1.png"), SHAWARMA_MEDIUM_SIZE),
        pygame.transform.scale(pygame.image.load("images/laffas/laffa_3_p2.png"), SHAWARMA_MEDIUM_SIZE),
        pygame.transform.scale(pygame.image.load("images/laffas/laffa_3_p3.png"), SHAWARMA_MEDIUM_SIZE)]
}

laffas_with_meat_small_images = {
    "Type 1": [
        pygame.transform.scale(pygame.image.load("images/laffas/laffa_1_p1.png"), SHAWARMA_MEDIUM_SIZE),
        pygame.transform.scale(pygame.image.load("images/laffas/laffa_1_p2.png"), SHAWARMA_MEDIUM_SIZE),
        pygame.transform.scale(pygame.image.load("images/laffas/laffa_1_p3.png"), SHAWARMA_MEDIUM_SIZE)],
    "Type 2": [
        pygame.transform.scale(pygame.image.load("images/laffas/laffa_2_p1.png"), SHAWARMA_MEDIUM_SIZE),
        pygame.transform.scale(pygame.image.load("images/laffas/laffa_2_p2.png"), SHAWARMA_MEDIUM_SIZE),
        pygame.transform.scale(pygame.image.load("images/laffas/laffa_2_p3.png"), SHAWARMA_MEDIUM_SIZE)],
    "Type 3": [
        pygame.transform.scale(pygame.image.load("images/laffas/laffa_3_p1.png"), SHAWARMA_MEDIUM_SIZE),
        pygame.transform.scale(pygame.image.load("images/laffas/laffa_3_p2.png"), SHAWARMA_MEDIUM_SIZE),
        pygame.transform.scale(pygame.image.load("images/laffas/laffa_3_p3.png"), SHAWARMA_MEDIUM_SIZE)]}

meat_1_image = pygame.transform.scale(pygame.image.load("images/meats/meat_1.png"),
                                          PRESENTING_MEAT_SIZE)
meat_images = {
    "raw": [
        pygame.transform.scale(pygame.image.load("images/meats/meat_1.png"), (450, 450)),
        pygame.transform.scale(pygame.image.load("images/meats/shwarma_1_p1.png"), (450, 450)),
        pygame.transform.scale(pygame.image.load("images/meats/shwarma_1_p2.png"), (450, 450)),
        pygame.transform.scale(pygame.image.load("images/meats/shwarma_1_p3.png"), (450, 450))],
    "medium": [
        pygame.transform.scale(pygame.image.load("images/meats/meat_2.png"), (450, 450)),
        pygame.transform.scale(pygame.image.load("images/meats/shwarma_2_p1.png"), (450, 450)),
        pygame.transform.scale(pygame.image.load("images/meats/shwarma_2_p2.png"), (450, 450)),
        pygame.transform.scale(pygame.image.load("images/meats/shwarma_2_p3.png"),(450, 450))],
    "well done": [
        pygame.transform.scale(pygame.image.load("images/meats/meat_3.png"), (450, 450)),
        pygame.transform.scale(pygame.image.load("images/meats/shwarma_3_p1.png"), (450, 450)),
        pygame.transform.scale(pygame.image.load("images/meats/shwarma_3_p2.png"), (450, 450)),
        pygame.transform.scale(pygame.image.load("images/meats/shwarma_3_p3.png"), (450, 450))]}

screen_buttons_image = pygame.transform.scale(pygame.image.load("images/background_images/screen_buttons.png"),
                                              (WINDOW_WIDTH, WINDOW_HEIGHT))
timer_border = pygame.image.load("images/other/timer_border.png")

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

checkmark_image = pygame.transform.scale(pygame.image.load("images/other/checkmark.png"), CHECKMARK_SIZE)

shawarma_closed = pygame.transform.scale(pygame.image.load("images/other/shawarma.png"), (210, 150))
