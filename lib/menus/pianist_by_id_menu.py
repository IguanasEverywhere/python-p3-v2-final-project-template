from helpers import retrieve_pianist_by_id

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