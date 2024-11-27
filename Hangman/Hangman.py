
from guessed_word import my_func

selected_item = my_func()
list1 = list(selected_item)
# print(list1)
list_of = [] # ცარიელი სიმბოლოების ლისტი. 


for _ in range(len(selected_item)):
    
    list_of.append("*")
print('\nGuess random word:_', *list_of)
print("\n")
i = 1
while i <= 10:
    user_input = input("\ninput word or symbol to guess: ")

    if i < 10:
        
        if user_input in list1:

            indexes = [index for index, value in enumerate(list1) if value == user_input]
            for index in indexes:
            
                list_of[index] = list1[index]
                
            print("you guessed one symbol in word.\n")
            print(*list_of)
            
            
            if list_of == list1:
                print("\n...congrats you guessed word..\n")
                break
            
                    
        else:
                print("wrong symbol")
    i += 1
else:
    
    print("\nSorry you didnt guess the word\n")
    
print("...Game Over...")