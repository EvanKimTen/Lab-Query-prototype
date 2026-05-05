import tkinter as tk
from tkinter import messagebox

def placeholder():
    messagebox.showinfo("Coming Soon", "This feature will be connected later.")


def open_project_member_menu():
    win = tk.Toplevel()
    win.title("Project & Member Management")
    win.geometry("400x400")

    tk.Label(win, text="Project & Member Management", font=("Arial", 16, "bold")).pack(pady=15)

    options = {
        "Query Member": open_query_member_window,
        "Query Project": placeholder,
        "Add Member": placeholder,
        "Add Project": placeholder,
        "Update Member": placeholder,
        "Update Project": placeholder,
        "Remove Member": placeholder,
        "Remove Project": placeholder,
        "Assign Member to Project": placeholder, # insert a pair into works_on table
        "Display Project Status": placeholder,
        "Members by Grant": placeholder,
        "Mentorship Relations": placeholder
    }

    for option, command in options.items():
        tk.Button(win, text=option, width=30, command=command).pack(pady=7)

def open_query_member_window():
    win = tk.Toplevel()
    win.title("Query Member")
    win.geometry("400x400")

    tk.Label(win, text="Query Member", font=("Arial", 16, "bold")).pack(pady=15)
    member_id_entry = tk.Entry(win)
    member_id_entry.pack()
    tk.Button(win, text="Search", command=lambda: print(member_id_entry.get())).pack()