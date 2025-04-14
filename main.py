import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb+srv://santoshgodiha:Santoshgodiha@saint.txvph.mongodb.net/")
db = client["registration_db"]
collection = db["registrations"]

# Submit Function
def submit_form():
    data = {
        "first_name": entry_fname.get(),
        "last_name": entry_lname.get(),
        "dob": entry_dob.get(),
        "email": entry_email.get(),
        "phone": entry_phone.get(),
        "address": entry_address.get("1.0", 'end-1c'),  # for multiline
        "gender": gender_var.get(),
        "password": entry_password.get(),
        "accepted_terms": terms_var.get()
    }

    # Validation
    if not all([data["first_name"], data["last_name"], data["dob"], data["email"],
                data["phone"], data["address"], data["gender"], data["password"]]):
        messagebox.showwarning("⚠️ Input Error", "All fields are required!")
        return

    if not data["accepted_terms"]:
        messagebox.showwarning("⚠️ Terms & Conditions", "You must accept the terms and conditions.")
        return

    try:
        collection.insert_one(data)
        messagebox.showinfo("✅ Success", "Registration Successful!")
        clear_form()
    except Exception as e:
        messagebox.showerror("❌ Database Error", str(e))

def clear_form():
    for widget in [entry_fname, entry_lname, entry_dob, entry_email, entry_phone, entry_password]:
        widget.delete(0, 'end')
    entry_address.delete("1.0", 'end')
    gender_var.set("")
    terms_var.set(False)

# UI
app = ttk.Window(title="Rahul Ji Ara", themename="morph", size=(800, 700))
app.configure(background="#1E3A8A")  # Optional background

# Container to center all content
container = ttk.Frame(app)
container.pack(expand=True)

# Header
ttk.Label(container, text="Signup Now", font=("Segoe UI", 20, "bold"), background="#dce6f0").pack(pady=10)

# Form Frame
form = ttk.Frame(container, padding=20)
form.pack()

# Input Fields
ttk.Label(form, text="First Name").grid(row=0, column=0, sticky="w", pady=10)
entry_fname = ttk.Entry(form, width=30)
entry_fname.grid(row=0, column=1)

ttk.Label(form, text="Last Name").grid(row=1, column=0, sticky="w", pady=10)
entry_lname = ttk.Entry(form, width=30)
entry_lname.grid(row=1, column=1)

ttk.Label(form, text="Date of Birth").grid(row=2, column=0, sticky="w", pady=10)
entry_dob = ttk.Entry(form, width=30)
entry_dob.grid(row=2, column=1)

ttk.Label(form, text="Email").grid(row=3, column=0, sticky="w", pady=10)
entry_email = ttk.Entry(form, width=30)
entry_email.grid(row=3, column=1)

ttk.Label(form, text="Phone").grid(row=4, column=0, sticky="w", pady=10)
entry_phone = ttk.Entry(form, width=30)
entry_phone.grid(row=4, column=1)

ttk.Label(form, text="Address").grid(row=5, column=0, sticky="nw", pady=10)
entry_address = ttk.Text(form, width=30, height=2)
entry_address.grid(row=5, column=1, pady=5)

# Gender
ttk.Label(form, text="Gender").grid(row=6, column=0, sticky="w", pady=10)
gender_var = ttk.StringVar()
ttk.Radiobutton(form, text="Male", variable=gender_var, value="Male").grid(row=6, column=1, sticky="w")
ttk.Radiobutton(form, text="Female", variable=gender_var, value="Female").grid(row=6, column=1)
ttk.Radiobutton(form, text="Other", variable=gender_var, value="Other").grid(row=6, column=1, sticky="e")

# Password
ttk.Label(form, text="Password").grid(row=7, column=0, sticky="w", pady=10)
entry_password = ttk.Entry(form, show="*", width=30)
entry_password.grid(row=7, column=1)

# Terms & Conditions
terms_var = ttk.BooleanVar()
ttk.Checkbutton(form, text="I agree to the Terms & Conditions", variable=terms_var).grid(row=8, columnspan=2, pady=10)

# Submit
ttk.Button(container, 
text="Submit", bootstyle="success", command=submit_form, width=25, padding=(10, 10)).pack(pady=20)

# Run the app
app.mainloop()
