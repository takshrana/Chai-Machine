from menu import Menu
from chai_maker import ChaiMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
chai_maker = ChaiMaker()
menu = Menu()

is_on = True
print('''
                        .
                        `:.
                          `:.
                  .:'     ,::
                 .:'      ;:'
                 ::      ;:'
                  :    .:'
                   `.  :.
          _________________________
         : _ _ _ _ _ _ _ _ _ _ _ _ :
     ,---:".".".".".".".".".".".".":
    : ,'"`::.:.:.:.:.:.:.:.:.:.:.::'
    `.`.  `:-===-===-===-===-===-:'
      `.`-._:                   :
        `-.__`.               ,'
    ,--------`"`-------------'--------.
     `"--.__                   __.--"'
            `""-------------""'
            ''')
while is_on:
    options = menu.get_items()
    choice = input(f"Which Tea would you like? ( {options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        chai_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = chai_maker.is_resource_sufficient(drink)
        if not is_enough_ingredients:
            continue
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            chai_maker.make_chai(drink)

k = input("")