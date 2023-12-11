from WorkerDataBase import *
import matplotlib.pyplot as plt
import tkinter as tk

def main():
    collection = CollectionWorker()
    root = tk.Tk()
    menu = WorkerMenu(root, collection)

class WorkerMenu:
    def __init__(self, root, collection):
        self.collection = collection
        self.root=root
        self.button_generator()
        self.output_label = tk.Label(self.root)
        self.root.title("Worker")
        self.output_label.pack()
        self.root.mainloop()

    def button_generator(self):
        buttons={
            "Read workers": self.collection.worker_db,
            "Display workers": self.collection.desplay_collection,
            "Add worker": self.collection.add_worker,
            "Edit worker": self.collection.edit_worker,
            "Delete worker": self.collection.delete_worker,
            "Find worker": self.collection.search_worker,
            "Sort workers": self.collection.sort_workers,
            "Display diagram": self.collection.creat_diagram,
            "End prodram": exit
        }
        
        for key in buttons.keys():
            but = tk.Button(self.root, text = key, command=buttons[key])
            but.pack()



if __name__ == "__main__":
    main()
        

#     collection = CollectionWorker()

#     #filename=correct_input(input("Enter name of the file: "), file_existence )
#     collection.worker_db()   
#     choice=1
#     while(choice!="0"):
#         print("1 - add worker","\n",
#             "2 - edit worker", "\n",
#             "3 - delete worker", "\n",
#             "4 - desplay list of workers", "\n",
#             "5 - write list to file", "\n",
#             "6 - find the element", "\n",
#             "7 - sort the list by field", "\n",
#             "0 - exit", "\n")
#         choice=input("Enter your choice: ")
#         if(choice=="1"):
#             collection.add_worker()
#         elif(choice=="2"):
#             collection.edit_worker()
#         elif(choice=="3"):
#             collection.delete_worker(id)
#         elif(choice=="4"):
#             collection.desplay_collection()     
#         elif(choice=="5"):
#             collection.write_to_file()
#         elif(choice=="6"): 
#             collection.search_worker()
#         elif(choice=="7"):
#             collection.sort_workers()
#             collection.desplay_collection()
#         elif(choice=="8"):
#             collection.creat_diagram()    