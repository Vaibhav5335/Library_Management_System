# 📚 Library Management System (LMS)

### Full-Stack Django Web Application for Managing Library Operations

---

## 📌 Overview

The **Library Management System (LMS)** is a full-stack web application built using **Django** that enables efficient management of **books, users, and borrowing activities** in a library.

This project simulates a real-world system where:

* 📖 Books are managed digitally
* 👤 Users can interact with the system
* 🔄 Borrowing and returning is tracked

It demonstrates:

* 🌐 Full-stack web development
* 🗄️ Database design and integration
* 🔐 Authentication system
* 📊 CRUD operations

---

## 🎯 Objectives

* Digitize traditional library operations
* Manage books and users efficiently
* Track book issuing and returning
* Provide a clean and functional UI

---

## 🚀 Key Features

### 📖 Book Management

* Add new books
* Update book details
* Delete books
* View available books

---

### 👤 User Management

* User registration
* Login and logout
* Session-based authentication

---

### 🔄 Issue & Return System

* Issue books to users
* Track borrowed books
* Return functionality
* Availability status updates

---

### 📊 Admin Control

* Manage all records
* Control users and books
* Monitor system activity

---

## 🏗️ Project Structure

```id="lmsrealstruct"
Library_Management_System/
│
├── LMS/                        # Main Django project
│   ├── settings.py
│   ├── urls.py
│
├── library/                   # Main app
│   ├── models.py              # Database models
│   ├── views.py               # Business logic
│   ├── urls.py                # App routing
│   ├── admin.py               # Admin panel config
│
├── templates/                 # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── book_list.html
│
├── static/                    # CSS, JS, assets
│
├── db.sqlite3                 # Database
├── manage.py                  # Entry point
```

---

## 🧠 System Architecture

### 🔄 Application Flow

```id="lmsflowreal"
1. User registers or logs in
2. System authenticates user
3. User accesses dashboard
4. Admin manages books
5. Users view/borrow books
6. System updates database
7. Books returned and status updated
```

---

## 🖥️ Tech Stack

### ⚙️ Backend

* Python
* Django Framework

---

### 🌐 Frontend

* HTML5
* CSS3
* Django Templates

---

### 🗄️ Database

* SQLite (default Django DB)

---

## 📂 Core Components Explained

### 📌 `models.py`

Defines core database structure:

* Book model (title, author, availability)
* User model (Django default/custom)
* Issue/Borrow model

---

### 📌 `views.py`

Handles:

* Authentication logic
* Book CRUD operations
* Issue/return functionality
* Rendering templates

---

### 📌 `urls.py`

* Routes requests to views
* Controls navigation

---

### 📌 `admin.py`

* Enables admin panel management
* Allows managing models via Django admin

---

### 📌 `templates/`

Contains:

* Login & Register pages
* Dashboard UI
* Book listing pages

---

## 🎨 UI Features

* Clean and structured layout
* Navigation-based interface
* Forms for input
* Tables for displaying data
* User-friendly experience

---

## 🔐 Authentication System

* Secure login/logout
* Django authentication system
* Session management
* Protected routes

---

## 📊 Database Design

### 📚 Book Table

* Title
* Author
* Availability status

---

### 👤 User Table

* Username
* Password
* Email

---

### 🔄 Issue Table

* User reference
* Book reference
* Issue date
* Return date

---

## ⚡ Installation & Setup

### 1️⃣ Clone Repository

```bash id="lmsclone2"
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
```

---

### 2️⃣ Create Virtual Environment

```bash id="lmsvenv2"
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash id="lmsinstall2"
pip install django
```

---

### 4️⃣ Run Migrations

```bash id="lmsmigrate2"
python manage.py migrate
```

---

### 5️⃣ Create Superuser (Optional)

```bash id="lmssuper"
python manage.py createsuperuser
```

---

### 6️⃣ Run Server

```bash id="lmsrun2"
python manage.py runserver
```

---

### 7️⃣ Open in Browser

```id="lmsopen2"
http://127.0.0.1:8000/
```

---

## 📊 Use Cases

* 🏫 School/College libraries
* 📚 Small library systems
* 🎓 Academic projects
* 💼 Full-stack portfolio

---

## 🌟 Highlights

✔ Full-stack Django application
✔ Real-world system implementation
✔ Authentication + CRUD operations
✔ Clean architecture
✔ Beginner to intermediate level

---

## 🧩 Future Enhancements

* 📱 Responsive UI
* 📊 Analytics dashboard
* 📧 Email notifications
* 🌐 Cloud deployment
* 🔐 Role-based access (Admin/User)

---

## 👨‍💻 Author

**Vaibhav Sharma**

* Full Stack Developer
* Passionate about building real-world systems

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 💡 Final Note

This project demonstrates how to build a **complete library management system** using Django, combining backend logic, database management, and frontend UI.

A strong addition to your **full-stack developer portfolio 🚀**

---
