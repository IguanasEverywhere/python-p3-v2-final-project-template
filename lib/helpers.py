# lib/helpers.py
from models.collaborative_pianist import Collaborative_Pianist
from models.student import Student


def get_all_pianists_from_db():
    all_pianists = Collaborative_Pianist.get_all()
    print("\n+++ ALL COLLABORATIVE PIANISTS: +++ \n")
    for pianist in all_pianists:
        print(f"ID: {pianist.id} {pianist.name}")

def retrieve_pianist_by_id(pianist_id):
    ## Check all?
    try:
        found_pianist = Collaborative_Pianist.get_by_id(pianist_id)
        return found_pianist
    except Exception as msg:
        print(msg)

def print_pianist_info(self):
    print(f"\n=====PIANIST INFO:=====")
    print(f"ID: {self.id} Name: {self.name} // Rank: {self.rank} // Email: {self.email}")
    print("=======================")

def delete_pianist(pianist_id):
    pianist_to_delete = retrieve_pianist_by_id(pianist_id)
    if pianist_to_delete == None:
        print("No pianist by that ID in the database!")
    else:
        Collaborative_Pianist.delete_instance(pianist_to_delete)

def add_new_pianist():
    print("\n+++ ADD NEW PIANIST +++ \n")
    name = input("Enter pianist's name: ")
    rank = input("Enter pianist's rank (Faculty, TA, or Student): ")
    email = input("Enter pianist's email: ")
    try:
        Collaborative_Pianist.create(name, rank, email)
    except Exception as msg:
        print(f"\n** {msg} **")
        print("Please try again!")
        add_new_pianist()

def get_assigned_students(self):
    print(f"\n+++ STUDENTS ASSIGNED TO {self.name.upper()}: +++ \n")
    assigned_students = Collaborative_Pianist.get_assigned_students(self.id)
    for student in assigned_students:
        print_student_info(student)
    print('------------------------------')

def update_pianist_info(self):
    print(f"\n+++ UPDATE {self.name} +++ \n")

    try:
        name = input("Enter updated name: ")
        self.name = name
        rank = input("Enter updated rank: ")
        self.rank = rank
        email = input("Enter updated email: ")
        self.email = email
        self.update_pianist(name, rank, email)

    except Exception as msg:
        print(f"\n\n!!! ERROR UPDATING {self.name} !!!")
        print(msg)
        fetched_pianist_from_db = Collaborative_Pianist.get_by_id(self.id)
        update_pianist_info(fetched_pianist_from_db)


def get_all_students_from_db():
    all_students = Student.get_all()
    print("\n+++ ALL STUDENTS: +++ \n")
    for student in all_students:
        print(f"ID: {student.id} {student.name}")

def retrieve_student_by_id(student_id):
    found_student = Student.get_by_id(student_id)
    return found_student

def delete_student(student_id):
    student_to_delete = retrieve_student_by_id(student_id)
    Student.delete_instance(student_to_delete)

def print_student_info(self):
    print(f"\n=====STUDENT INFO:=====")
    print(f"ID: {self.id} Name: {self.name} // Year: {self.year} // Instrument: {self.instrument}")
    print("=======================")

def retrieve_assigned_pianist_for_student(self):
    if not self.pianist_id:
        print("Pianist unassigned! Would you like to assign a pianist? Y/N: ")
        choice = input(">> ")
        if choice.upper() == 'Y':
            get_all_pianists_from_db()
            pianist_selection = input(f"Enter ID of pianist to assign to {self.name}: >>")
            self.update_student(self.name, self.year, self.instrument, pianist_selection)


    else:
        assigned_pianist = retrieve_pianist_by_id(self.pianist_id)
        print(f"\n{self.name}'s assigned pianist:")
        print_pianist_info(assigned_pianist)

def update_student_info(self):
    print(f"\n+++ UPDATE {self.name} +++ \n")
    name = input("Enter updated name: ")
    year = input("Enter updated year: ")
    instrument = input("Enter updated instrument: ")
    get_all_pianists_from_db()
    pianist =  input("Enter pianist's id to assign to this student: ")


    try:
        self.name = name
        self.year = year
        self.instrument = instrument
        self.pianist_id = pianist

        self.update_student(name, year, instrument, pianist)
    except Exception as msg:
        print(f"\n\n!!! ERROR UPDATING {self.name} !!!")
        print(msg)

def add_new_student():
    print("\n+++ ADD NEW STUDENT +++ \n")
    name = input("Enter student's name: ")
    year = input("Enter pianist's year (Freshman, Sophomore, Junior, Senior): ")
    instrument = input("Enter pianist's instrument: ")
    get_all_pianists_from_db()
    pianist_id =  input("Enter pianist's id to assign to this student (1 for unassigned): ")

    Student.create(name, year, instrument, pianist_id)

def unassigned_students():
    print("\n+++ UNASSIGNED STUDENTS +++ \n")
    unassigned_students = Student.get_unassigned_students()
    for student in unassigned_students:
        print_student_info(student)


def exit_program():
    print("Goodbye!")
    exit()
