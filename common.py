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

        for char in range(1, 9):
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
        to_all_data = str("".join(ui.get_inputs(["Please enter a " + str(title) + ": "], "")))
        all_data.append(to_all_data)


    return all_data


def ask_for_data_to_remove(table, id_):

    for all_info in table:
        id_to_observe = "".join(all_info[0])
        if id_to_observe == id_:
            return all_info


def ask_for_data_and_update(table, id_, list_of_titles):

    ui.print_menu("What do you want to update?", list_of_titles, "Back")
    to_update = int(ui.get_inputs(["Please enter a number: "], "")[0])
    update_to = str(ui.get_inputs(["Update data to: "], "")[0])
    if to_update != 0:
        for all_info in table:
            id_to_observe = "".join(all_info[0])
            if id_to_observe == id_:
                all_info[to_update] = update_to
        return table
    else:
        return
