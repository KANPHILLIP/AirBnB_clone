#!/usr/bin/python3
"""module to print items in a list """


def print_items(input_list):
    """ method that prints item in a list """
    for i in input_list:
        print(i)


if __name__ == "__main__":

    my_list = ['Phillip', 'Chiloane', 'ALX', 'Best', 'School']

    print_items(my_list)
