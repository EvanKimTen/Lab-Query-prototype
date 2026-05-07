import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "research_lab.db")

con = sqlite3.connect(DB_NAME)
con.execute("PRAGMA foreign_keys = ON")