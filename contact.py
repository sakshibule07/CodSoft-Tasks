import tkinter as tk
from tkinter import messagebox

# Define functions for contact operations
contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name and phone:
        contact = {"Name": name, "Phone": phone,"Email": email}
        contacts.append(contact)
        update_contact_listbox()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required fields.")

def update_contact():
    selected_contact_index = contact_listbox.curselection()
    if selected_contact_index:
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()

        if name and phone:
            selected_contact = contacts[selected_contact_index[0]]
            selected_contact["Name"] = name
            selected_contact["Phone"] = phone
            selected_contact["Email"] = email
            update_contact_listbox()
            clear_entries()
        else:
            messagebox.showwarning("Input Error", "Name and Phone are required fields.")

def delete_contact():
    selected_contact_index = contact_listbox.curselection()
    if selected_contact_index:
        contacts.pop(selected_contact_index[0])
        update_contact_listbox()
        clear_entries()

def search_contact():
    search_text = search_entry.get().lower()
    search_results = [contact for contact in contacts if search_text in contact["Name"].lower()]
    update_contact_listbox(search_results)

def update_contact_listbox(contact_list=contacts):
    contact_listbox.delete(0, tk.END)
    for contact in contact_list:
        contact_listbox.insert(tk.END, contact["Name"])

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

# Create the main application window
app = tk.Tk()
app.title("Contact Book")

# Contact Entry Fields
name_label = tk.Label(app, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1)

phone_label = tk.Label(app, text="Phone:")
phone_label.grid(row=1, column=0)
phone_entry = tk.Entry(app)
phone_entry.grid(row=1, column=1)

email_label = tk.Label(app, text="Email:")
email_label.grid(row=2, column=0)
email_entry = tk.Entry(app)
email_entry.grid(row=2, column=1)

# Buttons
add_button = tk.Button(app, text="Add Contact", command=add_contact)
update_button = tk.Button(app, text="Update Contact", command=update_contact)
delete_button = tk.Button(app, text="Delete Contact", command=delete_contact)
search_button = tk.Button(app, text="Search", command=search_contact)

add_button.grid(row=3, column=0)
update_button.grid(row=3, column=1)
delete_button.grid(row=3, column=2)
search_button.grid(row=4, column=1)

# Contact List
contact_listbox = tk.Listbox(app, selectmode=tk.SINGLE, height=10, width=40)
contact_listbox.grid(row=5, columnspan=2)

# Search Entry Field
search_label = tk.Label(app, text="Search:")
search_label.grid(row=4, column=0)
search_entry = tk.Entry(app)
search_entry.grid(row=4, column=1)

# Initialize the contact listbox
update_contact_listbox()

app.mainloop()








