from models.collaborative_pianist import Collaborative_Pianist
from models.student import Student

def seed_table():
    Collaborative_Pianist.create("Scott", "Faculty", "scott@scott.com")
    Collaborative_Pianist.create("Maria", "TA", "maria@maria.com")

    Student.create("John", "Sophomore", "Violin", 1)
    Student.create("Anna", "Junior", "Flute", 2)
    Student.create("Bob", "Freshman", "Flute", 2)
    Student.create("Michael", "Senior", "Trumpet", 2)


