from helpers import delete_student

def delete_student_menu():
    print("Enter the ID of the student you wish to delete: ")
    student_id = input(">> ")
    delete_student(student_id)

