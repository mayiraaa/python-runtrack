def any_computation(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2

print (any_computation(10, "+", 5))  # Output: 15
print (any_computation(10, "-", 5))  # Output: 5
print (any_computation(10, "*", 5))  # Output: 50
