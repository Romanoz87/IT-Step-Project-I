#Calculator 
import sys

print("Calculator app")
while True:
    allowed_symbols = ['+', '-', '*', '/', '%', 'x']
    print("-"*100)
    symbol = input("Enter Mathematical operation (+, -, *, /, % or x): ").lower()
    if symbol in allowed_symbols and symbol == 'x':
        print("exit calculator")
        sys.exit(1)
    else:        
        try:
            if symbol in allowed_symbols:
                
                number1 = eval(input("Enter first number: "))
                number2 = eval(input("Enter second number: "))

            

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
                    number3 = number2/100*number1
                    print(f"{number1} % {number2} = ",  number3)

               
                    
            else:
                print("Invalid operator. Please use +, -, *, /, %, or x.")
                


        except NameError as er:
            print("Enter only numbers")
        except SyntaxError as sy:
            print("Not alowed mathematical action with symbols")