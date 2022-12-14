"""
Program: mowingCustomer.py
Author: David Drummond

This module declares a class to define a customer's data.

"""

class Customer:
    """Class that sets the expected values for a customer record."""

    def __init__(self):
        self.first = input("What is the customer's first name?")
        self.last = input("What is the customer's last name?")
        self.streetNumber = input("What is the customer's street number?")
        self.streetName = input("What street does the customer live on?")
        self.city = input("What city does the customer live in?")
        self.stateID = input("What state does the customer live in?  Enter the 2 character postal code (IN:Indiana) ?")
        self.zipCode = input("What is the customer's zipcode?")
        self.timePreference = int(input("What time does the customer prefer service? 1:Morning, 2:Afternoon, 3:Evening"))
        self.weekdayPreference = input("Enter a day of the week for service. S, M, T, W, TH, F, Sa")
        self.customerNumber = 1

    def __str__(self):
        """This creates a function that puts the entire record in a string."""

        return ('{} {} {} {} {} {} {} {} {}'.format(self.first, self.last, self.streetNumber, self.streetName, self.city, self.stateID, self.zipCode, self.timePreference, self.weekdayPreference))

# cust1 = Customer()
# cust2 = Customer()

# print(cust1.createdRecord())
# print(cust2.createdRecord())


