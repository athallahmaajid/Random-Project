import pickle
class todolist:
    def __init__(self, todo):
        self.todo = todo
    def create(self):
        thing = input("What do you want to add? ")
        self.todo.append(thing)
    def display(self):
        print("Your todo list:")
        for i in range(len(self.todo)):
            print(f"{i+1}. {self.todo[i]}")
    def delete(self):
        self.display()
        try:
            item_pos = int(input("which item number do you want to delete? "))
            del self.todo[item_pos-1]
            self.display()
        except:
            print("Invalid number to delete")
try:
    f = open("todolist.pickle", 'rb')
    my_list = todolist(pickle.load(f))
    f.close()
except:
    my_list = todolist([])
command = ""
while command != 'exit':
    command = input('''What Would you like to do?
                    C - create new item
                    V - Display to do list
                    D - delete existing item
                    exit - exit the program
''')
    if command == "C":
        my_list.create()
    elif command == "D":
        my_list.delete()
    elif command == "V":
        my_list.display()
    elif command == "exit":
        f = open("todolist.pickle", "wb")
        pickle.dump(my_list.todo, f)
        f.close()