from models.__init__ import CONN, CURSOR

class Collaborative_Pianist:

    all_pianists = {}

    def __init__(self, name, rank, email, id=None):
        self.id = id
        self.name = name
        self.rank = rank
        self.email = email

    def __repr__(self):
        return f"\n {self.name.upper()} // {self.rank} // {self.email}"

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
    def make_instance_from_db_row(cls, row):
        pianist = cls.all_pianists.get(row[0])
        if pianist:
            return cls.all_pianists[row[0]]
        else:
            pianist = Collaborative_Pianist(row[1], row[2], row[3])
            cls.all_pianists[row[0]] = pianist
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

        print(f"{self.name} saved to the database!")

    def delete_instance(self):
        print(self.id)
        sql = """
            DELETE
            FROM collaborative_pianists
            WHERE ID = ?
            """
        CURSOR.execute(sql, (self.id))
        print(f"{self.name} deleted from database!")



