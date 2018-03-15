#####################################
#   COMPSCI 105 S2 C, 2015          #
#   Assignment 1 Question 1         #
#                                   #
#   @author     Huang Jiachen and jhua924   #
#   @version    22/09/2015            #
#####################################

from Item import Item

class Stock:
    # the constructor
    def __init__(self):
        self.__items = []

    # This function gets the number of items in stock.
    def get_size(self):
        return len(self.__items)

    # This function loads all the items on sale into the list.
    def load_items(self, filename):
        try:
            infile = open(filename, "r")
            stock_str = infile.read()
            infile.close()   
            stock_list = stock_str.split("\n")
            for item in stock_list:
                item_list = item.split(",")
                self.__items += [Item(item_list[0], item_list[1], float(item_list[2]), int(item_list[3]))]
        except IOError: 
            print("Error: File does not exist.")
    
    # This function saves all the items on sale into a file.
    def save_items(self, filename):     
        try:
            out_file = open(filename, 'w')
            for item in self.__items:
                out_file.write(str(item) + "\n")
            out_file.close()
        except IOError: 
            print("Error: File writing error.")

    #################################################################################################
    # The implementation of the above functions have already been given.                            #
    # Please DO NOT MODIFY the content of the ABOVE functions, as they are used by other functions. #
    # Please given the implementation of the following two functions to complete the program.       #
    #################################################################################################
    
    # This function finds an item on sale based on the item code.
    def find_item(self, code):
        for items in self.__items:
                if items.getCode() == code and items.getQuantity() != 0:
                        items.setQuantity(items.getQuantity()-1)
                        break
                        """Item - " + str(items.getDescription()) + " is added to the shopping cart."""
                if items.getCode() == code and items.getQuantity() == 0:
                        break
                        """Sorry, item " + str(items.getCode()) + " is out of stock."""
        return items
        ## IMPLEMENT THIS METHOD
    
    # This function displays all the items on sale.
    def display_items(self):
        for items in self.__items:
                if items.getQuantity()!= 0:
                        print(items)
        ## IMPLEMENT THIS METHOD
