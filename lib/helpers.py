# lib/helpers.py
from models.collaborative_pianist import Collaborative_Pianist

def get_all_pianists_from_db():
    all_pianists = Collaborative_Pianist.get_all()
    for pianist in all_pianists:
        print(f"ID: {pianist.id} {pianist.name} // {pianist.rank} // {pianist.email}")

def retrieve_pianist_by_id(pianist_id):
    found_pianist = Collaborative_Pianist.get_by_id(pianist_id)
    return found_pianist

def retrieve_pianist_by_name(name):
    found_pianist = Collaborative_Pianist.get_by_name(name)
    return found_pianist

def delete_pianist(pianist_id):
    pianist_to_delete = retrieve_pianist_by_id(pianist_id)
    Collaborative_Pianist.delete_instance(pianist_to_delete)




def exit_program():
    print("Goodbye!")
    exit()
