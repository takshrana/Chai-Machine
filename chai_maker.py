class ChaiMaker:

    def __init__(self):
        self.resources = {
            "sugar": 300,
            "milk": 200,
            "chai": 100,
        }

    def report(self):

        print(f"Sugar: {self.resources['sugar']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Chai: {self.resources['chai']}g")

    def is_resource_sufficient(self, drink):

        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item} to make the Chai.")
                can_make = False
        return can_make

    def make_chai(self, order):

        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Enjoy your {order.name} ☕!")
