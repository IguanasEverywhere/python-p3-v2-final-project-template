from models.__init__ import CONN, CURSOR
from models.collaborative_pianist import Collaborative_Pianist

class Student:

    all_students = {}

    def __init__(self, name, year, instrument, pianist_id, id=None):
        self.id = id
        self.name = name
        self.year = year
        self.instrument = instrument
        self.pianist_id = pianist_id

    def __repr__(self):
        return f"{self.name}, {self.year}, {self.instrument}, {self.pianist_id}"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name STRING,
            year STRING,
            instrument STRING,
            pianist_id INTEGER,
            FOREIGN KEY (pianist_id) REFERENCES collaborative_pianist(id)
            )
            """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS students
            """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, year, instrument, pianist_id=1):
        new_student = cls(name, year, instrument, pianist_id)
        print(new_student)
        new_student.save_to_db()
        return new_student

    def save_to_db(self):
        sql = """
            INSERT INTO students (name, year, instrument, pianist_id)
            VALUES (?, ?, ?, ?)
            """
        print(self)
        CURSOR.execute(sql, (self.name, self.year, self.instrument, self.pianist_id))
        CONN.commit()
        print(f"{self.name} saved to the database!")