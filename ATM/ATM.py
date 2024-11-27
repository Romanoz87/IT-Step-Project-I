# ATM pin 1234

import time
import json
from json import JSONEncoder

# დეკორატორი პინ კოდით ვალიდაციისთვის
def enter_pass(func):                             
        def wrapper(*args, **kwargs):
            i = 1
            while i<=3:   
                print("Enter Pin")
                try:
                    input_pin = int(input('****'))
                
                        
                    if input_pin == 1234:
                        print("Success...\n")
                        return func()
                    else:
                        print(f'\nInput correct pin number\n')
                        i += 1  
                        continue
                except ValueError:  
                    print("Allowed only numbers")
            print("You entered wrong pin 3 times, your card is blocked!...")    
        return wrapper


class Atm:
    def __init__(self, ballance=5000):
        self.ballance = ballance

   
#ფუნქცია თანხის გამოსატანად    
    def withdrow_cash(self, withdraw=0, fee=0.01):
        withdraw = eval(input("Enter withdraw amount: "))
        self.withdraw = withdraw
        
        if self.ballance < (withdraw + (withdraw * fee)):
            self.ballance = self.ballance
            print("'#"*100)
            print("Your ballance is not anough\n")
        else:
            time.sleep(0.5)
            print("In process...")
            self.ballance = self.ballance - (withdraw + (withdraw * fee))
            return self.ballance
        
    

#ფუნქცია ბალანსის შესავსებად  
    def add_ballance(self, input_amount=0):
        try:
            input_amount = int(input("Please put cash in ATM: "))
        except ValueError:
            print('enter only numbers')
        self.input_amount = input_amount
        
        self.ballance += input_amount

# ფუნქცია ბალანსის სანახავად    
    def see_ballance(self):
        print(f"Your remaining ballance is {self.ballance}$\n\n")

class jsonencode(JSONEncoder):
    def default(self, o):
        return o.__dict__




withd1 = Atm()



# ფუნქცია ძირითადი მენიუს გამოსატანად და მოქმედებების განსახორციელებლად

print("Welcome..\n")


@enter_pass
def action():
    while True:
        time.sleep(1)
        print("Choose action you want to do: ")
        print("Type 'b' to see your ballance\nType 'w' to withdrow cash\nType 'a' to add amount to your ballance\nType 'x' to exit")
        action = input('\nEnter symbol___ ')
        if action == 'x':
            print('Exit...')
            break
            
        elif action == 'w':
            withd1.withdrow_cash()

        elif action == 'a':
            withd1.add_ballance()

        elif action == 'b':
            withd1.see_ballance()
        

action()



data = json.dumps(withd1, cls=jsonencode, indent=2)
with open("atm.json", mode = 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2)




