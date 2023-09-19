from models.__init__ import CONN, CURSOR

class Collaborative_Pianist:

    all_pianists = {}

    def __init__(self, name, rank, email, id=None):
        self.id = id
        self.name = name
        self.rank = rank
        self.email = email

    # def __repr__(self):
    #     return f"\n {self.name.upper()} // {self.rank} // {self.email}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name value must be letters and not be empty!"
            )
    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, rank):
        if rank == 'Faculty' or rank == 'TA' or rank == 'Student':
            self._rank = rank
        else:
            raise ValueError(
                "Pianist rank must be Faculty, TA, or Student"
            )

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if '@' in email and '.' in email:
            self._email = email
        else:
            raise ValueError(
                "Email addresses must include both an @ and a . symbol"
            )


    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS collaborative_pianists (
            id INTEGER PRIMARY KEY,
            name STRING,
            rank STRING,
            email STRING
            )
            """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS collaborative_pianists
            """
        CONN.execute(sql)
        CONN.commit()

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM collaborative_pianists
            """
        all_pianists_rows = CONN.execute(sql).fetchall()
        return [cls.make_instance_from_db_row(pianist) for pianist in all_pianists_rows]

    @classmethod
    def get_by_id(cls, id):
        sql = """
            SELECT *
            FROM collaborative_pianists
            WHERE id = ?
            """
        found_pianist = CONN.execute(sql, (id,)).fetchone()
        if found_pianist == None:
            raise ValueError(
                "No pianist found by that ID in the database!"
            )
        else:
            return cls.make_instance_from_db_row(found_pianist)



    @classmethod
    def make_instance_from_db_row(cls, row):
        pianist = cls.all_pianists.get(row[0])
        if pianist:
            if not pianist.name == row[1]:
                pianist.name = row[1]
            if not pianist.rank == row[2]:
                pianist.rank = row[2]
            if not pianist.email == row[3]:
                pianist.email = row[3]
            return cls.all_pianists[row[0]]
        else:
            pianist = Collaborative_Pianist(row[1], row[2], row[3])
            cls.all_pianists[row[0]] = pianist
            pianist.id = row[0]
            return pianist

    @classmethod
    def create(cls, name, rank, email):
        new_pianist = cls(name, rank, email)
        new_pianist.save_to_db()
        return new_pianist


    def save_to_db(self):
        sql = """
            INSERT INTO collaborative_pianists (name, rank, email)
            VALUES (?, ?, ?)
            """
        CURSOR.execute(sql, (self.name, self.rank, self.email))
        CONN.commit()

        print(f"\n{self.name} saved to the database!")

    def delete_instance(self):
        from models.student import Student
        sql = """
            DELETE
            FROM collaborative_pianists
            WHERE ID = ?
            """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        print(f"\n ** {self.name} deleted from database! **")

        Student.unassign_students(self.id)


    def get_assigned_students(id):
        from models.student import Student
        sql = """
            SELECT *
            FROM students
            WHERE pianist_id = ?
            """
        found_students = CURSOR.execute(sql, (id,)).fetchall()
        return [Student.make_instance_from_db(row) for row in found_students]

    def update_pianist(self, name, rank, email):
            sql = """
                UPDATE collaborative_pianists
                SET name = ?, rank = ?, email = ?
                WHERE id = ?
                """
            CURSOR.execute(sql, (name, rank, email, self.id))
            CONN.commit()

            print(f"\n** {self.name} updated! **")






