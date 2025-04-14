
# Registration Form with Tkinter (PYTHON)

This project is a modern, user-friendly registration form built using **Python**, **ttkbootstrap**, and **MongoDB Atlas**. It allows users to input and submit their registration details through a graphical user interface (GUI). Data is validated and stored securely in a MongoDB cloud database.


## 🚀 Features
    - 🧑‍💼 Collects user information:
    - First Name, Last Name
    - Date of Birth
    - Email, Phone Number
    - Address, Gender
    - Password
    - Terms & Conditions checkbox
    - ✅ Form Validation before submission
    - ☁️ Stores data in **MongoDB Atlas**
    - 🎨 Beautiful, modern UI using `ttkbootstrap`
    - 🔒 Secure password input with masked entry
    - 🖼️ Responsive form layout, centered on screen
    - ⚠️ Alerts for errors and successful submissions


# 🛠️ Technologies Used
-------------------------------------------------------------------------------------------------------------------------------------------------------

### 💻 Python
The primary language used for logic, GUI, and database interaction.

### 🧰 Tkinter
Standard GUI library in Python. Used for layout, widgets (Entry, Label, Button), and event handling.

### 🎨 ttkbootstrap
A modern styling wrapper for Tkinter that mimics Bootstrap themes.
- Offers themes like `morph`, `flatly`, etc.
- Built-in `bootstyle` options like `success-round` for rounded buttons.

### 🌐 MongoDB Atlas
Cloud-based NoSQL database used to store registration data.
- Database: `registration_db`
- Collection: `registrations`

### 🔌 pymongo
MongoDB's official Python driver. Used for establishing secure connection and performing database operations.
___________________________________________________________________________________________________________________________________________________________________________

# MongoDB Setup
    -> Create an account on MongoDB Atlas.
    -> Create a cluster and database named registration_db.
    -> Create a collection called registrations.
    -> Get your connection string (something like:
    -> mongodb+srv://<username>:<password>@cluster0.mongodb.net/).

# 🙋‍♂️ Author
Developed by Rahul Ji Ara
