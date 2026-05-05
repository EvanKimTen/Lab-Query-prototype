import tkinter as tk
from tkinter import messagebox
import sqlite3

def placeholder():
    messagebox.showinfo("Coming Soon", "This feature will be connected later.")

def open_project_member_menu():
    win = tk.Toplevel(root)
    win.title("Project & Member Management")
    win.geometry("400x400")

    tk.Label(win, text="Project & Member Management", font=("Arial", 16, "bold")).pack(pady=15)

    options = [
        "Query Member",
        "Query Project",
        "Add Member",
        "Add Project",
        "Update Member",
        "Update Project",
        "Remove Member",
        "Remove Project",
        "Assign Member to Project", # insert a pair into works_on table
        "Display Project Status",
        "Members by Grant",
        "Mentorship Relations"
    ]

    for option in options:
        tk.Button(win, text=option, width=30, command=placeholder).pack(pady=3)

def open_equipment_menu():
    win = tk.Toplevel(root)
    win.title("Equipment Usage Tracking")
    win.geometry("400x300")

    tk.Label(win, text="Equipment Usage Tracking", font=("Arial", 16, "bold")).pack(pady=15)

    options = [
        "Query Equipment",
        "Add Equipment",
        "Update Equipment",
        "Remove Equipment",
        "Query Equipment Usage",
        "Add Equipment Usage",
        "Update Equipment Usage",
        "Delete Equipment Usage",
        "Show Equipment Status",
        "Show Current Users"
    ]

    for option in options:
        tk.Button(win, text=option, width=30, command=placeholder).pack(pady=3)

def open_grant_publication_menu():
    win = tk.Toplevel(root)
    win.title("Grant & Publication Reporting")
    win.geometry("450x300")

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

root = tk.Tk()
root.title("Research Lab Manager")
root.geometry("420x300")

DB_NAME = "research_lab.db"
con = sqlite3.connect(DB_NAME)

tk.Label(root, text="Research Lab Manager", font=("Arial", 18, "bold")).pack(pady=25)

tk.Button(root, text="Project & Member Management", width=35, command=open_project_member_menu).pack(pady=8)
tk.Button(root, text="Equipment Usage Tracking", width=35, command=open_equipment_menu).pack(pady=8)
tk.Button(root, text="Grant & Publication Reporting", width=35, command=open_grant_publication_menu).pack(pady=8)

tk.Button(root, text="Exit", width=35, command=root.destroy).pack(pady=20)

root.mainloop()