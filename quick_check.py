import sqlite3

DB_NAME = "research_lab.db"
con = sqlite3.connect(DB_NAME)

cursor = con.cursor()
con.execute("PRAGMA foreign_keys = ON")
results = cursor.execute("""
select p.project_id, count(DISTINCT g.grant_id)
from Project p
JOIN Grants g ON p.project_id = g.project_id
where p.end_date < ?
group by p.project_id;
""", ('2025-01-01', )).fetchall()
for row in results: 
    print(row)

con.close()


# con = sqlite3.connect("research_lab.db")
# con.execute("PRAGMA foreign_keys = ON")
# con.commit()