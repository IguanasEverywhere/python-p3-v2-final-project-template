#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.collaborative_pianist import Collaborative_Pianist
from seed import seed_table

def start_fresh_table():
    Collaborative_Pianist.drop_table()
    Collaborative_Pianist.create_table()
    seed_table()


start_fresh_table()


ipdb.set_trace()
