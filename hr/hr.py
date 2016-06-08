# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


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

    list_of_functions = ["Show Table", "Add", "Remove", "Update", "Oldest", "Closest to AVG"]
    ui.print_menu("HR manager", list_of_functions, "Back to menu")
    chosen_number = ui.get_inputs(["Please enter a number: "], "")
    option = chosen_number[0]

    if option == '1':
        show_table('persons.csv')
    elif option == '2':
        add('persons.csv')
    elif option == '3':
        id_ = str(ui.get_inputs(["Please enter the ID: "], "")[0])
        remove('persons.csv', id_)
    elif option == '4':
        id_ = str(ui.get_inputs(["Please enter the ID: "], "")[0])
        update('persons.csv', id_)
    elif option == '5':
        get_oldest_person(table)
    elif option == '6':
        get_persons_closest_to_average(table)


# print the default table of records from the file
def show_table(table):

    list_of_titles = ["ID", "Name", "Birth date"]
    ui.print_table(data_manager.get_table_from_file(table), list_of_titles)
    start_module()

# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):

    list_of_titles = ["ID", "Name", "Birth date"]
    table_to_extend = data_manager.get_table_from_file(table)
    table_to_extend.append(common.ask_for_data_to_add(table_to_extend, list_of_titles[1:]))
    data_manager.write_table_to_file('persons.csv', table_to_extend)
    start_module()


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):

    table_to_shorten = data_manager.get_table_from_file(table)
    try:
        table_to_shorten.remove(common.ask_for_data_to_remove(table_to_shorten, id_))
        data_manager.write_table_to_file('persons.csv', table_to_shorten)
    except:
        ui.print_error_message("No person found with this ID!\n")
    start_module()


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):

    list_of_titles = ["ID", "Name", "Birth date"]
    table_to_update = data_manager.get_table_from_file(table)
    updated_table = common.ask_for_data_and_update(table_to_update, id_, list_of_titles[1:])
    data_manager.write_table_to_file('persons.csv', updated_table)
    start_module()

# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    # your code

    pass


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code

    pass
