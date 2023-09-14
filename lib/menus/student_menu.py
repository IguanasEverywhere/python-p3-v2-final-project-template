from helpers import get_all_students_from_db
from menus.student_by_id_menu import student_by_id_menu
from menus.delete_student_menu import delete_student_menu

def student_menu():
    active = True
    while active:
        print("\n===================================")
        print("\n*** STUDENT MENU ***")
        print("\n===================================")
        print("What would you like to do?")
        print("1. Show all Students in the Database")
        print("2. Access Student by ID")
        print("3. Access Student by name")
        print("4. Delete Student From Database")
        print("0. Go Back to Main Menu")
        choice = input(">> ")
        if choice == "1":
            get_all_students_from_db()
        elif choice == "2":
            student_by_id_menu()
        elif choice == "4":
            delete_student_menu()
        elif choice == "0":
            active = False