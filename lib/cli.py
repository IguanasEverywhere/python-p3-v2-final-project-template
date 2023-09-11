# lib/cli.py

from helpers import (
    exit_program,
    helper_1
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
        print("Pianist options...")
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
    print("Please select an option:")
    print("1. Pianist Menu")
    print("2. Student Menu")
    print("0. Exit the program")



if __name__ == "__main__":
    main()
