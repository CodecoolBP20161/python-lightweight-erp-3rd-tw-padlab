

# An example output:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
def print_table(table, title_list):

    print(('|') + (" | ".join(title_list)) + ('|'))
    for row in table:
        print(('|') + ('-') * 50 + ('|'))
        print(('|') + (" | ".join(row)) + ('|'))

    print(('|') + ('-') * 50 + ('|'))



# An example output:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# see the function call in main.py
def print_menu(title, list_options, exit_message):

    print(title)
    for number_of_option in range(0, len(list_options)):
        print('(' + str(number_of_option+1) + ') ' + list_options[number_of_option])
    print('(0) ' + exit_message)

    pass


# see the function call in main.py
def get_inputs(list_titles, title):
    record = [0]

    chosen_function = input(list_titles[0])

    record[0] = chosen_function

    return record


# see the function call in main.py
def print_error_message(message):

    print(message)
