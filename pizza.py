import pytest

class Pizza:
    """Pizza module"""
    def __init__(self,crust,sauces,cheese,toppings):
        """__init__ - Constructor for Pizzs class
            
            :param self: self Handle for object
            :type self: Pizza
            :param sauces: List of Sauces as list of strings
            :type sauces: list
            :param cheese: Type of cheese used
            :type cheese: str
            :param toppings: List of Toppings as list of strings
            :type toppings: list
            :return: Pizza object
            :rtype: Pizza
        """
        self.crust = crust
        self.sauces = sauces
        self.cheese = cheese
        self.toppings = toppings
        self.cost = 0

    def __str__(self):
        """
        __str__ - Defines string representation of Pizza class
        
        :param self: self Handle for object
        :type self: Pizza
        :return: String of Pizza object
        :rtype: str
        """
        sauces_str = ""
        toppings_str = ""
        for sauce in self.sauces:
             sauces_str = sauces_str + sauce + ", "
        for topping in self.toppings:
             toppings_str = toppings_str + topping + ", "
        str1 = f"Crust: {self.crust}\nSauces: {sauces_str}\nToppings: {toppings_str}"
        str2 = f"Crust: {self.crust}, Sauces: {sauces_str}, Toppings: {toppings_str}"
        return str2

    def crustCost(self):
        """
        crustCost - Returns the cost of the selected crust
                
        :param self: self Handle for object
        :type self: Pizza
        :return: Cost of crust
        :rtype: int
        """
        cost = 0
        if (self.crust == "Thin"):
            cost = 5
        elif (self.crust == "Thick"):
            cost = 6
        elif (self.crust == "Gluten Free"):
            cost = 8
        else:
             assert "Crust Type not found, please double check entry"
        return cost
             
    def sauceCost(self):
        """
        sauceCost - Returns the cost of the selected sauces
                
        :param self: self Handle for object
        :type self: Pizza
        :return: Cost of sauces
        :rtype: int
        """
        cost = 0
        for sauce in self.sauces:
            if (sauce == "Marinara"):
                cost = cost + 2
            elif (sauce == "Pesto"):
                cost = cost + 3
            elif (sauce == "Liv Sauce"):
                cost = cost + 5
            else:
                assert "Sauce Type not found, please double check entry"
        return cost

    def toppingCost(self):
        """
        topppingCost - Returns the cost of the selected toppings   

        :param self: self Handle for object
        :type self: Pizza
        :return: Cost of toppings
        :rtype: int
        """
        cost = 0
        for topping in self.toppings:
            if (topping == "Pineapple"):
                cost = cost + 1
            elif (topping == "Pepperoni"):
                cost = cost + 2
            elif (topping == "Mushrooms"):
                cost = cost + 3
            else:
                assert "Topping Type not found, please double check entry"
        return cost

    def pizzaCost(self):
        """
        pizzaCost - Returns the cost of the pizza given the selected configuration

        :param self: self Handle for object
        :type self: Pizza
        :return: Cost of pizza
        :rtype: int
        """
        cost = self.crustCost() + self.sauceCost() + self.toppingCost()
        self.pizzaCost = cost
        return cost
        