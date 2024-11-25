import tkinter as tk
from tkinter import font
import json
import os

# Define the filename to store tasks
TASKS_FILE = "tasks.json"

root = tk.Tk()
root.title("To Do List")
root.geometry("1000x800")

# Create a custom font
new_font = font.Font(family="Helvetica", size=16)

# Create the listbox with the custom font
list_box = tk.Listbox(root, height=20, width=30, bg="grey", activestyle='dotbox', font=new_font)
list_box.pack(side=tk.LEFT, padx=20, pady=20)

# Function to load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
            for task in tasks:
                list_box.insert(tk.END, task)

# Function to save tasks to file
def save_tasks():
    tasks = list_box.get(0, tk.END)  # Get all tasks from the listbox
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        list_box.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Function to remove the selected task
def remove_task():
    try:
        selected_task = list_box.curselection()
        list_box.delete(selected_task)
    except:
        pass

# Function to edit the selected task
def edit_task():
    try:
        selected_task = list_box.curselection()
        new_task = task_entry.get()
        if new_task != "":
            list_box.delete(selected_task)
            list_box.insert(selected_task, new_task)
            task_entry.delete(0, tk.END)
    except:
        pass

# Entry box to input new tasks
task_entry = tk.Entry(root, width=30, font=new_font)
task_entry.pack(pady=10)

# Button to add a task
add_button = tk.Button(root, text="Add Task", command=add_task, font=new_font)
add_button.pack(pady=5)

# Button to remove the selected task
remove_button = tk.Button(root, text="Remove Task", command=remove_task, font=new_font)
remove_button.pack(pady=5)

# Button to edit the selected task
edit_button = tk.Button(root, text="Edit Task", command=edit_task, font=new_font)
edit_button.pack(pady=5)

# Load tasks when the application starts
load_tasks()

# Save tasks when the application is closed
root.protocol("WM_DELETE_WINDOW", lambda: (save_tasks(), root.destroy()))

root.mainloop()
