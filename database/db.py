import sqlite3

DB_NAME = "research_lab.db"

con = sqlite3.connect(DB_NAME)
con.execute("PRAGMA foreign_keys = ON")