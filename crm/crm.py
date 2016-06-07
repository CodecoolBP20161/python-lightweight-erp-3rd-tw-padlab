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
ui = SourceFileLoader("module.name", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("module.name", current_file_path + "/../data_manager.py").load_module()


# start this manager by a menu
def start():
    inputs = ui.get_inputs(["Please enter a number: "], "")
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
        get_longest_name_id()
    elif option == 6:
        get_subscribed_emails()
    else:
        raise KeyError("There is no such option.")


# print the default table of records from the file
def show_table(table):

    print_table(write_table_to_file(customers.csv, table)

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):

    new_record = []
    new_record.append(generate_random())
    new_record.append(input("What is the customer's name?: "))
    new_record.append(input("What is the customer's e-mail address?: "))
    new_record.append(input("Is the customer subscribed?(1/0 = yes/not): "))
    table.append(new_record)
    write_table_to_file(customers.csv, table)

    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):

    for x in table:
        if x[0] = id_:
            table.remove(x)
    write_table_to_file(customers.csv, table)

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):

    # your code

    return table


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

    # your code

    pass
