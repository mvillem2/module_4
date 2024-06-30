"""test_pizza - Unit tests for pizza.py"""

from pizza import *

@pytest.fixture()
def example_pizza():
    """
    example_pizza - Reference Pizza for class testing
    """
    Pizza1 = Pizza("Thin",["Marinara","Pesto","Liv Sauce"], "Mozzerella", ["Pineapple","Pepperoni","Mushrooms"])
    return Pizza1

def test_pizza_init(example_pizza):
    """
    test_pizza_init - Ensures Pizza constructor works as intended
    
    :param example_pizza: Sample pizza used for tesing
    :type example_pizza: Pizza
    """
    Pizza1 = example_pizza
    checkCrust = False
    if (Pizza1.crust == "Thin"):
        checkCrust = True
    print("Crust?: " + str(checkCrust))
    checkSauces = False
    if (Pizza1.sauces == ["Marinara","Pesto","Liv Sauce"]):
        checkSauces = True
    print("Sauces?: " + str(checkSauces))
    checkCheese = False
    if (Pizza1.cheese == "Mozzerella"):
        checkCheese = True
    print("Cheese?: " + str(checkCheese))     
    checkToppings = False
    if (Pizza1.toppings == ["Pineapple","Pepperoni","Mushrooms"]):
        checkToppings = True      
    print("Toppings?: " + str(checkToppings)) 
    assert checkCrust and checkSauces and checkCheese and checkToppings

def test_pizza_str(example_pizza):
    """
    test_pizza_str - Ensures string representation of pizza class works as intended
   
    :param example_pizza: Sample pizza used for tesing
    :type example_pizza: Pizza
    """
    Pizza1 = example_pizza
    print(Pizza1)
    pizza_str = "Crust: Thin, Sauces: Marinara, Pesto, Liv Sauce, , Toppings: Pineapple, Pepperoni, Mushrooms, "
    print(pizza_str)
    assert str(Pizza1) == pizza_str