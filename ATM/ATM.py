import os, json, sys, time
from json import JSONEncoder

# მომხმარებელთა ბარათის ნომრები და პინები
    # (123456789, 1234, 5000),
    # (123456783, 2345, 6000),
    # (456784324, 3421, 10000),
    # (873213456, 1221, 700),
    # (111111111, 1111, 9000),
    # (112211111, 1311, 9000),   

#==================================================================================================
#დეკორატორი პინ კოდით ვალიდაციისთვის
def verification(func):                             
        def wrapper(*args, **kwargs):
                         
                for pin in result:
                        
                    if input_pin == pin['_Atm__pin'] and input_card == pin['_Atm__card_id']:
                        print("Success...\n")
                        return func()
                else:    
                    print(f'\nInput correct pin number\n')
                             
        return wrapper
    
#==================================================================================================
# ფაილიდან ამოსაკითხი ფუნქცია
def read_data():
    with open('atm.json', mode='r', encoding='utf-8') as file:
        return json.load(file)
    
# ფაილში შენახვის ფუნქცია
def write_data(data):
    
    with open("atm.json", mode = 'w', encoding='utf-8') as file:
        json.dump(data, file, cls=jsonencode, indent=2)


#==================================================================================================
# ძირითადი კლასი 
class Atm:
    def __init__(self, card_id=None, pin=None, ballance=None):
        
        self.__card_id = card_id
        self.__pin = pin
        self.ballance = ballance
#==================================================================================================   
#ფუნქცია თანხის გამოსატანად    
    def withdrow_cash(self, withdraw=0, fee=0.01):
        
        self.withdraw = withdraw
        for bal in result:
            if input_card == bal['_Atm__card_id']:
                if bal['ballance'] < (withdraw + (withdraw * fee)):
                    bal['ballance'] == bal['ballance']
                    print("-"*100)
                    print("Your ballance is not anough\n")
                else:
                    time.sleep(0.5)
                    print("In process...")
                    bal['ballance'] = bal['ballance'] - (withdraw + (withdraw * fee))
                    return result
#==================================================================================================
# ფუნქცია ბალანსის შესავსებად  
    def add_ballance(self, input_amount=0):
        
        self.input_amount = input_amount
        for bal in result:
            if input_card == bal['_Atm__card_id']:
                bal['ballance'] = bal['ballance']+ input_amount
        
#==================================================================================================
# ფუნქცია ბალანსის სანახავად    
    def see_ballance(self):
        for bal in result:
            if input_card == bal['_Atm__card_id']:

                print("-"*50)
                print(f"Your remaining ballance is {bal['ballance']}$\n\n")
                print("-"*50)
#==================================================================================================
# ფუნქცია პინის შესაცვლელად    
    def change_pin(self, new_pin):
        self.new_pin = new_pin
        for pin in result:
            if input_card == pin['_Atm__card_id']:
                pin['_Atm__pin'] = self.new_pin

#  ენკოდერი
class jsonencode(JSONEncoder):
    def default(self, o):
        return o.__dict__


# მომხმარებელთა მონაცებემი, რომელიც გადაეცემა ძირითად კლასს ბარათის ნომერი, პინი და ბალანსი.
customers_data = [
    Atm(123456789, 1234, 5000),
    Atm(123456783, 2345, 6000),
    Atm(456784324, 3421, 10000),
    Atm(873213456, 1221, 700),
    Atm(111111111, 1111, 9000),
    Atm(112211111, 1311, 9000),   
]

#---------------------------------------------------------------------------------------
json_filename = 'ATM' + '.json'
    
# შემოწმება თუ უკვე არსებობს ფაილი მეორედ არ ჩაიწერება
if not os.path.exists(json_filename):
    try:
        write_data(customers_data)
       
        print(f"Data successfully saved as {json_filename}")
                
    except (TypeError, OverflowError) as json_err:
            print(f"JSON failed: {json_err}")
else:
    print(f"JSON file '{json_filename}' already exists. Skipping JSON write.")



result = read_data()  # ვიძახებთ ფაილიდან წაკითხვის ფუნქციას

#==================================================================================
# ფუნქცია მენიუს გამოსატანად და მოქმედებების განსახორციელებლად

print("\nWelcome..\n")

@verification
def action():
    while True:
        time.sleep(1)
        print("Choose action you want to do: ")
        print("Type 'b' to see your ballance\nType 'w' to withdrow cash\nType 'a' to add amount to your ballance\nType 'p' to change pin code\nType 'x' to exit")

        action = input('\nEnter symbol___ ').lower()
#_________________________________________________________________________________________________________________
# 'x' შეყვანის შემთხვევაში მომხმარებელი გადის ბანკომატის პროგრამიდან და ინახავს საბოლოო მონაცემს        
        if action == 'x':                               
            print('Exit...')
            write_data(result)
            
            break
#_________________________________________________________________________________________________________________
# 'w' შეყვანს შემთხვევაში მომხმარებელი იძახებს თანხის გამოტანის ფუნქციას             
        elif action == 'w':                                              
            withdraw = eval(input("Enter withdraw amount: "))
            customer1.withdrow_cash(withdraw)
#_________________________________________________________________________________________________________________
# 'a' შეყვანის შემთხვევაში მომხმარებელი იძახებს თანხის დამატების ფუნქციას
        elif action == 'a':
            try:
                input_amount = eval(input("Please put cash in ATM: "))
            except ValueError:
                print('enter only numbers')
            customer2 = Atm()
            customer2.add_ballance(input_amount)
#_________________________________________________________________________________________________________________
# 'b' შეყვანის შემთხვევაში მომხმარებელი ნახულობს დარჩენილ ბალანსს
        elif action == 'b':
            customer1 = Atm()
            customer1.see_ballance()
#_________________________________________________________________________________________________________________
# 'p' შეყვანის შემთხვევაში  ვიძახებთ პინის შეცვლის ფუნქციას       
        elif action == 'p':
            
                customer1 = Atm()                
                while True:
                    try:
                        new_pin = int(input('change new pin'))
                        
                        # ვამოწმებთ რომ მომხმარებელმა მხოლოდ 4 სიმბოლო შეიყვანოს
                        if len(str(new_pin)) == 4:                          
                            customer1.change_pin(new_pin)
                            print("\nPin is changed\n")
                            break                       
                        else:
                            print("Invalid input. Please make sure you enter exactly 4 digits.")
                    except ValueError:
                        print("wrong symbols, try only numbers")
                        
        else:
            print("\nplease enter only valid symbols ( a, b, w, p or x)\n")

#==================================================================================================================================
# მომხმარებელს კონსოლიდან შეჰყავს id ბარათის მონაცემები და პინ კოდი გამოირიცხება არასწორი სიმბოლოების შეყვანა
print("Enter Id and pin numbers below \n")

try:
    input_card = int(input("input card number: _ "))
except:
    print("\n Wrong symbols. Allowed only numbers. ATM finished working\n ")
    sys.exit(1)

try:
    input_pin = int(input('input pin:_  '))
except:
    print("\n Wrong symbols. Allowed only numbers. ATM finished working\n ")
    sys.exit(1)

action()




