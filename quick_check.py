import sqlite3

DB_NAME = "research_lab.db"
con = sqlite3.connect(DB_NAME)

cursor = con.cursor()
con.execute("PRAGMA foreign_keys = ON")
results = cursor.execute("""
select strftime('%Y', pb.publication_date) as year, count(DISTINCT pb.publication_id) as publications
from Student st
JOIN Authors a ON st.member_id = a.member_id
JOIN publication pb ON pb.publication_id = a.publication_id
group by year
order by publications desc
limit 3;
""").fetchall()
for row in results: 
    print(row)

con.close()


# con = sqlite3.connect("research_lab.db")
# con.execute("PRAGMA foreign_keys = ON")
# con.commit()