def add_space_between_ops(input):
    """Add space between each operator"""
    new_input = ""

    i = 0

    while i < len(input):
        new_input += input[i]
        if i == len(input)-1:
            break 
        if input[i+1] == '+' or input[i+1] == '-' or input[i+1] == "*" or input[i+1] == "/":
            new_input += " "
        if input[i] == '+' or input[i] == '-' or input[i] == '*' or input[i] == '/':
            new_input += " "
        i = i + 1

    return new_input