import time
#initialize the library
library = { 
    "python" : "Electrical" ,
    "java" : "Cs"
}
total = int(len(library))
print(total)
#we divided into two parts first is for librarian that manage this library
#second for student that take bhooks from library
#first part for librarian
def add_bhooks(name , department):
    library[name] = department

def del_bhook(name):
    if name in library:
        del library[name]
    else:
        print("This bhook is not present in library")
def view_all():
    for name , department in library.items():
        print(f"{name} : {department}")

def main():
    while True:
        print("\n\n Welcome to the Library of Uet Narowal \n\n")
        print("Choose 1 if you are Student ")
        print("choose 2 if your are a librarian")
        print("choose option 3 for Exit the library")
        choice_studentorLibrarian = int(input("Select the Above option "))
        if choice_studentorLibrarian == 1:
            print("1. View all the Bhooks ")
            print("2. Take the Bhooks ")
            print("3. Return the Bhooks")
            choice = int(input("Enter the Choice = "))
            if choice == 1:
                view_all()
            elif choice == 2:
                print("You want to return the bhooks within 10 days")
                bhooks_take = input("Enter the name of bhooks that you want to take = ")
                if bhooks_take in library:
                    print("we issue this bhook for you ")
                    del_bhook(bhooks_take)
                else:
                    print("This bhook is not available yet")
            elif choice == 3 :
                name = input("Enter the name of bhooks that you want to return")
                department = input("Enter the department = ")
                add_bhooks(name , department)
        elif choice_studentorLibrarian == 2:
            print("1. Add new Bhooks in library")
            print("2. Remove the old version Bhooks")
            man = int(input("Enter the chooice ="))
            if man == 1 :
                name = input("Enter the name of bhooks that you want to add = ")
                department = input("Enter the department = ")
                add_bhooks(name , department)
            elif man == 2 :
                name = input("Enter the name of bhooks that you want to remove = ")
                if bhooks_take in library:
                    del_bhook(bhooks_take)
                    print("This bhook is succesfully remove")
                else:
                    print("This bhook is not present")
        if choice_studentorLibrarian == 3:
            time.sleep(3)
            print("Thanks for using this system")
            break
 
main()