from helpers import retrieve_student_by_id, print_student_info, retrieve_assigned_pianist_for_student, update_student_info, delete_student

def student_by_id_menu():
    active = True
    print("Enter the student ID: ")
    student_id = input(">> ")

    found_student = retrieve_student_by_id(student_id)
    if found_student == None:
        active = False


    while active:
        print(f"\nStudent: {found_student.name.upper()}")
        print(f"What would you like to do with {found_student.name}? ")
        print(f"1. Show {found_student.name}'s Info")
        print(f"2. Show {found_student.name}'s assigned collaborative pianist")
        print(f"3. Update {found_student.name}'s info")
        print(f"4. Delete {found_student.name}")
        print("0. Go back to Student Menu")

        choice = input(">> ")
        if choice == "1":
            print_student_info(found_student)
        elif choice == "2":
            retrieve_assigned_pianist_for_student(found_student)
        elif choice == "3":
            update_student_info(found_student)
            # is there a better solution?
            active = False
        elif choice == "4":
            delete_student(found_student.id)
            active = False
        elif choice == "0":
            active = False
        else:
            print("Invalid choice, please try again!")

