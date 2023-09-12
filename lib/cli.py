# lib/cli.py

from helpers import (
    exit_program,
    get_all_pianists_from_db,
    retrieve_pianist_by_id
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            pianist_menu()
        elif choice == "2":
            student_menu()
        else:
            print("Invalid choice")

def pianist_menu():
    active = True
    while active:
        print("\nCOLLABORATIVE PIANIST MENU")
        print("What would you like to do?")
        print("1. Show all Collaborative Pianists in the database")
        print("2. Access Collaborative Pianist by ID")
        print("3. Access Collaborative Pianist by name")
        print("0. Back to Main Menu")
        choice = input(">> ")
        if choice == "1":
            get_all_pianists_from_db()
        elif choice == "2":
            pianist_by_id_menu()
        elif choice == "0":
            active = False

def pianist_by_id_menu():

    pianist_id = input("Enter the pianist's ID: ")
    retrieve_pianist_by_id(pianist_id)


    print("specific pianist menu")

def student_menu():
    active = True
    while active:
        print("Student options...")
        choice = input(">> ")
        if choice == "0":
            active = False

def menu():
    print("\nWhat data you like to access? Select an option from below: ")
    print("1. Collaborative Pianists")
    print("2. Students")
    print("0. Exit the program")



if __name__ == "__main__":
    main()
