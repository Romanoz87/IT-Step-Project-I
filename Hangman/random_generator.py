import random

def random_word():
# List of items
    items = ['brazil', 'canada', 'georgia', 'japan']

    # Select a random item
    return random.choice(items)
    
selected_item = random_word()

def question():
   
    if selected_item == 'brzil':
        print("Which country's flag depicts the earth?")
    elif selected_item == 'canada':
        print("Which country's flag features a leaf?")
    elif selected_item == 'georgia':
        print("Which country's flag has five crosses on it?")
    elif selected_item == 'japan':
        print("Which country's flag depicts the sun?")


       
        