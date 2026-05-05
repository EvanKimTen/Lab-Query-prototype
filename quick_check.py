import sqlite3

DB_NAME = "research_lab.db"
con = sqlite3.connect(DB_NAME)

cursor = con.cursor()
con.execute("PRAGMA foreign_keys = ON")

print(cursor.execute("SELECT * FROM Uses WHERE member_id = ? and device_number = ? and item_id = ?", (1, 1, 3)))

con.close()


# con = sqlite3.connect("research_lab.db")
# con.execute("PRAGMA foreign_keys = ON")
# con.commit()