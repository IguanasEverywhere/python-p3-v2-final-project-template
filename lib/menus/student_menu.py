from helpers import get_all_students_from_db, add_new_student, unassigned_students
from menus.student_by_id_menu import student_by_id_menu

def student_menu():
    active = True
    while active:
        print("\n===================================")
        print("\n*** STUDENT MENU ***")
        print("\n===================================")
        print("What would you like to do?")
        print("1. Show all Students in the Database")
        print("2. Access Student by ID")
        print("3. Add a new student to the database")
        print("4. Show all students without an assigned pianist")
        print("0. Go Back to Main Menu")
        choice = input(">> ")
        if choice == "1":
            get_all_students_from_db()
        elif choice == "2":
            student_by_id_menu()
        elif choice == "3":
            add_new_student()
        elif choice == "4":
            unassigned_students()
        elif choice == "0":
            active = False
        else:
            print("\nInvald choice, please try again!")