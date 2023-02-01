from convert_to_list import convert_to_list
from calc import convert_digit_to_number, multiplcation_or_division, addition_or_subtraction
from add_space_between_ops import add_space_between_ops 

#exp = convert_to_list("12 / 1 - 2 + 1 * 8")
#exp = convert_to_list("12 * 3 + 3 / 10 - 32")

user_inp = input("Enter a math expression: ")

inp = add_space_between_ops(user_inp)

exp = convert_to_list(inp)

# Code runs here
exp = convert_digit_to_number(exp)
exp = multiplcation_or_division(exp)
exp = addition_or_subtraction(exp)

ans = round(exp[0], 10)
print(ans)
