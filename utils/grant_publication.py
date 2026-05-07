import tkinter as tk
from tkinter import messagebox
from database.db import con

def clean(value):
    return value if value != "" else None

def open_grant_publication_menu(root):
    win = tk.Toplevel(root)
    win.title("Grant & Publication Reporting")
    win.geometry("450x450")

    tk.Label(win, text="Grant & Publication Reporting", font=("Arial", 16, "bold")).pack(pady=15)

    options = {
        "Top 5 Projects by Grant Funding": top_five_proj_grant_funding, #
        "Top Mentors by Publications": mentors_by_no_publicatons, #
        "Student Publications by Major/Year": student_publications, #
        "Ended Projects Before Date": ended_projs_wind, #
        "Top 3 Publication Years": top_three_pub_years #
    }

    for option, comamnd in options.items():
        tk.Button(win, text=option, width=35, command=comamnd).pack(pady=3)


def top_five_proj_grant_funding():
    cursor = con.cursor()
    cursor.execute("""
    select g.project_id, sum(g.budget) as total_funding
    from Grants g, Project p
    where g.project_id = p.project_id
    group by g.project_id
    order by total_funding desc
    limit 5;
    """)
    results = cursor.fetchall()
    for row in results:
        print(row)

def mentors_by_no_publicatons():
    cursor = con.cursor()
    cursor.execute("""
    select lm.mentor_id, count(*) as pub_count
    from LabMember lm
    JOIN Authors a ON lm.member_id = a.member_id
    where lm.mentor_id is not null
    group by lm.mentor_id
    having count(*) = (
    select max(pub_count)
    from (
        select lm2.mentor_id, count(*) AS pub_count_2
        FROM LabMember lm2
        JOIN Authors a2 ON lm2.member_id = a2.member_id
        where lm2.mentor_id is not null
        group by lm2.mentor_id
        ) as mentor_pub_counts
    );
    """)
    results = cursor.fetchall()
    for row in results:
        print(row)

def student_publications():
    cursor = con.cursor()
    cursor.execute("""
    select st.major, strftime('%Y', pb.publication_date) as publish_year, count(*)
    from Publication pb, Student st, Authors a
    where a.member_id = st.member_id and pb.publication_id = a.publication_id
    group by st.major, publish_year;
    """)
    results = cursor.fetchall()
    for row in results:
        print(row)

def ended_projs_wind(root):
    title = "Ended Projects Before Date"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("400x400")

    tk.Label(win, text="Date (yyyy-mm-dd)", font=("Arial", 16, "bold")).pack(pady=15)
    device_no_entry = tk.Entry(win)
    device_no_entry.pack()
    tk.Button(win, text="Search", command=lambda: ended_projs(device_no_entry.get())).pack()


def ended_projs(date):
    cursor = con.cursor()
    cursor.execute("""
    select p.project_id, count(DISTINCT g.grant_id)
    from Project p
    JOIN Grants g ON p.project_id = g.project_id
    where p.end_date < ?
    group by p.project_id;
    """, (date, ))
    results = cursor.fetchall()
    for row in results:
        print(row)

def top_three_pub_years():
    cursor = con.cursor()
    cursor.execute("""
    select strftime('%Y', pb.publication_date) as year, count(DISTINCT pb.publication_id) as publications
    from Student st
    JOIN Authors a ON st.member_id = a.member_id
    JOIN publication pb ON pb.publication_id = a.publication_id
    group by year
    order by publications desc
    limit 3;
    """)
    results = cursor.fetchall()
    for row in results:
        print(row)