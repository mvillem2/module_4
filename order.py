from pizza import *
import pytest 

class Order:
    """Order module"""
    def __init__(self,dateTime,customerID,orderID):
        """
        __init__ - Order Class Constructor
        :param self: Handle for self in Order class
        :type self: Order
        :param dateTime: Date and Time upon placement of order
        :type dateTime: str
        :param customerID: ID of customer making purchase
        :type customerID: int
        :param orderID: ID of order
        :type orderID: int
        """
        self.customerID = customerID
        self.orderID = orderID
        self.pizzaOrder = []
        self.orderCost = 0
        self.orderPaid = False
        self.dateTime = dateTime

    def __str__(self):
        """
        __str__ - Defines string representation of order class

        :param self: Handle for self in Order class
        :type self: Order
        :return: N/A
        :rtype: Null        
        """
        pizzaStr = ""
        i = 1
        for pizza in self.pizzaOrder:
            pizzaStr = pizzaStr + "Pizza " + str(i) + ": " + str(pizza) + ","
            i = i + 1
        str1 = f"""\nOrder ID: {self.orderID}\nCustomer ID: {self.customerID}\nOrder Date / Time: {self.dateTime}\nPizza Order: {pizzaStr}\nOrder Cost: ${self.orderCost}.00\nOrder Paid?: {self.orderPaid}"""
        str2 = f"""Order ID: {self.orderID}, Customer ID: {self.customerID}, Order Date / Time: {self.dateTime}, Pizza Order: {pizzaStr}, Order Cost: ${self.orderCost}.00, Order Paid?: {self.orderPaid}"""
        print(str2)
        return str2

    def input_pizza(self, newPizza):
        """
        input_pizza - Inputs a Pizza class into the current order and updates the cost of the order

        :param self: Handle for self in Order class
        :type self: Order
        :param newPizza: New pizza that will be added to order
        :type newPizza: Pizza
        :return: N/A
        :rtype: Null        
        """        
        self.pizzaOrder.append(newPizza)
        self.orderCost = self.orderCost + newPizza.pizzaCost()

    def order_paid(self):
        """
        order_paid - Acknoledges payment from card vendor and returns Boolean value
        
        :param self: Handle for self in Order class
        :type self: Order
        :return: N/A
        :rtype: Null        
        """        
        self.orderPaid = True
        return True
