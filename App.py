import tkinter as tk
from tkinter import messagebox
import json

def save_password():
    """Save a password entry to a JSON file."""
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if not website or not username or not password:
        messagebox.showwarning("Warning", "Please fill out all fields.")
        return

    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data.update(new_data)

    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)

    entry_website.delete(0, tk.END)
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

    messagebox.showinfo("Success", "Password saved!")

def create_password_manager():
    """Create a simple password manager GUI."""
    root = tk.Tk()
    root.title("Password Manager")

    global entry_website, entry_username, entry_password

    tk.Label(root, text="Website:").grid(row=0, column=0, pady=5)
    entry_website = tk.Entry(root, width=35)
    entry_website.grid(row=0, column=1, pady=5)

    tk.Label(root, text="Username:").grid(row=1, column=0, pady=5)
    entry_username = tk.Entry(root, width=35)
    entry_username.grid(row=1, column=1, pady=5)

    tk.Label(root, text="Password:").grid(row=2, column=0, pady=5)
    entry_password = tk.Entry(root, width=35)
    entry_password.grid(row=2, column=1, pady=5)

    tk.Button(root, text="Save Password", command=save_password).grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_password_manager()
