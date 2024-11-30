
from random_generator import random_word, question
from random_generator import selected_item # შემოგვაქვს რანდომად შერჩეული სიტყვის ფუნქცია

list1 = list(selected_item)       # ლისტში ვათავსებთ რანდომ სიტყვის სიმბოლოებს

list_of = [] # ცარიელი სიმბოლოების ლისტი. 


for _ in range(len(selected_item)):                    # რანდომ სიტყვის რაოდენობის ფიფქების სიას ვაკეთებთ
    
    list_of.append("*")

print('\nGuess thee country with flags\nyou have 10 tries\n')
print("-"*50)
quest = question()

print('\n',*list_of)
print("-"*50)


 # მინიშნება შემოტანილ რანდომ სიტყვაზე
print("\n")


print("select action:\n\n'1') Guess whole word \n'2') Guess step by step ")
symbols = ['1', '2']
while True:
        action = input("\nguess number with one try. you win bonus or lose everything: _")

        

        if action in symbols:
            
            if action == '1':
                word = input("Type word here:_").lower().strip()
                if word == selected_item:
                    print("\n...congrats you won with one try...\n")
                else:
                    print('\nSorry you lose')
            elif action == '2':

                i = 1
                while i <= 10:
                    user_input = input(f"\ninput word or symbol to guess {i}-st try: ").lower()

                    if i < 10:
                            
                        if user_input in list1:

                            indexes = [index for index, value in enumerate(list1) if value == user_input]
                            for index in indexes:
                                
                                list_of[index] = list1[index]
                                    
                            print("you guessed one symbol in word.\n")
                            print(*list_of)
                                            
                            if list_of == list1:                                                        # თუ ამოცნობილი სიმბოლოების ლისტი გაუტოლდა რანდომ ლისტს, მომხმარებელი იმარჯვებს
                                print(f"\n...congrats you guessed word with {i}-th try..\n")
                                break
                                                
                        else:
                            print("wrong symbol")
                    i += 1
                else:
                        
                    print("\nSorry you didnt guess the word\n")
                print("...Game Over...")
        else:
            print("Wrong symbol. please choose 1) or 2) ")

            
                
                                
