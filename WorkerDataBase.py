import csv
from worker_validation import *
from ClassWorker import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import simpledialog

def dec_search(search_func):
    def wrapper(*args, **kwargs):
        instance, fild, key = args
        print("Resulte where", fild, " is ", key)
        search_func(*args, **kwargs)
    return wrapper

def dec_sort(sort_func):
    def wrapper(*args, **kwargs):
        instance, fild = args
        print("Sorted by ", fild, ": ")
        sort_func(*args, **kwargs)
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
        worker.read_worker()
        self.collection.append(worker)
    
    def edit_worker(self):
        id=int(input("Enter ID of worker u want be changed: "))
        field=input("Enter field to change: ")
        value=input("Enter new value: ")

        setters = {
            "id": lambda w, v: setattr(w, "id", v),
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
        id=int(input("Enter ID of worker u want be deleted: "))
        for w in self.collection:
            if(w.get_id()==id):
                self.collection.remove(w)

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
    def search_worker(self):
        field=input("Enter the search fild: ")
        key=input("Enter the search iformation: ")
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
                    w.desplay_worker()     
            simpledialog.messagebox.showinfo("Workers data base", workers)
        else: print("Element does NOT exist!")

    @dec_sort
    def sort_workers(self):
        field=input("Enter the field by which the list will be sorted: ")
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
            return
        print("Invalid field for sorting")
        

    



