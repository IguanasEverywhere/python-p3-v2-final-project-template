#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.collaborative_pianist import Collaborative_Pianist
from models.student import Student
from seed import seed_table

def start_fresh_table():
    Collaborative_Pianist.drop_table()
    Collaborative_Pianist.create_table()
    Student.drop_table()
    Student.create_table()

    seed_table()


start_fresh_table()


ipdb.set_trace()
