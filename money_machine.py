class MoneyMachine:

    CURRENCY = "₹"

    COIN_VALUES = {
        "ten": 10,
        "twenty": 20,
        "fifty": 50,
        "hundred": 100
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):

        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):

        print("Please insert money.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):

        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is your {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry money is not enough. Money refunded.")
            self.money_received = 0
            return False
        
