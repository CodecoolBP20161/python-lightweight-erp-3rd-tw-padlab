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

    list_of_functions = ["Show Table", "Add", "Remove", "Update", "The oldest: ", "Closest to average:"]

    ui.print_menu("HR", list_of_functions, "Back to menu")
    chosen_number = ui.get_inputs(["Please enter a number: "], "")

    option = chosen_number[0]

    if option == '1':
        show_table('persons.csv')
    elif option == '2':
        add('persons.csv')
    elif option == '3':
        hr.remove()
    elif option == '4':
        hr.update()
    elif option == '5':
        hr.get_oldest_person()
    elif option == '6':
        hr.get_persons_closest_to_average()
    elif option == '0':
        return
    else:
        raise KeyError("There is no such option.")



# print the default table of records from the file
def show_table(table):

    list_of_titles = ["ID", "Name", "Date of birth"]
    ui.print_table(data_manager.get_table_from_file(table), list_of_titles)
    start_module()



# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):

    list_of_titles = ["ID", "Name", "Date of birth"]
    table_to_extend = data_manager.get_table_from_file(table)
    table_to_extend.append(common.ask_for_data_to_add(table_to_extend, list_of_titles[1:]))
    data_manager.write_table_to_file('tools.csv', table_to_extend)

    return table_to_extend



# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):


    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):

    # your code

    return table


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
