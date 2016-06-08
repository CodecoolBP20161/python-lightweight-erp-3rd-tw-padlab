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

    list_of_functions = ["Show Table", "Add", "Remove", "Update", "Highest profit", "Average profit of items"]
    ui.print_menu("Accounting manager", list_of_functions, "Back to menu")
    chosen_number = ui.get_inputs(["Please enter a number: "], "")
    option = chosen_number[0]

    if option == '1':
        show_table('items.csv')
    elif option == '2':
        add('items.csv')
    elif option == '3':
        id_ = str(ui.get_inputs(["Please enter the ID: "], "")[0])
        remove('items.csv', id_)
    elif option == '4':
        id_ = str(ui.get_inputs(["Please enter the ID: "], "")[0])
        update('items.csv', id_)
    elif option == '5':
        table = data_manager.get_table_from_file('items.csv')
        which_year_max(table)
    elif option == '6':
        table = data_manager.get_table_from_file('items.csv')
        avg_amount(table, "2015")
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

    list_of_titles = ["Month", "Day", "Year", "Type", "Ammount"]
    table_to_extend = data_manager.get_table_from_file(table)
    table_to_extend.append(common.ask_for_data_to_add(table_to_extend, list_of_titles[1:]))
    data_manager.write_table_to_file('items.csv', table_to_extend)
    start_module()


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):

    table_to_shorten = data_manager.get_table_from_file(table)
    try:
        table_to_shorten.remove(common.ask_for_data_to_remove(table_to_shorten, id_))
        data_manager.write_table_to_file('items.csv', table_to_shorten)
    except:
        ui.print_error_message("Nothing with this ID!\n")
    start_module()


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):

    list_of_titles = ["Month", "Day", "Year", "Type", "Ammount"]
    table_to_update = data_manager.get_table_from_file(table)
    updated_table = common.ask_for_data_and_update(table_to_update, id_, list_of_titles[1:])
    data_manager.write_table_to_file('items.csv', updated_table)
    start_module()

# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out) (2015 or 2016)
# return the answer (number)
def which_year_max(table):

    year_15 = 0
    year_16 = 0
    table_to_check = table
    for item in table_to_check:
        if item[3] == '2015':
            if item[4] == 'in':
                year_15 += int(item[5])
            else:
                year_15 -= int(item[5])
        elif item[3] == '2016':
            if item[4] == 'in':
                year_16 += int(item[5])
            else:
                year_16 -= int(item[5])
    if year_15 > year_16:
        year = 2015
    elif year_16 > year_15:
        year = 2016
    ui.print_table([[str(year)]], ["Year of the highest profit"])
    return year


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    in_list = []
    out_list = []

    for account_of_a_date in table:
        year_to_observe = account_of_a_date[3]
        if year_to_observe == year:
            in_or_out = account_of_a_date[4]
            if in_or_out == "in":
                amount = account_of_a_date[5]
                in_list.append(amount)
            else:
                amount = account_of_a_date[5]
                out_list.append(amount)

    all_in = common.sum_of_list(in_list)
    all_out = common.sum_of_list(out_list)

    profit = all_in - all_out

    if (common.len_of_list(in_list) + common.len_of_list(out_list)) != 0:
        profit_avg = profit/(common.len_of_list(in_list) + common.len_of_list(out_list))
    else:
        profit_avg = 0
        
    return profit_avg
