from settings import *
from surfaces import meat_images


class Meat:
    def __init__(self, count, roasting="medium"):
        self.roasting = roasting
        self.count = count

    def get_count(self):
        return self.count

    def get_roasting(self):
        return self.roasting

    def add_meat(self):
        self.count += 1
        if self.count > 3:
            self.count = 3
