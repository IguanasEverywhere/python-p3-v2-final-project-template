from models.collaborative_pianist import Collaborative_Pianist

def seed_table():
    pianist_1 = Collaborative_Pianist("Scott", "Faculty", "scott@scott.com")
    pianist_2 = Collaborative_Pianist("Maria", "TA", "maria@maria.com")

    pianist_1.save_to_db()
    pianist_2.save_to_db()

seed_table()