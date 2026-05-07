import tkinter as tk
from tkinter import messagebox
from database.db import con

from utils.project_member_windows import open_project_member_menu
from utils.equipment_usage_windows import open_equipment_menu
from utils.grant_publication import open_grant_publication_menu

root = tk.Tk()
root.title("Research Lab Manager")
root.geometry("420x300")

def exit_app():
    con.close()
    root.destroy()

tk.Label(root, text="Research Lab Manager", font=("Arial", 18, "bold")).pack(pady=25)

tk.Button(root, text="Project & Member Management", width=35, command=lambda: open_project_member_menu(root)).pack(pady=8)
tk.Button(root, text="Equipment Usage Tracking", width=35, command=lambda: open_equipment_menu(root)).pack(pady=8)
tk.Button(root, text="Grant & Publication Reporting", width=35, command=lambda: open_grant_publication_menu(root)).pack(pady=8)

tk.Button(root, text="Exit", width=35, command=exit_app).pack(pady=20)

root.mainloop()