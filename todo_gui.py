import tkinter as tk

# Function to add a task
def submit_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)

# Function to edit a task
def edit_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        selected_task_index = int(selected_task_index[0])
        updated_task = entry.get()
        if updated_task:
            task_list.delete(selected_task_index)
            task_list.insert(selected_task_index, updated_task)
            entry.delete(0, tk.END)

# Function to delete a task
def delete_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index[0])

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Set the window size to 500x300
root.geometry("420x500")

# Add a green-bordered label at the top
title_label = tk.Label(root, text="To-Do List", font=("Arial", 24, "bold"))
title_label.config(bg="lightgreen", bd=20)
title_label.pack(fill=tk.X)

# Add items section
add_item_label = tk.Label(root, text="Add Items")
add_item_label.pack()

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit_task)
submit_button.pack()

# Task list section
task_label = tk.Label(root, text="Tasks")
task_label.pack()

task_list = tk.Listbox(root, selectmode=tk.SINGLE)
task_list.pack()

edit_button = tk.Button(root, text="Edit Task", command=edit_task)
edit_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

root.mainloop()

