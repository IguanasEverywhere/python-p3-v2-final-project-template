from helpers import retrieve_student_by_id

def student_by_id_menu():
    print("Enter the student ID: ")
    student_id = input(">> ")
    found_student = retrieve_student_by_id(student_id)

    active = True
    while active:
        print(f"What would you like to do with {found_student.name}? ")
        print(f"1. Update {found_student.name}'s Info")
        print(f"2. Retrieve {found_student.name}'s assigned collaborative pianist")
        print(f"3. Delete {found_student.name} from the database")
        print("0. Go back to Student Menu")

        choice = input(">> ")
        if choice == "1":
            print("Do update work here")
        elif choice == "2":
            print("Do retrieve pianist work here")
        elif choice == "3":
            print("Do delete work here")
        elif choice == "0":
            active = False

