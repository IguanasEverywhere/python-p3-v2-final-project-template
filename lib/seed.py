from models.collaborative_pianist import Collaborative_Pianist

def seed_table():
    Collaborative_Pianist.create("Scott", "Faculty", "scott@scott.com")
    Collaborative_Pianist.create("Maria", "TA", "maria@maria.com")
