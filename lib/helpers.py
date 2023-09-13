# lib/helpers.py
from models.collaborative_pianist import Collaborative_Pianist
from models.student import Student

def get_all_pianists_from_db():
    all_pianists = Collaborative_Pianist.get_all()
    for pianist in all_pianists:
        print(f"ID: {pianist.id} {pianist.name} // {pianist.rank} // {pianist.email}")

def retrieve_pianist_by_id(pianist_id):
    found_pianist = Collaborative_Pianist.get_by_id(pianist_id)
    return found_pianist

def retrieve_pianist_by_name(name):
    found_pianist = Collaborative_Pianist.get_by_name(name)
    return found_pianist

def delete_pianist(pianist_id):
    pianist_to_delete = retrieve_pianist_by_id(pianist_id)
    Collaborative_Pianist.delete_instance(pianist_to_delete)

def get_all_students_from_db():
    all_students = Student.get_all()
    for student in all_students:
        print(f"ID: {student.id} {student.name} // {student.instrument} // {student.pianist_id}")

def retrieve_student_by_id(student_id):
    found_student = Student.get_by_id(student_id)
    return found_student





def exit_program():
    print("Goodbye!")
    exit()
