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