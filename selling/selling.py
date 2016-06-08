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

    list_of_functions = ["Show Table", "Add", "Remove", "Update", "Lowest Price", "Between dates"]
    ui.print_menu("Selling", list_of_functions, "Back to menu")
    chosen_number = ui.get_inputs(["Please enter a number: "], "")
    option = chosen_number[0]

    if option == '1':
        show_table('sellings.csv')
    elif option == '2':
        add('sellings.csv')
    elif option == '3':
        id_ = str(ui.get_inputs(["Please enter the ID: "], "")[0])
        remove('sellings.csv', id_)
    elif option == '4':
        id_ = str(ui.get_inputs(["Please enter the ID: "], "")[0])
        update('sellings.csv', id_)
    elif option == '5':
        get_lowest_price_item_id(table)
    elif option == '6':
        get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
    elif option == '0':
        return
    else:
        raise KeyError("There is no such option.")


# print the default table of records from the file
def show_table(table):

    list_of_titles = ["ID", "Title", "Price", "Month", "Day", "Year"]
    ui.print_table(data_manager.get_table_from_file(table), list_of_titles)
    start_module()


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):

<<<<<<< HEAD
    list_of_titles = ["ID", "Title", "Price", "Month", "Day", "Year"]
    table_to_extend = data_manager.get_table_from_file(table)
    table_to_extend.append(common.ask_for_data_to_add(table_to_extend, list_of_titles[1:]))
    data_manager.write_table_to_file('sellings.csv', table_to_extend)
    start_module()


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):

    table_to_shorten = data_manager.get_table_from_file(table)
    try:
        table_to_shorten.remove(common.ask_for_data_to_remove(table_to_shorten, id_))
        data_manager.write_table_to_file('sellings.csv', table_to_shorten)
    except:
        ui.print_error_message("No game found with this ID!\n")
    start_module()


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):

    list_of_titles = ["ID", "Title", "Price", "Month", "Day", "Year"]
    table_to_update = data_manager.get_table_from_file(table)
    updated_table = common.ask_for_data_and_update(table_to_update, id_, list_of_titles[1:])
    data_manager.write_table_to_file('sellings.csv', updated_table)
    start_module()


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
