Todo=[] #sets the list
from pathlib import Path #impoorts the pathlib library in order to work with files and folders

def file_write(): #function that writes the list to a file
    p=Path("./Todolistfolder")
    with open(p/"Todolistfile.txt", "w") as f:
        for item in Todo:
            f.write(item + "\n")
    f.close()

def file_retrieval(): #function that retrieves the list from the file and creates it if it doesnt exist
    p = Path("./Todolistfolder")

    if not p.is_dir(): #checks wether the folder exists, and if it doesnt, it creates it based on user input
        print("it seems like you don't have a todo list yet, would you like to create one?")
        folder_creation_input = input("do you want to create the folder? y/n")
        while folder_creation_input not in ("y", "n", "Y", "N", "yes", "no", "YES", "NO"):
            print("invalid input, please enter y or n")
            folder_creation_input = input("do you want to create the folder? y/n")
        if folder_creation_input in ("y", "Y", "yes", "YES"):
            p.mkdir()
        else:
            print("file not created, exiting program")
            raise SystemExit
    file_path = p / "Todolistfile.txt"
    if not file_path.is_file():
        file_path.touch()  
    with open(file_path, "r") as f:
        return f.read().splitlines()
        
    
def task_add(): #function that adds tasks to the list until the user wants to stop
    add=input("Enter the task you want to add to your todo list: ")
    while add!="stop":
        Todo.append(add)
        add=input("Enter the task you want to add to your todo list: ")
     

def task_remove(): #function removes tasks from the list
     remove=input("enter which task you want to remove(1-n): ")
     while remove!="stop":
        if not remove.isdigit():
             print("invalid input, please enter a number corresponding to the task you want to remove or stop to exit")
             while not remove.isdigit() and remove!="stop":
                   remove=input("enter which task you want to remove(1-n): ")
        elif remove.isdigit():
                remove=int(remove)
                if 1<=remove<= (len(Todo)):
                    Todo.pop(remove-1)
                remove=input("enter which task you want to remove(1-n): ")
     

Todo=file_retrieval() #the base program 
print("Welcome to your todo list! Your current todo list is: ",Todo)
print("To add a task, enter 'add'. To remove a task, enter 'remove'. To show the todo list, enter 'show'. To exit the program, enter 'exit'.")
print("Note: when adding or removing tasks, enter 'stop' to stop adding or removing tasks and return to the main menu.")
command_pr=input("enter first command: ")
while True:
     if command_pr in ("add", "remove", "show", "exit"):
        if command_pr!="show":
                print("Your todo list is: ",Todo)
        if command_pr=="add":
           task_add()
        elif command_pr=="remove":
              task_remove()
        elif command_pr=="exit":
             print("Your final todo list is: ",Todo)
             final=input("are you sure? y/n:")
             if final in ("y", "Y", "yes", "YES"):
                 file_write()
                 raise SystemExit
             elif final =="n":
                 print("Your todo list is: ",Todo)
        elif command_pr=="show":
             print("Your todo list is: ",Todo)
        command_pr=input("enter next command: ") 
     else:
        print("invalid command, please enter add, remove, show, or exit")
        command_pr=input("enter next command: ")         
