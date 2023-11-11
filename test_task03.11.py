import csv
id_count=0
class Worker:
    def __init__(self, name="", surname="", depart="", salary="" ):
        global id_count
        id_count=id_count+1
        ID=id_count
        self.set_id(ID)
        self.name=name
        self.surname=surname
        self.depart=depart
        self.salary=salary
    
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
        self.name = input("name: ")
        self.surname = input("surname: ")
        self.depart = input("depart: ")
        self.salary = input("salary: ")


    def desplay_worker(self):
        print(
            "ID:", self.get_id(), "\n",
            "name:", self.name, "\n",
            "surname:", self.surname,"\n",
            "department:", self.depart,"\n",
            "salary:", self.salary, "\n"
        )

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

    def worler_db(self, filename):
        with open(filename, newline='') as csv_file:
            reader=csv.DictReader(csv_file, delimiter=',')
            for row in reader:
                name, surname, depart, salary = row["name"], row["surname"], row["depart"], row["salary"]
                worker=Worker(name, surname, depart, salary)
                self.collection.append(worker)

    def add_worker(self):
        worker = Worker()
        worker.read_worker()
        self.collection.append(worker)
    
    def edit_worker(self, id):
        for w in self.collection:
            if(w.get_id()==id):
                print(
                "1 - edit name", "\n",
                "2 - edit surname","\n",
                "3 - edit department", "\n",
                "4 - edit salary", "\n")
                choice=int(input("Enter your choice: "))
                if(choice==1):
                    n_name=input("Enter new name: ")
                    w.set_name(n_name)
                elif(choice==2):
                    n_surname=input("Enter new surname: ")
                    w.set_surname(n_surname)
                elif(choice==3):
                    n_depart=input("Enter new depart: ")
                    w.set_depart(n_depart)
                elif(choice==4):
                    n_salary=input("Enter new name: ")
                    w.set_salary(n_salary)

    def delete_worker(self, id):
        for w in self.collection:
            if(w.get_id()==id):
                self.collection.remove(w)

    def desplay_collection(self):
        for worker in self.collection:
            worker.desplay_worker()

    def write_to_file(self, filename):
        with open(filename, 'w', newline='') as csv_file:
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
    
    @dec_search
    def search_worker(self, field, key):
        getters = {
            "id": lambda w: w.id,
            "name": lambda w: w.name,
            "surname": lambda w: w.surname,
            "depart": lambda w: w.depart,
            "salary": lambda w: w.salary,
        }

        getter = getters.get(field)
        if getter is not None:
            for w in self.collection:
                if getter(w) == key:
                    w.desplay_worker()
            return
       
        else: print("Element does NOT exist!")

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
            return

        print("Invalid field for sorting")
        
def main():
    filename = 'DataBase_test_task03.11.csv'
    collection = CollectionWorker()
    
    choice=input("Pres 1 to read list of workers from file: ")
    collection.worler_db(filename)   

    while(choice!="0"):
        print("1 - add worker","\n",
            "2 - edit worker", "\n",
            "3 - delete worker", "\n",
            "4 - desplay list of workers", "\n",
            "5 - write list to file", "\n",
            "6 - find the element", "\n",
            "7 - sort the list by field", "\n",
            "0 - exit", "\n")
        choice=input("Enter your choice: ")
        if(choice=="1"):
            collection.add_worker()
        elif(choice=="2"):
            id=int(input("Enter ID of worker u want be changed: "))
            collection.edit_worker(id)
        elif(choice=="3"):
            id=int(input("Enter ID of worker u want be deleted: "))
            collection.delete_worker(id)
        elif(choice=="4"):
            collection.desplay_collection()     
        elif(choice=="5"):
            collection.write_to_file('result_file.csv')
        elif(choice=="6"): 
            field=input("Enter the search fild: ")
            key=input("Enter the search iformation: ")
            collection.search_worker(field, key)
        elif(choice=="7"):
            field=input("Enter the field by which the list will be sorted: ")
            collection.sort_workers("name")
            collection.desplay_collection()


if __name__ == "__main__":
    main()
        

    



