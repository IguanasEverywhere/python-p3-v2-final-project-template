from helpers import get_all_pianists_from_db
from menus.pianist_by_id_menu import pianist_by_id_menu
from menus.pianist_by_name_menu import pianist_by_name_menu

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