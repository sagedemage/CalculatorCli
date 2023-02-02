def search_left_parenthesis(exp):
    i = 0

    while i < len(exp):
        if exp[i] == '(':
            break

        i = i + 1

    return int(i)

def search_right_parenthesis(exp):
    j = 0

    while j < len(exp):
        if exp[j] == ')':
            break

        j = j + 1
    
    return int(j)

def parenthesis(exp):
    """ Addition and Subtraction """
    new_exp = []

    i = search_left_parenthesis(exp)
    j = search_right_parenthesis(exp)

    if (i == j):
        return exp

    exp_temp = exp[i+1:j]

    exp_temp = exponential(exp_temp)
    exp_temp = multiplcation_or_division(exp_temp)
    exp_temp = addition_or_subtraction(exp_temp)

    s = 0

    while s < i:
        new_exp.append(exp[s])
        s = s + 1

    ans = exp_temp[0]

    new_exp.append(ans)

    j = j + 1

    while j < len(exp):
        new_exp.append(exp[j])
        j = j + 1

    return new_exp

def exponential(exp):
    """ Addition and Subtraction """
    i = 0

    while i < len(exp):
        if exp[i] == '^':
            ans = pow(exp[i-1], exp[i+1])
            exp[i-1] = ans
            exp.pop(i)
            exp.pop(i)
            i = 0

        i = i + 1
    return exp

def multiplcation_or_division(exp):
    """ Apply mutiplication or division """
    i = 0

    while i < len(exp):
        if exp[i] == '/':
            ans = exp[i-1] / exp[i+1]
            exp[i-1] = ans
            exp.pop(i)
            exp.pop(i)
            i = 0

        if exp[i] == '*':
            ans = exp[i-1] * exp[i+1]
            exp[i-1] = ans
            exp.pop(i)
            exp.pop(i)
            i = 0

        i = i + 1
    return exp

def addition_or_subtraction(exp):
    """ Addition and Subtraction """
    i = 0

    while i < len(exp):
        if exp[i] == "-":
            ans = exp[i-1] - exp[i+1]
            exp[i-1] = ans
            exp.pop(i)
            exp.pop(i)
            i = 0

        if exp[i] == "+":
            ans = exp[i-1] + exp[i+1]
            exp[i-1] = ans
            exp.pop(i)
            exp.pop(i)
            i = 0

        i = i + 1
    return exp