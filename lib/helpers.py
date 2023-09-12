# lib/helpers.py
from models.collaborative_pianist import Collaborative_Pianist

def get_all_pianists_from_db():
    all_pianists = Collaborative_Pianist.get_all()
    for pianist in all_pianists:
        print(f"ID: {pianist.id} {pianist.name} // {pianist.rank} // {pianist.email}")

def retrieve_pianist_by_id(pianist_id):
    found_pianist = Collaborative_Pianist.get_by_id(pianist_id)
    print(f"ID: {found_pianist.id} {found_pianist.name} // {found_pianist.rank} // {found_pianist.email}")




def exit_program():
    print("Goodbye!")
    exit()
