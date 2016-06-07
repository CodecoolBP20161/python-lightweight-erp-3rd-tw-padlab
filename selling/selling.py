# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("module.name", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("module.name", current_file_path + "/../data_manager.py").load_module()


# start this manager by a menu
def start():

    inputs = input(["Please enter a number: "], "")
    option = inputs[0]
    if option == 1:
        show_table()
    elif option == 2:
        add()
    elif option == 3:
        remove()
    elif option == 4:
        update()
    elif option == 5:
        get_lowest_price_item_id()
    elif option == 6:
        get_items_sold_between()
    else:
        raise KeyError("There is no such option.")




# print the default table of records from the file
def show_table(table):


    print_table(write_table_to_file(selling.csv, table))




# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):

    new_record = []
    new_record.append(generate_random)
    new_record.append(input("What's the name of the game?"))
    new_record.append(input("What is the selling price of the game?"))
    new_record.append(input("What is the date the purchase was made?(month; day; year format pls)"))
    table.append(new_record)
    write_table_to_file(selling.csv, table)

    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):

    for i in table:
        if i = id_:
            table.remove(i)
    write_table_to_file(selling.csv)


    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):

    new_data



    return table


# special functions:
# ------------------

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order
def get_lowest_price_item_id(table):

    # your code

    pass


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):

    # your code

    pass
