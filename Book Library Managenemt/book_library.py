import json, os
from json import JSONEncoder
import time

class Books():
    book_id = 1
    def __init__(self, title=None, author=None, year=None):
        self.book_id = Books.book_id
        self.title = title
        self.author = author
        self.year = year
        
        Books.book_id += 1

class BookManager(Books):
    def __init__(self, title=None, author=None, year=None):
        super(). __init__(title, author, year)
        ...  

    # წიგნების დამატების ფუნქცია   
    def update_books(self,new_author=None, new_title=None, new_year=None):
        
        new_author = input("Enter author: ").title()
        new_title = input("Enter title: ").title()
        new_year = input("Enter issue year: ")
        self.new_author = new_author
        self.new_title = new_title
        self.new_year = new_year
        for id in result:
            next_id = id['book_id'] + 1
            
       
        book = {"book_id": next_id, "title": self.new_title, "author": self.new_author, "year": self.new_year}
        result.append(book)
        
        print("\nYour book is added in library...")

    # სრული სიის გამოტანის ფუნქცია
    def full_library():
            
            print('-'*100)
            print(f"\n{'ID':<5}{'Title':<36}{'Author':<23}{'Year'}")
            print('='*100)
            for i in result:
                print(f"{i['book_id']:<5}{i['title']:<35} {i['author']:<22} {i['year']}")


    #წიგნების საძიებო დასახელების მიხედვით
    def book_finder(self, finder=None):
        self.finder = finder
        finder = input("Enter book title you want to find: ").title()  
            
        for i in result:
            if finder == i['title']:
                print('-'*100)
                print(f"\n{'ID':<5}{'Title':<36}{'Author':<23}{'Year'}")
                print('='*100)
                print(f"{i['book_id']:<5}{i['title']:<35} {i['author']:<22} {i['year']}")
        print('-'*100)


class jsonencode(JSONEncoder):
    def default(self, o):
        return o.__dict__
   

# json ფაილში ჩაწერის ფუნქცია
def write_to_json_file(data):
    with open('data5.json', mode='w', encoding='utf-8') as file:
        json.dump(data, file, cls=jsonencode, indent=2)

# json ფაილიდან წაკითხვის ფუნქცია
def read_from_json_file():
    with open('data5.json', mode='r', encoding='utf8') as file:
        return json.load(file)
    


# წიგნების თავდაპირველი ბიბლიოთეკა, რომელიც იწერება ფაილში
books = [
        Books('Anna Karenina', 'Leo Tolstoy', 1887),
        Books('The Lord of the Rings', 'J. R. R. Tolkien', 1954),
        Books('David Copperfield', 'Charles Dickens', 1849),
        Books('Didostatis Marjvena', 'Konstantine Gamsaxurdia', 1939),
        Books('Kacia Adamiani?!', 'Ilia Chavchavadze', 1863),
        Books('All Quiet on the Western Front', 'Erich Maria Remarque', 1928),
        Books('Idiot', 'Fyodor Dostoevsky', 1869),
        Books('To Kill a Mockingbird', 'Harper Lee', 1960),
        Books('The Great Gatsby', 'F. Scott Fitzgerald', 1925),
]



json_filename = 'data5' + '.json'
    
# შემოწმება თუ უკვე არსებობს ფაილი
if not os.path.exists(json_filename):
    try:
        write_to_json_file(books)
       
        print(f"Data successfully saved as {json_filename}")
                
    except (TypeError, OverflowError) as json_err:
            print(f"JSON failed: {json_err}")
else:
    print(f"JSON file '{json_filename}' already exists. Skipping JSON write.")



result = read_from_json_file()  # ვიძახებთ ფაილიდან წაკითხვის ფუნქციას და ვინხავთ ცვლადში




# მომხმარებლის მიერ ბიბლიოთეკაზე განსახორციელებული ოპერაციები:
while True:
    time.sleep(1)
    print('''\n\nChoose action you want to do: 
    1) Type 'a' to add new book in library..
    2) Type 's' to search for book
    3) Type  'l' to see complate list of library 
    4) Type 'e' to Save and Exit        ''')
    print('-'*100,'\n')

    
    action_list = ['a', 'A', 's', 'S', 'l', 'L', 'e', 'E']  # სიმბოლოების სია რომელთა გამოყენებაა შესაძლებელი
    
    action = input("Type symbol: ").lower()

    if action  not in action_list:
            print("\n\nWrong command. Please type symbols from list:  ")
            continue
    else:

    
    
        # მომხმარებლის მიერ 'a' შეყვანისას იძახებს წიგნების დამატების ფუნქვიას
        if action == 'a':
                book1 = BookManager()
                book1.update_books()
                

            
        # მომხმარებლის მიერ 's' შეყვანისას იძახებს წიგნების ძებნის ფუნქციას
        elif action == 's':
                book2 = BookManager()
                book2.book_finder()


        # მომხმარებლის მიერ 'l' შეყვანისას იახებს სრული ბიბლიოთეკის გამოტანის ფუნქციას
        elif action == 'l':
                BookManager.full_library()


        # მომხმარებლის მიერ 'e' შეყვანისას ასრულებს პროგრამის მუშაობას
        elif action == 'e':
            print("Save and exit")
            write_to_json_file(result)
            break

