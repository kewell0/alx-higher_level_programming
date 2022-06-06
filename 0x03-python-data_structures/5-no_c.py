#!/usr/bin/python3
def no_c(my_string):
    """
    A function to remove all characters c and C from a string.
    """
    my_list = []
    for c in my_string:
        if c != 'c' and c != 'C':
            my_list.append(c)
    return "".join(my_list)
