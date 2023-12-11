import os
import tkinter as tk
from tkinter import simpledialog

def letters_only(word):
    try: 
        for w in word:
            if w.isdigit(): 
                simpledialog.messagebox.showinfo("Error type", "letters only!")
                return False
        return True
    except ValueError:
        simpledialog.messagebox.showinfo("Error type", "letters only!")
        #print("letters only!")

def digits_only(number):
    try:
        for n in number:
            if not n.isdigit(): 
                simpledialog.messagebox.showinfo("Error type", "digits only!")
                return False
        return True
    except ValueError:
        simpledialog.messagebox.showinfo("Error type", "digits only!")
        #print("digits only!")

def file_existence(filename):
        return os.path.exists(filename)

    