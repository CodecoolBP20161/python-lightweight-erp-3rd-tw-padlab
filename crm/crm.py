# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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

    list_of_functions = ["Show Table", "Add", "Remove", "Update", "Longest name", "Who is subscribed?"]
    ui.print_menu("Customers manager", list_of_functions, "Back to menu")
    chosen_number = ui.get_inputs(["Please enter a number: "], "")
    option = chosen_number[0]

    if option == '1':
        show_table('customers.csv')
    elif option == '2':
        add('customers.csv')
    elif option == '3':
        id_ = str(ui.get_inputs(["Please enter the ID: "], "")[0])
        remove('customers.csv', id_)
    elif option == '4':
        id_ = str(ui.get_inputs(["Please enter the ID: "], "")[0])
        update('customers.csv', id_)
    elif option == '5':
        get_longest_name_id('customers.csv')
    elif option == '6':
        get_subscribed_emails('customers.csv')
    elif option == '0':
        return
    else:
        raise KeyError("There is no such option.")


# print the default table of records from the file
def show_table(table):

    list_of_titles = ["ID", "Name", "Email", "Subscribed(0/1)"]
    ui.print_table(data_manager.get_table_from_file(table), list_of_titles)
    start_module()


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):

    list_of_titles = ["ID", "Name", "Email", "Subscribed(0/1)"]
    table_to_extend = data_manager.get_table_from_file(table)
    table_to_extend.append(common.ask_for_data_to_add(table_to_extend, list_of_titles[1:]))
    data_manager.write_table_to_file('customers.csv', table_to_extend)
    start_module()


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):

    table_to_shorten = data_manager.get_table_from_file(table)
    try:
        table_to_shorten.remove(common.ask_for_data_to_remove(table_to_shorten, id_))
        data_manager.write_table_to_file('customers.csv', table_to_shorten)
    except:
        ui.print_error_message("No customer found with this ID!\n")
    start_module()


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):

    list_of_titles = ["ID", "Name", "Email", "Subscribed(0/1)"]
    table_to_update = data_manager.get_table_from_file(table)
    updated_table = common.ask_for_data_and_update(table_to_update, id_, list_of_titles[1:])
    data_manager.write_table_to_file('customers.csv', updated_table)
    start_module()


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
def get_longest_name_id(table):

    # your code

    pass


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):

    table_that_need_to_iterate_over = data_manager.get_table_from_file(table)
    subscribed_people = []
    for name_email_list in table_that_need_to_iterate_over:
        if name_email_list[3] == "1":
            subscribed_people.append([name_email_list[2], name_email_list[1]])
    titles = ["e-mail", "name"]
    ui.print_table(subscribed_people, titles)
    list_to_return = []
    for name_email_list in subscribed_people:
        string_to_add = ";".join(name_email_list)
        list_to_return.append(string_to_add)

    return list_to_return
