def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
     return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        return "Operator was not found"

print(calcule(40, ".", 2))