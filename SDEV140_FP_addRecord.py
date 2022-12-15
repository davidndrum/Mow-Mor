"""

This module contains the code for adding a record to customers.pickle.

"""

from SDEV140_FP_customer import Customer
import pickle
import os

customerList = [] #Creates a list to hold current customer data.
addCustomerList = [] #Creates a list to hold data for customers to be added.
newRecord = True


def addRecord():
    """Adds a function to add a record."""

    if os.path.exists("customers.pickle") is not True:  # This checks whether the file exists.
        """ If it does not exist, it creates the file and adds
        nothing to it so that it is not empty."""

        f = open("customers.pickle", "wb")
        pickle.dump("", f)
        f.close()

    with open("customers.pickle", "rb") as f:  # This section loads the file into a list.
        customerList = pickle.load(f)

    while newRecord is True:  # This starts a loop to add records

        addCustomerList.append(Customer())

        cont = input("Add another customer? y/n > ")  # This section prompts "y/n" to continue.
        while cont.lower() not in ("y","n"):
            cont = input("Entry not allowed.  Add another customer? y/n > ")
        if cont == "n":
            break

    for i in range(len(customerList)):  # This section adds the old records to the bottom of the new list
        addCustomerList.append(customerList[i])

    pickle_out = open("customers.pickle","wb")  # This section saves new complete list to file.
    pickle.dump(addCustomerList, pickle_out)
    pickle_out.close()