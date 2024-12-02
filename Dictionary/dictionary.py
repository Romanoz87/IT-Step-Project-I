import json, re
import os
from json import JSONEncoder
import time

# ფაილიდან წაკითხვის ფუნქცია
def read_file():
    with open('dictionary.json', mode='r', encoding='utf-8') as file:
        return json.load(file)
#======================================================================================================
   

# ფაილის ჩამწერი ფუნქცია
def write_file(data):
    with open('dictionary.json', mode='w', encoding='utf-8') as file:
        json.dump(data, file, cls=encode_json, indent=2)
#======================================================================================================


# ვალიდაციის ფუნქცია ქართული სიტყვებისთვის
def is_georgian(text):
    
    return bool(re.match(r'^[\u10A0-\u10FF]+$', text))
#======================================================================================================



# ვალიდაციის ფუნქცია ინგლისური სიტყვებისთვის
def is_english(text):
    
    return bool(re.match(r'^[a-zA-Z\s]+$', text))
#======================================================================================================



# ენკოდერი
class encode_json(JSONEncoder):
    def default(self, o):
        return o.__dict__
#======================================================================================================    

# ლექსიკონის საწყისი ბაზა
dictionary = [
    {"eng": "country", "geo": "ქვეყანა"},
    {"eng": "city", "geo": "ქალაქი"},
    {"eng": "birthday", "geo": "დაბადების დღე"},
    {"eng": "brother", "geo": "ძმა"},
    {"eng": "game", "geo": "თამაში"},
    {"eng": "sister", "geo": "და"},
    {"eng": "mother", "geo": "დედა"},
    {"eng": "father", "geo": "მამა"},
    {"eng": "book", "geo": "წიგნი"},
]

#======================================================================================================
#  ფაილის ვალიდურობის შემოწმება, თუ უკვე არსებობს, არ გადაეწერება
if not os.path.exists('dictionary.json'):
    try:
        write_file(dictionary)
    except Exception as e:
        print(f"Failed to write JSON: {e}")
else:
    print("json already exists")
#======================================================================================================

# ფაილიდან ვტვირთავთ მონაცემებს
result_json = read_file()

#======================================================================================================

# ძირითადი მოქმედებები
action = ["1", "2", "3"]
print("=" * 55)
print("(ინგლისურ - ქართული) და (ქართულ - ინგლისური) ლექსიკონი")
print("(English - Georgian) and (Georgian - English) dictionary")
print("=" * 55)
#------------------------------------------------------------------------------------------------------
while True:             
    time.sleep(1)
    print("-" * 55)
    print("Choose dictionary type (აირჩიეთ ლექსიკონის ტიპი)\n")
    print("1)English-Georgian - ინგლისურ-ქართული ლექსიკონი")
    print("2)Georgian-English - ქართულ-ინგლისური ლექსიკონი")
    
    print("3)exit - გასასვლა >>")
    print("=" * 55)

    choose_action = input("Choose 1, 2 or '3':\nაარჩიეთ 1, 2 ან '3':\n:_ ").strip()

    if choose_action in action:
# ინგლისურ - ქართილი ლექსიკონის ბლოკი__________________________________________________________________
        if choose_action == '1':
            # ვახდენთ ვალიდაციას, რომ მომხმარებელმა შეიყვანოს სიტყვა ინგლისურ ენაზე      
            while True:
                eng_input = input('Enter English word - შეიყვანე ინგლისური სიტყვა: ').strip().lower()
                if not is_english(eng_input):
                    print("Invalid English input. Please enter a word in English.")
                    print("უნდა შეიყვანოთ ლათინური სიმბოლოები.")
                else:
                    break
            found = False
            for book in result_json:
                if eng_input == book['eng'].strip().lower():
                    print("-"*55, f"\n{book['eng']}: {book['geo']}\n")
                    found = True
                    break

            if not found:
                print("word not found. do you want to add it to dictionary? press Y/N ")
                print("სიტყვა ვერ მოიძებნა. დასამატებლად აარჩიეთ Y/N ")
                add = input("_").strip().lower()

                if add == 'y' or add == 'ყ':
                    # ვახდენთ ვალიდაციას, რომ მომხმარებელმა შეიყვანოს სიტყვა ინგლისურ ენაზე
                    while True: 
                        eng_word = input("Input English word to add in library - შეიყვანეთ ინგლისური სიტყვა რათა დავამატოთ ლექსიკონში: ").lower().strip()
                        if not is_english(eng_word):
                            print("Invalid English input. Please enter a word in English.")
                            print("უნდა შეიყვანოთ ლათინური სიმბოლოები.")
                        else:
                            break
                                
                    # ვახდენთ ვალიდაციას, რომ მომხმარებელმა შეიყვანოს სიტყვა ქართულ ენაზე      
                    while True:
                        ge_word = input("Input Georgian translation - შეიყვანეთ ქართული თარგმანი: ").lower().strip()

                        if is_georgian(ge_word):
                            new_data = {'eng': eng_word, 'geo': ge_word}
                            result_json.append(new_data)
                            write_file(result_json)
                            print(f"New word '{eng_word}' added to dictionary.")
                            print(f"ახალი სიტყვა '{eng_word}' დაემატა ბიბლიოთეკაში.")
                            break
                        else:
                            print("Invalid Georgian input. Please enter a word in Georgian.")
                            print("უნდა შეიყვანოთ ქართული სიმბოლოები.")
                            

                        
                elif add == 'n':
                    print("Deny - უარყოფა")
                    break
                else:
                    print("Deny - უარყოფა")
                    break

# ქართულ-ინგლისური ლექსიკონის ბლოკი__________________________________________________________________
       
        elif choose_action == '2':
            # ვახდენთ ვალიდაციას, რომ მომხმარებელმა შეიყვანოს სიტყვა ქართულ ენაზე      
            while True:
                geo_input = input('Enter Georgian word - შეიყვანე ქართული სიტყვა: ').lower().strip()               
                if not is_georgian(geo_input):
                    print("Invalid Georgian input. Please enter a word in Georgian.")
                    print("უნდა შეიყვანოთ ქართული სიმბოლოები.")
                else:
                    break

            found = False
            for book in result_json:
                if geo_input == book['geo'].strip():
                    print(f"{book['geo']}: {book['eng']}")
                    found = True
                    break

            if not found:
                 if not found:
                    print("word not found. do you want to add it to dictionary? press Y/N ")
                    print("სიტყვა ვერ მოიძებნა. დასამატებლად აარჩიეთ Y/N ")
                    add = input("_").strip().lower()
                    if add == 'y' or add == 'ყ':

                        # ვახდენთ ვალიდაციას, რომ მომხმარებელმა შეიყვანოს სიტყვა ქართულ ენაზე
                        while True:
                            ge_word = input("Input Georgian word to add in library - შეიყვანეთ ქართული სიტყვა რათა დავამატოთ ლექსიკონში: ").lower().strip()
                            if not is_georgian(ge_word):
                                print("Invalid Georgian input. Please enter a word in Georgian.")
                                print("უნდა შეიყვანოთ ქართული სიმბოლოები.")
                            else:
                                break

                        # ვახდენთ ვალიდაციას, რომ მომხმარებელმა შეიყვანოს სიტყვა ინგლისურ ენაზე        
                        while True:
                            eng_word = input("Input English translation - შეიყვანეთ ინგლისური თარგმანი ").lower().strip()
                            if is_english(eng_word):
                                new_data = {'eng': eng_word, 'geo': ge_word}
                                result_json.append(new_data)
                                write_file(result_json)
                                print(f"New word '{eng_word}' added to dictionary.")
                                print(f"ახალი სიტყვა '{eng_word}' დაემატა ბიბლიოთეკაში.")
                                break
                            else:
                                print("Invalid Georgian input. Please enter a word in English.")
                                print("უნდა შეიყვანოთ ლათინური სიმბოლოები.")

                    elif add == 'n':
                        print("Deny - უარყოფა")
                        break   
                    else:
                        print("Deny - უარყოფა")
                        break
        
        elif choose_action == '3':
            print('exit..>>\nგასვლა..>>')
            break

    else:
        print("Wrong action input. Please choose '1', '2' or '3'.")
        print("არასწორი ბრძანება, აარჩიეთ '1', '2', ან '3'.")
