#Calculator 

print("Calculator app")
try:
    number1 = eval(input("Enter first number: "))
    number2 = eval(input("Enter second number: "))


    symbol = input("Enter Mathematical operation (+, -, *, /, or %): ")
    allowed_symbols = ['+', '-', '*', '/', '%']


    if symbol in allowed_symbols:

        if symbol == '+':
            print(f"{number1} + {number2} = {number1 + number2}")

        elif symbol == '-':
            print(f"{number1} - {number2} = {number1 - number2}")

        elif symbol == '*':
            print(f"{number1} * {number2} = {number1 * number2}")

        elif symbol == '/':
            if number1 == 0 or number2 == 0:
                raise ZeroDivisionError("You cannot divide by zero.")
            print(f"{number1} / {number2} = {number1 / number2}")

        elif symbol == '%':
            print(f"{number1} % {number2} = {(number2 / number1)* 100}")

    else:
        raise ValueError("Invalid operator. Please use +, -, *, /, or %.")
    


except NameError as er:
    print("Enter only numbers")
except SyntaxError as sy:
    print("Not alowed mathematical action with symbols")