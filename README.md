📝 Project Description: MongoDB-Connected Registration Form using Tkinter and ttkbootstrap
This application is a graphical user interface (GUI) registration form built using Python that collects user data including first name, last name, date of birth, contact information, gender, password, and more. The data is validated locally and stored in a MongoDB Atlas cloud database. The UI is designed with a modern look using ttkbootstrap, a stylish extension of the traditional Tkinter library.

🔧 Technologies Used & Explanation
1. Python
Core programming language used for building both the GUI and backend logic.

Offers extensive support for third-party libraries and database integration.

2. Tkinter
Standard Python library for GUI development.

Provides basic widgets like labels, buttons, text entries, and layout controls.

Acts as the backbone of the form interface.

3. ttkbootstrap
A modern styling layer built on top of ttk (Themed Tkinter).

Provides pre-styled widgets using Bootstrap-like themes (morph, cyborg, flatly, etc.).

Offers bootstyle options like success-round, info-outline, and more for visually appealing components.

Supports variable font sizes, padding, and icon integration, allowing you to mimic CSS-style buttons and inputs.

4. MongoDB Atlas
A cloud-based NoSQL database used to store the form submissions.

The pymongo driver is used to connect the Python application to MongoDB.

Offers high scalability, schema-less flexibility, and secure remote data storage.

Ensures that user data (name, DOB, address, etc.) is stored in structured document format (BSON/JSON-like).

5. pymongo
The official Python driver for MongoDB.

Handles CRUD operations (Create, Read, Update, Delete) with MongoDB databases.

In this app, it's used to insert validated user data into the registration_db.registrations collection.

✅ Features Implemented
Custom-styled and centered form layout.

All input fields validated before submission.

User-friendly error and success pop-ups using messagebox.

Cloud database integration for real-time data collection.

Rounded, styled buttons and modern form layout.

If you’d like, I can generate a README.md for this project, or help you convert this into an executable (.exe) for sharing.


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
