import json
import os
from json import JSONEncoder
import time

# Function to read the dictionary file
def read_file():
    with open('dictionary.json', mode='r', encoding='utf-8') as file:
        return json.load(file)
    
# Function to write the dictionary file
def write_file(data):
    with open('dictionary.json', mode='w', encoding='utf-8') as file:
        json.dump(data, file, cls=encode_json, indent=2)

# Custom encoder class
class encode_json(JSONEncoder):
    def default(self, o):
        return o.__dict__

# Sample dictionary data
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

# Check if the file exists and write initial data if not
if not os.path.exists('dictionary.json'):
    try:
        write_file(dictionary)
    except Exception as e:
        print(f"Failed to write JSON: {e}")
else:
    print("json already exists")

# Load the dictionary from the file
result_json = read_file()

# Main program logic
action = ["1", "2", "x"]

while True:
    time.sleep(1)
    print("-" * 50)
    print("Choose dictionary type (აირჩიეთ ლექსიკონის ტიპი)\n")
    print("1)English-Georgian - ინგლისურ-ქართული ლექსიკონი")
    print("2)Georgian-English - ქართულ-ინგლისური ლექსიკონი")
    
    print("3)exit - გასასვლა >>")
    print("=" * 50)

    choose_action = input("Choose 1, 2 or '3':\nაარჩიეთ 1, 2 ან '3':\n:_ ").strip()

    if choose_action in action:
        if choose_action == '1':
            eng_input = input('Enter English word - შეიყვანე ინგლისური სიტყვა: ').strip().lower()
            found = False
            for book in result_json:
                if eng_input == book['eng'].strip().lower():
                    print("-"*50, f"\n{book['eng']}: {book['geo']}\n")
                    found = True
                    break

            if not found:
                print("word not found. do you want to add it to dictionary? press Y/N ")
                add = input("_").strip().lower()
                if add == 'y':
                    eng_word = input("Input English word to add in library: ").strip()
                    ge_word = input("Input Georgian translation: ").strip()
                    new_data = {'eng': eng_word, 'geo': ge_word}
                    result_json.append(new_data)
                    write_file(result_json)
                    print(f"New word '{eng_word}' added to dictionary.")
                elif add == 'n':
                    print("No word added.")
        
        elif choose_action == '2':
            geo_input = input('შეიყვანე ქართული სიტყვა: ').strip()
            found = False
            for book in result_json:
                if geo_input == book['geo'].strip():
                    print(f"{book['geo']}: {book['eng']}")
                    found = True
                    break

            if not found:
                 if not found:
                    print("word not found. do you want to add it to dictionary? press Y/N ")
                    add = input("_").strip().lower()
                    if add == 'y':
                        ge_word = input("Input Georgian word to add in library: ").strip()
                        eng_word = input("Input English translation: ").strip()
                        
                        new_data = {'eng': eng_word, 'geo': ge_word}
                        result_json.append(new_data)
                        write_file(result_json)
                        print(f"New word '{ge_word}' added to dictionary.")
                    elif add == 'n':
                        print("No word added.")
        
        elif choose_action == '3':
            print('exit..>>\nგასვლა..>>')
            break
    else:
        print("Wrong action input. Please choose '1', '2' or '3'.")
