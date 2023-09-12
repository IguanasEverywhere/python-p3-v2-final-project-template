# lib/cli.py

from helpers import (
    exit_program,
    get_all_pianists_from_db,
    retrieve_pianist_by_id,
    retrieve_pianist_by_name
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
        print("\n*** COLLABORATIVE PIANIST MENU ***")
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
        elif choice == "3":
            pianist_by_name_menu()
        elif choice == "0":
            active = False

def pianist_by_id_menu():

    pianist_id = input("Enter the pianist's ID: ")
    found_pianist = retrieve_pianist_by_id(pianist_id)

    active = True
    while active:
        print(f"\nPianist: {found_pianist.name.upper()}")
        print(f"What would you like to do with pianist {found_pianist.name}?")
        print(f"1. Show {found_pianist.name}'s info")
        print(f"2. Show all assigned students for {found_pianist.name}")
        print("0. Go back to Collaborative Pianists menu")

        choice = input(">> ")
        if choice == "0":
            active = False

def pianist_by_name_menu():
    # Refactor this with id into one fn?
    name = input("Enter the pianist's name: ")
    found_pianist = retrieve_pianist_by_name(name)

    active = True
    while active:
        print(f"\nPianist: {found_pianist.name.upper()}")
        print(f"What would you like to do with pianist {found_pianist.name}?")
        print(f"1. Show {found_pianist.name}'s info")
        print(f"2. Show all assigned students for {found_pianist.name}")
        print("0. Go back to Collaborative Pianists menu")

        choice = input(">> ")
        if choice == "0":
            active = False

def student_menu():
    active = True
    while active:
        print("Student options...")
        choice = input(">> ")
        if choice == "0":
            active = False

def menu():
    print("\n*** MAIN MENU ***")
    print("What data you like to access? Select an option from below: ")
    print("1. Collaborative Pianists")
    print("2. Students")
    print("0. Exit the program")



if __name__ == "__main__":
    main()
