from settings import *
from surfaces import *
from classes.Ingredient import Ingredient
from classes.Meat import Meat


class Order:
    def __init__(self, laffa, meat: Meat = Meat(0), ingredient_list=[]):
        self.laffa = laffa
        self.meat = meat
        self.toppings = []
        for i in ingredient_list:
            self.toppings.append(Ingredient(i.name, i.on_laffa_x_pos, i.on_laffa_y_pos))

    def add_topping(self, topping):
        self.toppings.append(Ingredient(topping.name, topping.on_laffa_x_pos, topping.on_laffa_y_pos))

    def add_meat(self):
        self.meat.add_meat()

    def show_like_order(self, steps, order_size):
        order_image = pygame.transform.scale(pygame.image.load("images/other/order.png"), order_size)
        if order_size == ORDER_SIZE_BIG:
            screen.blit(order_image, ORDER_POS_BIG)
            screen.blit(laffas_order_images_big[self.get_laffa()], ORDER_LOCATION_BIG)
        else:
            screen.blit(order_image, ORDER_POS)
            screen.blit(laffas_order_images[self.get_laffa()], ORDER_LOCATION)
        order_ingredient_locations = []
        for step in range(0, steps):
            if steps >= 1 and self.has_meat():
                if order_size == ORDER_SIZE_BIG:
                    screen.blit(meat_to_present_in_order_big["meat"], (
                    ORDER_LOCATION_BIG[0] + ORDER_INGREDIENT_SIZE_BIG[0],
                    ORDER_LOCATION_BIG[1] - ORDER_ROW_OFFSET_BIG * 2))
                else:
                    screen.blit(meat_to_present_in_order["meat"], (
                    ORDER_LOCATION[0] + ORDER_INGREDIENT_SIZE[0], ORDER_LOCATION[1] - ORDER_ROW_OFFSET * 2))
            if step > 0:
                if order_size == ORDER_SIZE_BIG:
                    order_ingredient_location = (ORDER_LOCATION_BIG[0] + ORDER_INGREDIENT_SIZE_BIG[0],
                                                 ORDER_LOCATION_BIG[1] - (
                                                             ORDER_ROW_OFFSET_BIG * step * 2 + ORDER_ROW_OFFSET_BIG * 2))
                    order_ingredient_locations.append(order_ingredient_location)
                else:
                    order_ingredient_location = (ORDER_LOCATION[0] + ORDER_INGREDIENT_SIZE[0], ORDER_LOCATION[1] - (
                                ORDER_ROW_OFFSET * step * 2 + ORDER_ROW_OFFSET * 2))
                    order_ingredient_locations.append(order_ingredient_location)
        ingredient_num = 0
        for order_ingredient_location in order_ingredient_locations:
            if order_size == ORDER_SIZE_BIG:
                screen.blit(topping_order_images_big[self.get_ingredient_name(ingredient_num)],
                            order_ingredient_location)
                ingredient_num += 1
            else:
                screen.blit(topping_order_images[self.get_ingredient_name(ingredient_num)], order_ingredient_location)
                ingredient_num += 1

    def show_like_shawarma(self, shawarma_position, size="medium"):
        if self.meat.get_count() == 0:
            if size == "small":
                screen.blit(laffas_speech_box_images[self.laffa], shawarma_position)
            else:
                screen.blit(laffas_images[self.laffa], shawarma_position)
        else:
            if size == "small":
                screen.blit(laffas_with_meat_small_images[self.laffa][self.meat.get_count() - 1], shawarma_position)
            else:
                screen.blit(laffas_with_meat_medium_images[self.laffa][self.meat.get_count() - 1], shawarma_position)
        for topping in self.toppings:
            topping.show(shawarma_position, size)

    def get_ingredient_name(self, number):
        return self.toppings[number].name

    def get_toppings_count(self):
        return len(self.toppings)

    def get_laffa(self):
        return self.laffa

    def has_meat(self):
        return self.meat.get_count() != 0

    def get_meat_count(self):
        return self.meat.get_count()

    def compare(self, my_shawarma):
        """
        Future function compares THIS imagination shawarma and shawarma the user did

        :param my_shawarma:
        :return: percent 0 to 100
        """
        pass
