# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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

    list_of_functions = ["Show Table", "Add", "Remove", "Update",
                         "Which year has the highest profit?",
                         "What is the average (per item) profit in a given year"]

    ui.print_menu("Accounting", list_of_functions, "Back to menu")
    chosen_number = ui.get_inputs(["Please enter a number: "], "")

    option = chosen_number[0]

    if option == '1':
        show_table('items.csv')
    elif option == '2':
        add('items.csv')
    elif option == '3':
        remove()
    elif option == '4':
        update()
    elif option == '5':
        get_counts_by_manufacturers(table)
    elif option == '6':
        get_average_by_manufacturer(table, manufacturer)
    elif option == '0':
        return
    else:
        raise KeyError("There is no such option.")

# print the default table of records from the file
def show_table(table):

    list_of_titles = ["ID", "Month", "Day", "Year", "Type", "Amount"]
    ui.print_table(data_manager.get_table_from_file(table), list_of_titles)
    start_module()

# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):

    list_of_titles = ["ID", "Month", "Day", "Year", "Type", "Amount"]
    table_to_extend = data_manager.get_table_from_file(table)

    table_to_extend.append(common.ask_for_data_to_add(table_to_extend, list_of_titles[1:]))

    data_manager.write_table_to_file('items.csv', table_to_extend)

    return table_to_extend


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):

    # your code

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return the @table
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out) (2015 or 2016)
# return the answer (number)
def which_year_max(table):

    # your code

    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
