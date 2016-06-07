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
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this manager by a menu
def start_module():

    inputs = int(ui.get_inputs(["Please enter a number: "], ""))
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


    ui.print_table(get_table_from_file(table))




# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):

    new_record = []
    new_record.append(generate_random)
    new_record.append(ui.get_inputs("What's the name of the game?"))
    new_record.append(ui.get_inputs("What is the selling price of the game?"))
    new_record.append(ui.get_inputs("What is the date the purchase was made?(month; day; year format pls)"))
    table.append(new_record)
    write_table_to_file(selling.csv, table)

    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):

    for i in table:
        if i == id_:
            table.remove(i)
    write_table_to_file(selling.csv)


    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):


    which_update = int(ui.get_inputs("what do you want to update? (1: title, 2: selling price, 3: date of purchase)"))
    answer_1 = ui.get_inputs("The new title please: ")
    answer_2 = ui.get_inputs("The new selling price please: ")
    answer_3 = ui.get_inputs("Date of purchase please: ")
    if which_update == 1:
        table[which_update] = str(answer_1)
    if which_update == 2:
        table[which_update] = str(answer_2)
    if which_update == 3:
        table[which_update] = str(answer_3)
    else:
        ValueError ("Please enter 1, 2, or 3")

    write_table_to_file(sellings.csv, id_)
    return table


# special functions:
# ------------------

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order
def get_lowest_price_item_id(table):

    

    pass


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):

    # your code

    pass
