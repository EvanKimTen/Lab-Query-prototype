import tkinter as tk
from tkinter import messagebox
from database.db import con

def clean(value):
    return value if value != "" else None

def open_equipment_menu(root):
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

    for option, command_func in options.items():
        tk.Button(win, text=option, width=30, command=lambda f=command_func: f(root)).pack(pady=7)

def open_query_equipment_window(root):
    title = "Query Equipment"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("400x400")

    tk.Label(win, text=title, font=("Arial", 16, "bold")).pack(pady=15)
    member_id_entry = tk.Entry(win)
    member_id_entry.pack()
    tk.Button(win, text="Search", command=lambda: eq_printout_query_result(member_id_entry.get(), title)).pack()

def open_query_usage_window(root):
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
        # messagebox.showinfo("Success", row)
        print(row)

def add_equipment_wind(root):
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

def add_usage_wind(root):
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

def update_eqpt_win(root):
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

def update_eqpt_usage_win(root):
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

def delete_eqpt_win(root):
    title = "Remove Equipment"
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("500x500")

    tk.Label(win, text=title, font=("Arial", 16, "bold")).pack(pady=15)
    item_id_entry = tk.Entry(win)
    item_id_entry.pack()
    tk.Button(win, text="Delete", command=lambda: delete_equipment_usage(item_id_entry.get(), title)).pack()

def delete_usage_win(root):
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

def eq_status_wind(root):
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
        # messagebox.showinfo("Success", row)
        print(row)

def current_users_wind(root):
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
        # messagebox.showinfo("Success", row)
        print(row)