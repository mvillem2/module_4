from pizza import *
from order import *

def main():
    orderID = 1
    customerID = 1

    Order1 = Order("3/19/2024 13:23:32", customerID, orderID)
    Pizza1 = Pizza("Thin",["Pesto"], "Mozzerella", ["Mushrooms"])
    Pizza2 = Pizza("Thick",["Marinara"], "Mozzerella", ["Mushrooms"])
    Order1.input_pizza(Pizza1)
    Order1.input_pizza(Pizza2)
    Order1.order_paid()
    print(Order1)

    orderID = 2
    customerID = 2

    Order2 = Order("3/19/2024 13:23:32", customerID, orderID)
    Pizza1 = Pizza("Gluten Free",["Marinara"], "Mozzerella", ["Pineapple"])
    Pizza2 = Pizza("Thin",["Pesto","Liv Sauce"], "Mozzerella", ["Pepperoni","Mushrooms"])
    Order2.input_pizza(Pizza1)
    Order2.input_pizza(Pizza2)
    Order2.order_paid()
    print(Order2)

if __name__ == '__main__':
    main()