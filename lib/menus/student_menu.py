from helpers import get_all_students_from_db

def student_menu():
    active = True
    while active:
        print("\n*** STUDENT MENU ***")
        print("What would you like to do?")
        print("1. Show all Students in the Database")
        print("2. Access Student by ID")
        print("3. Access Student by name")
        print("4. Delete Student From Database")
        choice = input(">> ")
        if choice == "1":
            get_all_students_from_db()
        if choice == "0":
            active = False