import sqlite3
DB_NAME = "research_lab.db"
con = sqlite3.connect(DB_NAME)

def run_sql_file(cursor, filename):
    with open(filename, "r", encoding="utf-8") as file:
        sql_script = file.read()
    cursor.executescript(sql_script)

def initialize_database():
    con = sqlite3.connect(DB_NAME)
    # con.execute("PRAGMA foreign_keys = ON;")
    cursor = con.cursor()

    run_sql_file(cursor, "schema.sql")
    run_sql_file(cursor, "data.sql")

    con.commit()
    con.close()

    print("Database initialized successfully.")

initialize_database()