from Item import Item

class Cart:
    # the constructor
    def __init__(self):
        self.__items = []
    
    # This function gets the number of items in the shopping cart.
    def get_size(self):
        return len(self.__items)


    # This function adds an item into the shopping cart.
    def add_item(self, item):
        if item.getQuantity() != 0:
            print("Item - " + str(item.getDescription()) + " is added to the shopping cart.")
            self.__items += [item]
        else:
            print("Sorry, item " + str(item.getCode()) + " is out of stock.")
            print("Please select a different item.")
        ## IMPLEMENT THIS METHOD
    
    # This function finds an item on sale based on the item code.
    def find_item(self, code):
        r = 0
        for i in self.__items:
            if i.getCode() == code:
                r = i
            else:
                r = None
            return r

    # This function removes an item from the shopping cart.
    def delete_item(self, item):
        item.setQuantity(item.getQuantity()+1)
        print("Item - " + str(item.getDescription()) + " is removed from the shopping cart.")
        ## IMPLEMENT THIS METHOD

    # This function clears everything in the shopping cart.
    def discard_all(self):
        for i in self.__items:
            i.setQuantity(i.getQuantity()+1)
        self.__items = []
        ## IMPLEMENT THIS METHOD
    
    # This function prints out the items bought and calculates the total amount due.
    def check_out(self):
        r = 0
        for i in self.__items:
            print(i.getDescription() + "/$" + str(i.getPrice()))
            r += i.getPrice()
        return r
        ## IMPLEMENT THIS METHOD
