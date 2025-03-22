import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    
    if name and email and phone:
        with open("registrations.csv", "a") as file:
            file.write(f"{name},{email},{phone}\n")
        messagebox.showinfo("Success", "Registration Successful!")
    else:
        messagebox.showwarning("Error", "All fields are required!")

# Creating the main application window
root = tk.Tk()
root.title("Registration Form")

# Labels
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Phone:").grid(row=2, column=0, padx=10, pady=5)

# Entry fields
entry_name = tk.Entry(root)
entry_email = tk.Entry(root)
entry_phone = tk.Entry(root)

entry_name.grid(row=0, column=1, padx=10, pady=5)
entry_email.grid(row=1, column=1, padx=10, pady=5)
entry_phone.grid(row=2, column=1, padx=10, pady=5)

# Submit Button
tk.Button(root, text="Submit", command=submit_form).grid(row=3, column=1, pady=10)

# Run the application
root.mainloop()
