
from guessed_word import my_func # შემოგვაქვს რანდომად შერჩეული სიტყვის ფუნქცია

selected_item = my_func()
list1 = list(selected_item)       # ლისტში ვათავსებთ რანდომ სიტყვის სიმბოლოებს

list_of = [] # ცარიელი სიმბოლოების ლისტი. 


for _ in range(len(selected_item)):                    # რანდომ სიტყვის რაოდენობის ფიფქების სიას ვაკეთებთ
    
    list_of.append("*")

print('\nGuess random word from Fruit names\n you have 10 tries\n\n :', *list_of)
print("\n")


i = 1
while i <= 10:
    user_input = input(f"\ninput word or symbol to guess {i}-st try: ")

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