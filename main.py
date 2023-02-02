from convert_to_list import convert_to_list
from calc import multiplcation_or_division, addition_or_subtraction, exponential, parenthesis
from modify_input import convert_digit_to_number, add_space_between_ops

user_inp = input("Enter a math expression: ")

inp = add_space_between_ops(user_inp)

exp = convert_to_list(inp)

exp = convert_digit_to_number(exp)

# Calc runs here
exp = parenthesis(exp)
exp = exponential(exp)
exp = multiplcation_or_division(exp)
exp = addition_or_subtraction(exp)

ans = round(exp[0], 10)
print(ans)
