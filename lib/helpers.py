# lib/helpers.py
from models.collaborative_pianist import Collaborative_Pianist
from models.student import Student

def get_all_pianists_from_db():
    all_pianists = Collaborative_Pianist.get_all()
    print("\n+++ ALL COLLABORATIVE PIANISTS: +++ \n")
    for pianist in all_pianists:
        print(f"ID: {pianist.id} {pianist.name}")

def retrieve_pianist_by_id(pianist_id):
    found_pianist = Collaborative_Pianist.get_by_id(pianist_id)
    return found_pianist

def retrieve_pianist_by_name(name):
    found_pianist = Collaborative_Pianist.get_by_name(name)
    return found_pianist

def print_pianist_info(self):
    print(f"=====PIANIST INFO:=====")
    print(f"Name: {self.name}")
    print(f"Rank: {self.rank}")
    print(f"Email: {self.email}")
    print("=======================")

def delete_pianist(pianist_id):
    pianist_to_delete = retrieve_pianist_by_id(pianist_id)
    Collaborative_Pianist.delete_instance(pianist_to_delete)

def add_new_pianist():
    print("\n+++ ADD NEW PIANIST +++ \n")
    name = input("Enter pianist's name: ")
    rank = input("Enter pianist's rank (Faculty, TA, or Student): ")
    email = input("Enter pianist's email: ")
    Collaborative_Pianist.create(name, rank, email)

def get_assigned_students(self):
    print(f"\n+++ STUDENTS ASSIGNED TO {self.name.upper()}: +++ \n")
    assigned_students = Collaborative_Pianist.get_assigned_students(self.id)
    for student in assigned_students:
        print(student)
    print('------------------------------')

def get_all_students_from_db():
    all_students = Student.get_all()
    for student in all_students:
        print(f"ID: {student.id} {student.name} // {student.instrument} // {student.pianist_id}")

def retrieve_student_by_id(student_id):
    found_student = Student.get_by_id(student_id)
    return found_student

def delete_student(student_id):
    student_to_delete = retrieve_student_by_id(student_id)
    Student.delete_instance(student_to_delete)





def exit_program():
    print("Goodbye!")
    exit()
