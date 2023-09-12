from models.__init__ import CONN, CURSOR

class Student:

    all_students = {}

    def __init__(self, name, year, instrument, pianist_id = None, id=None):
        self.id = id
        self.name = name
        self.year = year
        self.instrument = instrument
        self.pianist_id = pianist_id

    def __repr__(self):
        return f"{self.name}, {self.year}, {self.instrument}"

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