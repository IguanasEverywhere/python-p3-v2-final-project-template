# lib/cli.py
from menus.main_menu import menu
from menus.pianist_menu import pianist_menu
from menus.student_menu import student_menu

from helpers import (
    exit_program,
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


if __name__ == "__main__":
    main()
