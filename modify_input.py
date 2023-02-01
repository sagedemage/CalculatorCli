import re

def convert_digit_to_number(exp):
    """ Convert digit to number """

    i = 0

    while i < len(exp):
        if exp[i].isdigit():
            exp[i] = int(exp[i])
        i = i + 1

    return exp

def add_space_between_ops(input):
    """Add space between each operator"""
    new_input = ""

    i = 0

    while i < len(input):
        new_input += input[i]
        if i == len(input)-1:
            break 
        if input[i+1].isdigit() == False:
            new_input += " "
        if input[i].isdigit() == False:
            new_input += " "
        i = i + 1

    return new_input

