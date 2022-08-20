class MenuItem:

    def __init__(self, name, sugar, milk, chai, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "sugar": sugar,
            "milk": milk,
            "chai": chai
        }


class Menu:

    def __init__(self):
        self.menu = [
            MenuItem(name="black tea", sugar=200, milk=150, chai=24, cost=270),
            MenuItem(name="green tea", sugar=50, milk=0, chai=18, cost=125),
            MenuItem(name="herbal tea", sugar=250, milk=50, chai=24, cost=192),
        ]

    def get_items(self):

        options = ""
        for item in self.menu:
            options += f"{item.name} / {item.cost}₹ | "
        return options

    def find_drink(self, order_name):

        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
