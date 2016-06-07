# implement commonly used functions here
import random
import string
import ui

# generate and return a unique and random
# (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter) string
# it must be unique in the list
def generate_random(table):

    while True:

        char_list = []

        cap_abc = list(string.ascii_uppercase)
        low_abc = list(string.ascii_lowercase)
        numbers = list(string.digits)
        symbols = ['@', '#', '&']

        list_of_types = [cap_abc, low_abc, numbers, symbols, cap_abc, low_abc, numbers, symbols]

        for char in range(1, 8):
            which_list = random.choice(list_of_types)
            char_to_add = random.choice(which_list)
            char_list.append(char_to_add)
            list_of_types.remove(which_list)

        unique_code = "".join(char_list)

        if unique_code not in table:
            return unique_code


def ask_for_data_to_add(table, list_of_titles):

    code = generate_random(table)

    all_data = [code]

    for title in list_of_titles:
        to_all_data = ui.get_inputs(["Please enter a " + str(title) + ": "], "")
        all_data.append(to_all_data)


    return all_data
