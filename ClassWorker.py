import csv
from worker_validation import *
id_count=0


def id_generator():
    for i in range(100):
        yield i

def correct_input(variable, ckeck_funk, data_enterence=True):
    if data_enterence:
        while(ckeck_funk(variable) == False):
            variable=input("Enter proper data: ")
        return variable
    else:
        return ckeck_funk(variable)

class Worker:
    id=id_generator()
    def __init__(self, name="", surname="", depart="", salary="" ):
        self.set_id(next(self.id))
        self.name=name
        self.surname=surname
        self.depart=depart
        self.salary=salary

    def __str__(self):
        return(f"{self.name} {self.surname}, {self.depart}, {self.salary}")
    
    def set_id(self, id): self.__ID=id
    def get_id(self): return self.__ID

    def set_name(self, name): self.name=name
    def get_name(self): return self.name

    def set_surname(self, surname): self.surname=surname
    def get_surname(self): return self.surname

    def set_depart(self, depart): self.depart=depart
    def get_depart(self): return self.depart

    def set_salary(self, salary): self.salary=salary
    def get_salary(self): return self.salary


    def read_worker(self):
        self.name = correct_input(input("name: "), letters_only)
        self.surname = correct_input(input("surname: "), letters_only)
        self.depart = correct_input(input("depart: "), letters_only)
        self.salary = correct_input(input("salary: "), digits_only)

    def desplay_worker(self):
        print(
            "ID:", self.get_id(), "\n",
            "name:", self.name, "\n",
            "surname:", self.surname,"\n",
            "department:", self.depart,"\n",
            "salary:", self.salary, "\n"
        )