"""test_order - Unit tests for order.py"""

from order import *
from pizza import *
import pytest 

@pytest.fixture
def example_order():
    """
    example_order - Reference order for testing

    :return: Sample order
    :rtype: Order
    """
    orderID = 1
    customerID = 1

    Order1 = Order("3/19/2024 13:23:32", customerID, orderID)
    Pizza1 = Pizza("Thin",["Pesto"], "Mozzerella", ["Mushrooms"])
    Pizza2 = Pizza("Thick",["Marinara"], "Mozzerella", ["Mushrooms"])
    Order1.input_pizza(Pizza1)
    Order1.input_pizza(Pizza2)
    Order1.order_paid()
    print(Order1)

    return Order1

def test_order_init():
    """
    test_order_init - Tests to ensure constructor for Order class works

    :return: N/A
    :rtype: Null
    :raises AssertionError: Initializing order did not work 
    """
    orderID = 1
    customerID = 1
    Order1 = Order("3/19/2024 13:23:32", customerID, orderID)
    checkEmpty = False
    checkZeroCost = False
    checkNotPaid = False
    print(Order1.orderPaid)
    if (Order1.orderPaid == False):
        checkNotPaid = True
    if (len(Order1.pizzaOrder) == 0):
        checkEmpty = True
    if (Order1.orderCost == 0):
        checkZeroCost = True   
    print(checkEmpty)
    print(checkZeroCost)
    print(checkNotPaid)
    assert checkNotPaid and checkEmpty and checkZeroCost

def test_order_str(example_order):
    """
    test_order_str - Tests to ensure string representation of Order class is working

    :param example_order: Example order used for testing
    :type example_order: Order
    :return: N/A
    :rtype: Null
    :raises AssertionError: Inputing pizza did not work
    """
    Order1 = example_order
    Order1str = """Order ID: 1, Customer ID: 1, Order Date / Time: 3/19/2024 13:23:32, Pizza Order: Pizza 1: Crust: Thin, Sauces: Pesto, , Toppings: Mushrooms, ,Pizza 2: Crust: Thick, Sauces: Marinara, , Toppings: Mushrooms, ,, Order Cost: $22.00, Order Paid?: True"""
    assert Order1str == str(Order1)

def test_input_pizza(example_order):
    """
    test_input_pizza - Tests that input_pizza works accordingly

    :param example_order: Example order used for testing
    :type example_order: Order
    :return: N/A
    :rtype: Null
    :raises AssertionError: Inputing pizza did not work
    """
    Order1 = example_order
    pizzaStrs = ["Crust: Thin, Sauces: Pesto, , Toppings: Mushrooms,","Crust: Thick, Sauces: Marinara, , Toppings: Mushrooms,"]
    i = 0
    for pizza in Order1.pizzaOrder:
        currentPizza = pizzaStrs[i]
        print("Pizza List")
        print(currentPizza)
        print("Pizza Check")
        print(str(pizza))
        if str(pizza).strip() == currentPizza.strip():
            pizzeCheckInput = True
        else:
            pizzeCheckInput = False
            break
        i = i + 1
    assert pizzeCheckInput

def test_order_paid(example_order):
    """
    test_order_paid - Ensures that order_paid function works as intended
    
    :param example_order: Example order used for testing
    :type example_order: Order
    """
    Order1 = example_order
    assert Order1.order_paid()


