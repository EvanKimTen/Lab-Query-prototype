import tkinter as tk
from tkinter import messagebox
from database.db import con

def clean(value):
    return value if value != "" else None


def open_project_member_menu(root):
    win = tk.Toplevel(root)
    win.title("Project & Member Management")
    win.geometry("600x800")

    tk.Label(win, text="Project & Member Management", font=("Arial", 16, "bold")).pack(pady=15)

    options = {
        "Query Member": open_query_member_window, #
        "Query Project": open_query_project_window, #
        "Add Member": add_member_window, 
        "Add Project": add_project_window, # 
        "Update Member": update_member_window, # 
        "Update Project": update_project_window, # 
        "Remove Member": delete_member_window, #
        "Remove Project": delete_project_window, #
        "Display Project Status": show_status_window, #
        "Members by Grant": member_by_grant_win, #
        "Mentorship Relations": display_mentorship_win #
    }

    for option, command_func in options.items():
        tk.Button(win, text=option, width=30, command=lambda f=command_func: f(root)).pack(pady=7)

def open_query_member_window(root):
    title = "Query Member"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("400x400")

    tk.Label(win, text=title, font=("Arial", 16, "bold")).pack(pady=15)
    member_id_entry = tk.Entry(win)
    member_id_entry.pack()
    tk.Button(win, text="Search", command=lambda: printout_query_result(member_id_entry.get(), title)).pack()

def open_query_project_window(root):
    title = "Query Project"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("400x400")
    
    tk.Label(win, text=title, font=("Arial", 16, "bold")).pack(pady=15)
    project_id_entry = tk.Entry(win)
    project_id_entry.pack()
    tk.Button(win, text="Search", command=lambda: printout_query_result(project_id_entry.get(), title)).pack()

def printout_query_result(_id, title):
    cursor = con.cursor()
    if title == "Query Member":
        cursor.execute(
            "SELECT * FROM LabMember WHERE member_id = ?",
            (_id,)
        )
    elif title == "Query Project":
        cursor.execute(
            "SELECT * FROM Project WHERE project_id = ?",
            (_id,)
        )
    results = cursor.fetchall()
    for row in results:
        print(row)

def add_member_window(root):
    title = "Add Member"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("500x500")

    fields = {}

    for label in ["member_id", "first_name", "middle_name", "last_name",
              "join_date", "mentor_id", "mentor_sdate", "mentor_edate"]:
        tk.Label(win, text=label).pack()
        entry = tk.Entry(win)
        entry.pack()
        fields[label] = entry


    tk.Button(win, text="Add", command=lambda: add_member_project(fields, title)).pack()

def add_project_window(root):
    title = "Add Project"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("450x450")

    fields = {}

    for label in ["project_id", "title", "begin_date", "end_date",
              "duration", "_status", "leader_id"]:
        tk.Label(win, text=label).pack()
        entry = tk.Entry(win)
        entry.pack()
        fields[label] = entry

    tk.Button(win, text="Add", command=lambda: add_member_project(fields, title)).pack()


def add_member_project(fields, title): 
    if title == "Add Member":
        values = tuple(clean(fields[name].get()) for name in [
            "member_id", "first_name", "middle_name", "last_name",
            "join_date", "mentor_id", "mentor_sdate", "mentor_edate"
        ])

        con.execute("""
            INSERT INTO LabMember
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, values)
        print("Inserted " + values[1])

    elif title == "Add Project":
        values = tuple(clean(fields[name].get()) for name in [
            "project_id", "title", "begin_date", "end_date", 
            "duration", "_status", "leader_id"
        ])

        con.execute("""
            INSERT INTO Project
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, values)
        print("Inserted " + values[1])
    con.commit()

def update_member_window(root):
    title = "Update Member"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("500x500")

    fields = {}

    for label in ["first_name", "middle_name", "last_name",
              "join_date", "mentor_id", "mentor_sdate", "mentor_edate", "member_id_to_update"]:
        tk.Label(win, text=label).pack()
        entry = tk.Entry(win)
        entry.pack()
        fields[label] = entry

    tk.Button(win, text="Add", command=lambda: update_member_project(fields, title)).pack()

def update_project_window(root):
    title = "Update Project"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("500x500")

    fields = {}

    for label in ["title", "begin_date", "end_date",
              "duration", "_status", "leader_id", "project_id_to_update"]:
        tk.Label(win, text=label).pack()
        entry = tk.Entry(win)
        entry.pack()
        fields[label] = entry

    tk.Button(win, text="Add", command=lambda: update_member_project(fields, title)).pack()

def update_member_project(fields, title):
    if title == "Update Member":
        member_id = fields["member_id_to_update"].get()

        updates = []
        values = []

        for col in [
            "first_name",
            "middle_name",
            "last_name",
            "join_date",
            "mentor_id",
            "mentor_sdate",
            "mentor_edate"
        ]:
            value = fields[col].get()

            if value != "":
                updates.append(f"{col} = ?")
                values.append(value)

        if not updates:
            messagebox.showwarning("No Update", "No fields were entered.")
            return

        values.append(member_id)

        sql = f"""
            UPDATE LabMember
            SET {", ".join(updates)}
            WHERE member_id = ?
        """

        con.execute(sql, values)
        con.commit()
        messagebox.showinfo("Success", "Member updated.")

    elif title == "Update Project":
        project_id = fields["project_id_to_update"].get()

        updates = []
        values = []

        for col in [
            "title", "begin_date", "end_date",
              "duration", "_status", "leader_id"
        ]:
            value = fields[col].get()

            if value != "":
                updates.append(f"{col} = ?")
                values.append(value)

        if not updates:
            messagebox.showwarning("No Update", "No fields were entered.")
            return

        values.append(project_id)

        sql = f"""
            UPDATE Project
            SET {", ".join(updates)}
            WHERE project_id = ?
        """

        con.execute(sql, values)
        con.commit()
        messagebox.showinfo("Success", "Project updated.")
        
def delete_member_window(root):
    title = "Remove Member"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("400x400")

    tk.Label(win, text=title, font=("Arial", 16, "bold")).pack(pady=15)
    project_id_entry = tk.Entry(win)
    project_id_entry.pack()
    tk.Button(win, text="Delete", command=lambda: delete_member_project(project_id_entry.get(), title)).pack()

def delete_project_window(root):
    title = "Remove Project"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("400x400")

    tk.Label(win, text=title, font=("Arial", 16, "bold")).pack(pady=15)
    project_id_entry = tk.Entry(win)
    project_id_entry.pack()
    tk.Button(win, text="Delete", command=lambda: delete_member_project(project_id_entry.get(), title)).pack()

def delete_member_project(_id, title):
    # cursor = con.cursor()
    if title == "Remove Member":
        con.execute("DELETE FROM LabMember WHERE member_id = ?", (_id, ))
    elif title == "Remove Project":
        con.execute("DELETE FROM Project WHERE project_id = ?", (_id, ))
    print("Deleted " + _id)
    con.commit()

def show_status_window(root):
    title = "Show Status"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("400x400")

    tk.Label(win, text=title, font=("Arial", 16, "bold")).pack(pady=15)
    member_id_entry = tk.Entry(win)
    member_id_entry.pack()
    tk.Button(win, text="show", command=lambda: show_status(member_id_entry.get())).pack()

def show_status(_id):
    cursor = con.cursor()
    cursor.execute(
            "SELECT _status FROM Project WHERE project_id = ?",
            (_id,)
    )
    results = cursor.fetchall()
    
    for row in results:
        if cursor.rowcount == 0:
            messagebox.showerror("Error", "No such member_id in database.") ##########
        else:
            # messagebox.showinfo("Success", row)
            print(row)


def member_by_grant_win(root):
    title = "Members by Grant"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("400x400")
    
    tk.Label(win, text=title, font=("Arial", 16, "bold")).pack(pady=15)
    project_id_entry = tk.Entry(win)
    project_id_entry.pack()
    tk.Button(win, text="Search", command=lambda: show_member_by_grant(project_id_entry.get())).pack()

def show_member_by_grant(g_id):
    cursor = con.cursor()

    cursor.execute(
    """
    select DISTINCT lm.member_id, lm.first_name, lm.last_name 
    from LabMember lm, works_on w, Project p, grants g
    where w.member_id = lm.member_id
    and w.project_id = p.project_id 
    and p.project_id = g.project_id
    and g.grant_id = ?
    """, (g_id,)
    )
    results = cursor.fetchall()
    for row in results:
        print(row)

def display_mentorship_win(root):
    title = "Mentorship Relations"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("400x400")
    
    tk.Label(win, text="project id", font=("Arial", 16, "bold")).pack(pady=15)
    project_id_entry = tk.Entry(win)
    project_id_entry.pack()
    tk.Button(win, text="Search", command=lambda: show_mentorship_given_proj(project_id_entry.get())).pack()

def show_mentorship_given_proj(p_id):
    cursor = con.cursor()

    cursor.execute(
    """
    SELECT DISTINCT lm.mentor_id, lm.member_id, w1.project_id
    FROM LabMember lm
    JOIN works_on w1 ON lm.member_id = w1.member_id
    JOIN works_on w2 ON lm.mentor_id = w2.member_id
    WHERE lm.mentor_id IS NOT NULL
  AND w1.project_id = w2.project_id AND w1.project_id = ?
    """, (p_id,)
    )
    results = cursor.fetchall()
    for row in results:
        print(row)