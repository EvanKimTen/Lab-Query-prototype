import tkinter as tk
from tkinter import messagebox
import sqlite3


DB_NAME = "research_lab.db"
con = sqlite3.connect(DB_NAME)
con.execute("PRAGMA foreign_keys = ON") # enforcing fk constraints in schema.sql.
# print(con.execute("PRAGMA foreign_keys").fetchone())

def placeholder():
    messagebox.showinfo("Coming Soon", "This feature will be connected later.")

def open_project_member_menu():
    win = tk.Toplevel(root)
    win.title("Project & Member Management")
    win.geometry("600x800")

    tk.Label(win, text="Project & Member Management", font=("Arial", 16, "bold")).pack(pady=15)

    options = {
        "Query Member": open_query_member_window, #
        "Query Project": open_query_project_window, #
        "Add Member": add_member_window, # - after deciding, you have to insert into one of the sub tables. (you don't have to, just leave it out.)
        "Add Project": add_project_window, # 
        "Update Member": update_member_window, # 
        "Update Project": update_project_window, # 
        "Remove Member": delete_member_window, #
        "Remove Project": delete_project_window, #
        "Display Project Status": show_status_window, # - error: no such proj id
        "Members by Grant": member_by_grant_win, #
        "Mentorship Relations": display_mentorship_win #
    }

    for option, command in options.items():
        tk.Button(win, text=option, width=30, command=command).pack(pady=7)

def open_query_member_window():
    title = "Query Member"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("400x400")

    tk.Label(win, text=title, font=("Arial", 16, "bold")).pack(pady=15)
    member_id_entry = tk.Entry(win)
    member_id_entry.pack()
    tk.Button(win, text="Search", command=lambda: printout_query_result(member_id_entry.get(), title)).pack()

def open_query_project_window():
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

def add_member_window():
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

    member_type_var = tk.StringVar(value="Student")

    tk.Label(win, text="member_type").pack()
    tk.OptionMenu(
        win,
        member_type_var,
        "Student",
        "Faculty",
        "Collaborator"
    ).pack()

    tk.Button(win, text="Add", command=lambda: add_member_project(fields, member_type_var.get(), title)).pack()

def add_project_window():
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

def clean(value):
    return value if value != "" else None

def add_member_project(fields, member_type, title):
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

        member_id = fields["member_id"].get()

        if member_type == "Student":
            con.execute("""
                INSERT INTO Student (member_id)
                VALUES (?)
            """, (member_id,))

        elif member_type == "Faculty":
            con.execute("""
                INSERT INTO Faculty (member_id)
                VALUES (?)
            """, (member_id,))

        elif member_type == "Collaborator":
            con.execute("""
                INSERT INTO Collaborator (member_id)
                VALUES (?)
            """, (member_id,))

    elif title == "Add Project":
        values = tuple(clean(fields[name].get()) for name in [
            "project_id", "title", "begin_date", "end_date", 
            "duration", "_status", "leader_id"
        ])

        con.execute("""
            INSERT INTO Project
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, values)
        print("Inserted " + values("title"))
    con.commit()

def update_member_window():
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

def update_project_window():
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
        
def delete_member_window():
    title = "Remove Member"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("400x400")

    tk.Label(win, text=title, font=("Arial", 16, "bold")).pack(pady=15)
    project_id_entry = tk.Entry(win)
    project_id_entry.pack()
    tk.Button(win, text="Delete", command=lambda: delete_member_project(project_id_entry.get(), title)).pack()

def delete_project_window():
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

def show_status_window():
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
            messagebox.showinfo("Success", row)

def member_by_grant_win():
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
    select DISTINCT lm.member_id, lm.first_name, lm.last_name from LabMember lm, works_on w, Project p, grants g
    where w.project_id = p.project_id 
    and w.member_id = lm.member_id 
    and g.project_id = p.project_id
    and g.grant_id = ?
    """, (g_id,)
    )
    results = cursor.fetchall()
    for row in results:
        print(row)

def member_by_grant_win():
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
    select DISTINCT lm.member_id, lm.first_name, lm.last_name from LabMember lm, works_on w, Project p, grants g
    where w.project_id = p.project_id 
    and w.member_id = lm.member_id 
    and g.project_id = p.project_id
    and g.grant_id = ?
    """, (g_id,)
    )
    results = cursor.fetchall()
    for row in results:
        print(row)

def display_mentorship_win():
    title = "Mentorship Relations"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("400x400")
    
    tk.Label(win, text=title, font=("Arial", 16, "bold")).pack(pady=15)
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


def open_equipment_menu():
    win = tk.Toplevel(root)
    win.title("Equipment Usage Tracking")
    win.geometry("700x650")

    tk.Label(win, text="Equipment Usage Tracking", font=("Arial", 16, "bold")).pack(pady=15)

    options = {
        "Query Equipment": open_query_equipment_window, #
        "Query Equipment Usage": open_query_usage_window, # 
        "Add Equipment": add_equipment_wind,  #
        "Add Equipment Usage": add_usage_wind, #
        "Update Equipment": update_eqpt_win, #
        "Update Equipment Usage": update_eqpt_usage_win, #
        "Remove Equipment": delete_eqpt_win, #
        "Delete Equipment Usage": delete_usage_win, #
        "Show Equipment Status": eq_status_wind, #
        "Show Current Users": current_users_wind #
    }

    for option, command in options.items():
        tk.Button(win, text=option, width=30, command=command).pack(pady=7)

def open_query_equipment_window():
    title = "Query Equipment"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("400x400")

    tk.Label(win, text=title, font=("Arial", 16, "bold")).pack(pady=15)
    member_id_entry = tk.Entry(win)
    member_id_entry.pack()
    tk.Button(win, text="Search", command=lambda: eq_printout_query_result(member_id_entry.get(), title)).pack()

def open_query_usage_window():
    title = "Query Equipment Usage"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("400x400")

    fields = {}
    for label in ["item_id", "device_number", "member_id"]:
        tk.Label(win, text=label).pack()
        entry = tk.Entry(win)
        entry.pack()
        fields[label] = entry
    tk.Button(win, text="Search", command=lambda: eq_printout_query_result(fields, title)).pack()

def eq_printout_query_result(fields, title):
    cursor = con.cursor()
    if title == "Query Equipment":
        item_id = fields
        cursor.execute(
            "SELECT * FROM Equipment WHERE item_id = ?",
            (item_id,)
        )
    elif title == "Query Equipment Usage":
        values = tuple(clean(fields[name].get()) for name in [
            "item_id", "device_number", "member_id"
        ])
        cursor.execute(
            "SELECT * FROM Uses WHERE item_id = ? and device_number = ? and member_id = ?",
            (values)
        )
    results = cursor.fetchall()
    for row in results:
        messagebox.showinfo("Success", row)
        # print(row)

def add_equipment_wind():
    title = "Add Equipment"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("750x500")

    fields = {}

    for label in ["item_id", "_name", "_type", "_manual"]:
        tk.Label(win, text=label).pack()
        entry = tk.Entry(win)
        entry.pack()
        fields[label] = entry

    tk.Button(win, text="Add", command=lambda: add_equipment_usage(fields, title)).pack()

def add_usage_wind():
    title = "Add Equipment Usage"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("500x500")

    fields = {}

    for label in ["member_id", "item_id", "device_number", "begin_date", "end_date", "purpose_of_use"]:
        tk.Label(win, text=label).pack()
        entry = tk.Entry(win)
        entry.pack()
        fields[label] = entry

    tk.Button(win, text="Add", command=lambda: add_equipment_usage(fields, title)).pack()

def add_equipment_usage(fields, title):
    if title == "Add Equipment": 
        values = tuple(clean(fields[name].get()) for name in [
            "item_id", "_name", "_type", "_manual"
        ])
        con.execute("""
            INSERT INTO Equipment (item_id, _name, _type, _manual)
            VALUES (?, ?, ?, ?)
        """, (values))
        con.commit()
        messagebox.showinfo("Success", "Equipment inserted.")
    elif title == "Add Equipment Usage":
        values = tuple(clean(fields[name].get()) for name in [
            "member_id", "item_id", "device_number", "begin_date", "end_date", "purpose_of_use"
        ])
        con.execute("""
            INSERT INTO Uses
            (member_id, item_id, device_number, begin_date, end_date, purpose_of_use)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (values))
        con.commit()
        messagebox.showinfo("Success", "Equipment usage inserted.")

def update_eqpt_win():
    title = "Update Equipment"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("500x500")

    fields = {}

    for label in ["item_id to update", "_name", "_type", "_manual"]:
        tk.Label(win, text=label).pack()
        entry = tk.Entry(win)
        entry.pack()
        fields[label] = entry

    tk.Button(win, text="Update", command=lambda: update_eqpt_usage(fields, title)).pack()

def update_eqpt_usage_win():
    title = "Update Equipment Usage"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("500x500")

    fields = {}

    for label in ["member_id to update", "item_id to update", "device_number to update", "begin_date", "end_date", "purpose_of_use"]:
        tk.Label(win, text=label).pack()
        entry = tk.Entry(win)
        entry.pack()
        fields[label] = entry

    tk.Button(win, text="Update", command=lambda: update_eqpt_usage(fields, title)).pack()
    
def update_eqpt_usage(fields, title):
    if title == "Update Equipment":
        item_id = fields["item_id to update"].get()

        updates = []
        values = []

        for col in ["_name", "_type", "_manual"]:
            value = fields[col].get()

            if value != "":
                updates.append(f"{col} = ?")
                values.append(value)

        if not updates:
            messagebox.showwarning("No Update", "No fields were entered.")
            return

        values.append(item_id)

        sql = f"""
            UPDATE Equipment
            SET {", ".join(updates)}
            WHERE item_id = ?
        """

        con.execute(sql, values)
        con.commit()
        messagebox.showinfo("Success", "Equipment updated.")

    elif title == "Update Equipment Usage":
        member_id = fields["member_id to update"].get()
        item_id = fields["item_id to update"].get()
        device_number = fields["device_number to update"].get()
    
        updates = []
        values = []

        for col in ["begin_date", "end_date", "purpose_of_use"]:
            value = fields[col].get()

            if value != "":
                updates.append(f"{col} = ?")
                values.append(value)

        if not updates:
            messagebox.showwarning("No Update", "No fields were entered.")
            return

        values.append(member_id)
        values.append(item_id)
        values.append(device_number)

        sql = f"""
            UPDATE Uses
            SET {", ".join(updates)}
            WHERE member_id = ? and item_id = ? and device_number = ?
        """

        con.execute(sql, values)
        con.commit()
        messagebox.showinfo("Success", "Equipment Usage updated.")

def delete_eqpt_win():
    title = "Remove Equipment"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("500x500")

    tk.Label(win, text=title, font=("Arial", 16, "bold")).pack(pady=15)
    item_id_entry = tk.Entry(win)
    item_id_entry.pack()
    tk.Button(win, text="Delete", command=lambda: delete_equipment_usage(item_id_entry.get(), title)).pack()

def delete_usage_win():
    title = "Delete Equipment Usage"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("400x400")

    fields = {}
    for label in ["member_id", "item_id", "device_number"]:
        tk.Label(win, text=label).pack()
        entry = tk.Entry(win)
        entry.pack()
        fields[label] = entry
    tk.Button(win, text="Delete", command=lambda: delete_equipment_usage(fields, title)).pack()

def delete_equipment_usage(fields, title):
    if title == "Remove Equipment":
        item_id = fields
        con.execute("""
            DELETE FROM Equipment
            WHERE item_id = ?
        """, (item_id,))
        con.commit()
        messagebox.showinfo("Success", "Equipment deleted.")
    elif title == "Delete Equipment Usage":
        con.execute("""
        DELETE FROM Uses
        WHERE member_id = ?
            AND item_id = ?
            AND device_number = ?
        """, (fields))
        con.commit()
        messagebox.showinfo("Success", "Equipment usage deleted.")

def eq_status_wind():
    title = "Show Equipment Status"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("400x400")

    tk.Label(win, text="device number", font=("Arial", 16, "bold")).pack(pady=15)
    device_no_entry = tk.Entry(win)
    device_no_entry.pack()
    tk.Button(win, text="Search", command=lambda: show_eq_status(device_no_entry.get())).pack()

def show_eq_status(device_no):
    cursor = con.cursor()
    cursor.execute(
        "select _status from Device where device_number = ?;",
        (device_no,)
    )
    results = cursor.fetchall()
    for row in results:
        messagebox.showinfo("Success", row)
        print(row)

def current_users_wind():
    title = "Show Current Users"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("400x400")

    tk.Label(win, text="device number", font=("Arial", 16, "bold")).pack(pady=15)
    device_no_entry = tk.Entry(win)
    device_no_entry.pack()
    tk.Button(win, text="Search", command=lambda: show_current_user_project_per_device(device_no_entry.get())).pack()

def show_current_user_project_per_device(entry):
    cursor = con.cursor()
    cursor.execute("""
    SELECT DISTINCT lm.member_id, lm.first_name, lm.last_name, w.project_id
    FROM Uses u
    JOIN LabMember lm ON lm.member_id = u.member_id
    JOIN Works_On w ON w.member_id = lm.member_id
    JOIN Project p ON p.project_id = w.project_id
    WHERE u.device_number = ? AND u.end_date IS NULL
    ORDER BY lm.member_id ASC
    """, (entry,))
    results = cursor.fetchall()
    for row in results:
        messagebox.showinfo("Success", row)
        print(row)


def open_grant_publication_menu():
    win = tk.Toplevel(root)
    win.title("Grant & Publication Reporting")
    win.geometry("450x450")

    tk.Label(win, text="Grant & Publication Reporting", font=("Arial", 16, "bold")).pack(pady=15)

    options = [
        "Top 5 Projects by Grant Funding",
        "Top Mentors by Publications",
        "Student Publications by Major/Year",
        "Ended Projects Before Date",
        "Top 3 Publication Years"
    ]

    for option in options:
        tk.Button(win, text=option, width=35, command=placeholder).pack(pady=3)




def exit_app():
    con.close()
    root.destroy()

root = tk.Tk()
root.title("Research Lab Manager")
root.geometry("420x300")


tk.Label(root, text="Research Lab Manager", font=("Arial", 18, "bold")).pack(pady=25)

tk.Button(root, text="Project & Member Management", width=35, command=open_project_member_menu).pack(pady=8)
tk.Button(root, text="Equipment Usage Tracking", width=35, command=open_equipment_menu).pack(pady=8)
tk.Button(root, text="Grant & Publication Reporting", width=35, command=open_grant_publication_menu).pack(pady=8)

tk.Button(root, text="Exit", width=35, command=exit_app).pack(pady=20)

root.mainloop()