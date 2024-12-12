#Calculator 
import sys

print("Calculator app")
while True:
    allowed_symbols = ['+', '-', '*', '/', '%', 'x']  # ნებადართული მოქმედებების სიმბოლოები 
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
                    try:
                        print(f"{number1} / {number2} = {number1 / number2}")
                    
                    except ZeroDivisionError:
                        print("You cannot divide by zero.")

                elif symbol == '%':
                    number3 = number2/100*number1
                    print(f"{number1} % {number2} = ",  number3)

               
                    
            else:
                print("Invalid operator. Please use +, -, *, /, %, or x.")
                


        except NameError as er:
            print("Enter only numbers")
        except SyntaxError as sy:
            print("Not alowed mathematical action with symbols")
        except TypeError as err:
            print("',' symbol not allowed please use '.' instead")