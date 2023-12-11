import os

def letters_only(word):
    try: 
        for w in word:
            if w.isdigit(): return False
        return True
    except ValueError:
        print("letters only!")

def digits_only(number):
    try:
        for n in number:
            if not n.isdigit(): return False
        return True
    except ValueError:
        print("digits only!")

def file_existence(filename):
        return os.path.exists(filename)

    