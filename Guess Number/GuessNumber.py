import random
from random import randint
import time

random_number = randint(1, 100)

user_input = 0
print('#'*100)
print("\n\nLets guess random number from 1 to 100\n\nYou have 7 try\n")

i = 1
while i <=7:
    try:
        user_input = int(input(f"input number. Try {i}:  "))
    
        
        if i < 7:
            
            if user_input == random_number: 
                print(f"Congrats.. You Guessed number with {i} try\n")
                break

            elif user_input < random_number:  
                print(f"Wrong number.. Please enter bigger number...\n")

            elif user_input > random_number:   
                print(f"Wrong number.. Please enter smaller number...\n")
        else:
            
            print("sorry you didn't guess number with 7 triesn\n")
            
        i +=1

    except  ValueError as ex:
        print("You must enter only numbers. Try again")


msg = "\nGame Over........\n\n\n\n\nDirected by Roman Chkadua\n\n It academy Step\n\n  2024 year\n\n....\n...\n..\n."
for i in msg:
    print(i, end="", flush=True)

    time.sleep(0.03)

