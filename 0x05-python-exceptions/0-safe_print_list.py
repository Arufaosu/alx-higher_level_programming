#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    starting_return = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            starting_return += 1
        except IndexError:
            break
    print("")
    return (starting_return)
