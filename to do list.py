import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)

def update_task():
    selected_task_index = task_listbox.curselection()
    new_task = task_entry.get()
    if selected_task_index and new_task:
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, new_task)
        task_entry.delete(0, tk.END)

# Create the main application window
app = tk.Tk()
app.title("To-Do List")

# Task Entry
task_entry = tk.Entry(app, width=40)
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(app, text="Add Task", command=add_task)
delete_button = tk.Button(app, text="Delete Task", command=delete_task)
update_button = tk.Button(app, text="Update Task", command=update_task)

add_button.pack()
delete_button.pack()
update_button.pack()

# Task List
task_listbox = tk.Listbox(app, selectmode=tk.SINGLE, height=10, width=40)
task_listbox.pack()

app.mainloop()