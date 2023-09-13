from helpers import delete_pianist

def delete_pianist_menu():
    print("Enter the ID of the pianist you wish to delete: ")
    pianist_id = input(">> ")
    delete_pianist(pianist_id)
