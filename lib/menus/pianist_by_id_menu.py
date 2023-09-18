from helpers import retrieve_pianist_by_id, get_assigned_students, print_pianist_info, update_pianist_info, delete_pianist


def pianist_by_id_menu():
    active = True
    pianist_id = input("Enter the pianist's ID: ")

    found_pianist = retrieve_pianist_by_id(pianist_id)
    if found_pianist == None:
        active = False

    while active:
        print(f"\nPianist: {found_pianist.name.upper()}")
        print(f"What would you like to do with pianist {found_pianist.name}?")
        print(f"1. Show {found_pianist.name}'s info")
        print(f"2. Show all assigned students for {found_pianist.name}")
        print(f"3. Update {found_pianist.name}'s info")
        print(f"4. Delete {found_pianist.name}")
        print("0. Go back to Collaborative Pianists menu")

        choice = input(">> ")
        if choice == "1":
            print_pianist_info(found_pianist)
        elif choice == "2":
            get_assigned_students(found_pianist)
        elif choice == "3":
            update_pianist_info(found_pianist)
        elif choice == "4":
            delete_pianist(found_pianist.id)
            active = False
        elif choice == "0":
            active = False
        else:
            print("Invalid choice, please try again!")

