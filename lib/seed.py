from models.collaborative_pianist import Collaborative_Pianist
from models.student import Student

def seed_table():
    Collaborative_Pianist.create("No Pianist", "Faculty", "None@none.com")
    Collaborative_Pianist.create("Scott", "Faculty", "scott@scott.com")
    Collaborative_Pianist.create("Maria", "TA", "maria@maria.com")
    Collaborative_Pianist.create("Emily", "Faculty", "emily@emily.com")

    Student.create("John", "Sophomore", "Violin", 2)
    Student.create("Anna", "Junior", "Flute", 1)
    Student.create("Bob", "Freshman", "Flute", 3)
    Student.create("Michael", "Senior", "Trumpet", 3)
    Student.create("Karen", "Freshman", "Trombone", 3)
    Student.create("Adam", "Junior", "Viola", 4)


