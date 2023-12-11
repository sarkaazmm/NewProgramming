import csv
from worker_validation import *
from ClassWorker import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import simpledialog

def dec_search(search_func):
    def wrapper(self):
        field=simpledialog.askstring("","Enter the search fild: ")
        key=simpledialog.askstring("","Enter the search iformation: ")
        #print("Resulte where", field, " is ", key)
        search_func(self, field, key)
    return wrapper

def dec_sort(sort_func):
    def wrapper(self):
        field=simpledialog.askstring("","Enter the field by which the list will be sorted: ")
        sort_func(self, field)
        #print("Sorted by ", field, ": ")
        
    return wrapper

class CollectionWorker:
    def __init__(self):
        self.collection=[]

    def __iter__(self):
        return iter(self.collection)   

    def worker_db(self):
        filename='WorkersData.csv'
        with open(filename, newline='') as csv_file:
            reader=csv.DictReader(csv_file, delimiter=',')
            for row in reader:
                name, surname, depart, salary = row["name"], row["surname"], row["depart"], row["salary"]
                if(correct_input(name, letters_only, False) 
                   and correct_input(surname, letters_only, False)
                    and correct_input(depart, letters_only, False)
                    and correct_input(salary, digits_only, False)):
                    worker=Worker(name, surname, depart, salary)
                    self.collection.append(worker)

    def add_worker(self):
        worker = Worker()
        #worker.read_worker()
        worker.read_worker_from_window()
        self.collection.append(worker)
    
    def edit_worker(self):
        id=int(simpledialog.askstring("","Enter ID of worker u want be changed: "))
        field=simpledialog.askstring("","Enter field to change: ")
        value=simpledialog.askstring("","Enter new value: ")

        setters = {
            "name": lambda w, v: setattr(w, "name", v),
            "surname": lambda w, v: setattr(w, "surname", v),
            "depart": lambda w, v: setattr(w, "depart", v),
            "salary": lambda w, v: setattr(w, "salary", v),
        }

        for w in self.collection:
            if w.get_id() == id:
                setter = setters.get(field)
                if setter is not None:
                    setter(w, value)
                    return

    def delete_worker(self):
        #id=int(input("Enter ID of worker u want be deleted: "))
        id=int(simpledialog.askstring("","Enter ID of worker u want be deleted: "))
        for w in self.collection:
            if(w.get_id()==id):
                self.collection.remove(w)
                return
        simpledialog.messagebox.showinfo("Workers data base", "ID does NOT exist")     
        

    def desplay_collection(self):
        workers=""
        for worker in self.collection:
            workers+=str(worker)+"\n"
            #worker.desplay_worker()
        simpledialog.messagebox.showinfo("Workers data base", workers)

    def write_to_file(self):
        filename='result_file.csv'
        with open(filename, 'a', newline='') as csv_file:
            fieldnames = ["id", "name", "surname", "depart", "salary"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
            writer.writeheader()  
            
            for w in self.collection:
                writer.writerow({
                    "id": w.get_id(),
                    "name": w.get_name(),
                    "surname": w.get_surname(),
                    "depart": w.get_depart(),
                    "salary": w.get_salary()
                })

    def creat_diagram(self):
        departments={}
        for w in self.collection:
            depart = w.get_depart()
            departments[depart] = departments.get(depart, 0) + 1
        y = np.array([])
        labels = []
        for department, count in departments.items():
            y = np.append(y, count)
            labels.append(f"{department}: {count}")

        plt.pie(y, labels=labels)  
        plt.title('Distribution of elements by department')
        plt.pie(y)
        plt.show() 
    
    @dec_search
    def search_worker(self, field, key):
        getters = {
            "id": lambda w: w.id,
            "name": lambda w: w.name,
            "surname": lambda w: w.surname,
            "depart": lambda w: w.depart,
            "salary": lambda w: w.salary,
        }
        workers=""
            
        getter = getters.get(field)
        if getter is not None:
            for w in self.collection:
                if getter(w) == key:
                    workers+=str(w)+"\n"
                    simpledialog.messagebox.showinfo( f"Resulte where {field} is {key}", workers)
                    break
            if workers == "":
                simpledialog.messagebox.showinfo("Workers data base", "Element does NOT exist!") 
        else: simpledialog.messagebox.showinfo("Workers data base", "this field does NOT exist")
            #print("Element does NOT exist!")
        
    @dec_sort
    def sort_workers(self, field):
        getters = {
            "id": lambda w: w.id,
            "name": lambda w: w.name,
            "surname": lambda w: w.surname,
            "depart": lambda w: w.depart,
            "salary": lambda w: w.salary,
        }

        getter = getters.get(field)

        if getter is not None:
            self.collection.sort(key=getter)
        else: 
            simpledialog.messagebox.showinfo("Workers data base", "Invalid field for sorting")
            return
            #print("Invalid field for sorting")
        self.desplay_collection()
        

    



