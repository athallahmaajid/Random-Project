import pickle
def create(todolist):
    thing = input("What do you want to add? ")
    todolist.append(thing)
def display(todolist):
    print("Your todo list:")
    for i in range(len(todolist)):
        print(f"{i+1}. {todolist[i]}")
def delete(todolist):
    display(todolist)
    try:
        item_pos = int(input("which item number do you want to delete? "))
        del todolist[item_pos-1]
        display(todolist)
    except:
        print("Invalid number to delete")
try:
    f = open("todolist.pickle", 'rb')
    my_list = pickle.load(f)
    f.close()
except:
    my_list = []
command = ""
while command != 'exit':
    command = input('''What Would you like to do?
                    C - create new item
                    V - Display to do list
                    D - delete existing item
                    exit - exit the program
''')
    if command == "C":
        create(my_list)
    elif command == "D":
        delete(my_list)
    elif command == "V":
        display(my_list)
    elif command == "exit":
        f = open("todolist.pickle", "wb")
        pickle.dump(my_list, f)
        f.close()