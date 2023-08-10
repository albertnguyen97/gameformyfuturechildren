import tkinter as tk
from tkinter import Listbox


def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)


def remove_item():
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)


root = tk.Tk()
root.title("List GUI Example")

# Create a Listbox
listbox = Listbox(root, selectmode=tk.SINGLE)
listbox.pack(padx=10, pady=10)

# Create an Entry widget for input
entry = tk.Entry(root)
entry.pack(padx=10, pady=5)

# Create buttons to add and remove items
add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack(padx=10, pady=5)

remove_button = tk.Button(root, text="Remove Selected", command=remove_item)
remove_button.pack(padx=10, pady=5)


root.mainloop()