from models.__init__ import CONN, CURSOR
from models.collaborative_pianist import Collaborative_Pianist

class Student:

    all_students = {}

    def __init__(self, name, year, instrument, pianist_id=None, id=None):
        self.id = id
        self.name = name
        self.year = year
        self.instrument = instrument
        self.pianist_id = pianist_id

    # def __repr__(self):
    #     return f"{self.name}, {self.year}, {self.instrument}, {self.pianist_id}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a string of letters and not empty"
            )

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if year == "Freshman" or year == "Sophomore" or year == "Junior" or year == "Senior":
            self._year = year
        else:
            raise ValueError("Year must be Freshman, Sophomore, Junior, or Senior")

    @property
    def instrument(self):
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        if isinstance(instrument, str) and len(instrument):
            self._instrument = instrument
        else:
            raise ValueError(
                "Instrument must be a non-empty string"
            )



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
    def create(cls, name, year, instrument, pianist_id=None):
        new_student = cls(name, year, instrument, pianist_id)
        new_student.save_to_db()
        return new_student

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM students
            """
        all_student_rows = CURSOR.execute(sql).fetchall()
        return [cls.make_instance_from_db(row) for row in all_student_rows]

    @classmethod
    def make_instance_from_db(cls, row):
        student = cls.all_students.get(row[0])
        if student:
            #fix this
            if not student.name == row[1]:
                student.name = row[1]
            if not student.year == row[2]:
                student.year = row[2]
            if not student.instrument == row[3]:
                student.instrument = row[3]
            if not student.pianist_id == row[4]:
                student.pianist_id = row[4]
            return cls.all_students[row[0]]
        else:
            student = Student(row[1], row[2], row[3], row[4])
            cls.all_students[row[0]] = student
            student.id = row[0]
            return student

    @classmethod
    def get_by_id(cls, id):
        sql = """
            SELECT *
            FROM students
            WHERE id = ?
            """
        found_student = CURSOR.execute(sql, (id,)).fetchone()
        return cls.make_instance_from_db(found_student)


    def save_to_db(self):
        sql = """
            INSERT INTO students (name, year, instrument, pianist_id)
            VALUES (?, ?, ?, ?)
            """
        CURSOR.execute(sql, (self.name, self.year, self.instrument, self.pianist_id))
        CONN.commit()
        print(f"{self.name} saved to the database!")

    def delete_instance(self):
        sql = """
            DELETE FROM students
            WHERE id = ?
            """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        print(f"{self.name} deleted from database!")

    def unassign_students(pianist_id):
        sql = """
            UPDATE students
            SET pianist_id = NULL
            WHERE pianist_id = ?
            """
        CURSOR.execute(sql, (pianist_id,))
        CONN.commit()
        print("Students updated!")

    def update_student(self, name, year, instrument, pianist_id):
        sql = """
            UPDATE students
            SET name = ?, year = ?, instrument = ?, pianist_id = ?
            WHERE id = ?
            """
        CURSOR.execute(sql, (name, year, instrument, pianist_id, self.id))
        CONN.commit()

        print(f"{self.name} has been updated!")