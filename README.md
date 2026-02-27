# 📚 Library Management System (LMS)

### Django Based Full-Stack Web Application for Managing Library Operations

---

## 📌 Overview

The **Library Management System (LMS)** is a full-stack web application developed from scratch to efficiently manage **library operations such as book management, user handling, and borrowing records**.

This project demonstrates:

* 🌐 Full-stack web development
* 🗄️ Database management
* 🔐 Authentication & authorization
* 📊 Real-world CRUD operations

It is designed as a **portfolio-level project**, showcasing practical implementation of backend logic, frontend UI, and database integration.

---

## 🎯 Objectives

* Digitize library operations
* Manage books, users, and transactions
* Provide a structured and scalable system
* Improve efficiency over manual processes

---

## 🚀 Key Features

### 📖 Book Management

* Add new books
* Update book details
* Delete books
* View available books

### 👤 User Management

* User registration
* Login & logout system
* Role-based access (Admin/User)

### 🔄 Borrow & Return System

* Issue books to users
* Track borrowed books
* Return book functionality
* Due tracking (if implemented)

### 📊 Dashboard (if present)

* Overview of books and users
* Activity tracking

---

## 🏗️ Project Architecture

```id="lms123"
LMS/
│
├── app/ / core modules        # Main application logic
│   ├── models.py              # Database models
│   ├── views.py               # Business logic
│   ├── urls.py                # Routing
│
├── templates/                 # HTML templates (UI)
├── static/                    # CSS, JS, assets
│
├── database/ or db.sqlite3    # Database
├── manage.py                  # Entry point
```

---

## 🖥️ Tech Stack

### 🌐 Frontend

* HTML5
* CSS3
* (Optional: Bootstrap for styling)

### ⚙️ Backend

* Python
* Django Framework *(or similar backend based on your project structure)*

### 🗄️ Database

* SQLite (default) / MySQL (if configured)

### 🧰 Tools & Platform

* VS Code
* Git & GitHub
* Browser (Chrome)

---

## 🔄 Application Workflow

```id="flowlms"
1. User/Admin logs into system
2. Admin adds/manages books
3. Users browse available books
4. User requests/borrows book
5. System tracks issued books
6. User returns book
7. Database updates automatically
```

---

## 📂 Core Components Explained

### 📌 `models.py`

Defines:

* Book model (title, author, availability)
* User model (if custom)
* Borrow/Issue model

---

### 📌 `views.py`

Handles:

* User authentication
* Book CRUD operations
* Borrow/return logic
* Request handling

---

### 📌 `urls.py`

* Maps routes to views
* Controls navigation across pages

---

### 📌 `templates/`

* Frontend UI pages
* Forms (login, add book, etc.)
* Dashboard views

---

## 🎨 UI Features

* Clean and structured layout
* Navigation bar for easy access
* Forms for data input
* Tables for displaying records
* User-friendly interface

---

## 🔐 Authentication System

* Secure login/logout
* Password protection
* Session management

---

## 📊 Database Design

### 📚 Book Table

* Book ID
* Title
* Author
* Availability

### 👤 User Table

* User ID
* Username
* Password

### 🔄 Transaction Table

* Issue Date
* Return Date
* Book reference
* User reference

---

## ⚡ Installation & Setup

### 1️⃣ Clone Repository

```bash id="clonelms"
git clone https://github.com/Vaibhav5335/Library_Management_System.git
cd library-management-system
```

---

### 2️⃣ Create Virtual Environment

```bash id="venvlms"
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash id="installlms"
pip install -r requirements.txt
```

---

### 4️⃣ Run Migrations

```bash id="migratelms"
python manage.py migrate
```

---

### 5️⃣ Run Server

```bash id="runlms"
python manage.py runserver
```

---

### 6️⃣ Open in Browser

```id="openlms"
http://127.0.0.1:8000/
```

---

## 📊 Use Cases

* 🏫 Schools & Colleges
* 📚 Public Libraries
* 🧑‍🎓 Student Projects
* 💼 Portfolio Demonstration

---

## 🌟 Highlights

✔ Full-stack CRUD application
✔ Real-world use case
✔ Clean architecture
✔ Beginner to intermediate friendly
✔ Built completely from scratch

---

## 🧩 Future Enhancements

* 📱 Mobile responsive design
* 📊 Analytics dashboard
* 📅 Due date reminders
* 📧 Email notifications
* 🌐 Deployment on cloud

---

## 👨‍💻 Author

**Vaibhav Sharma**

* Full Stack Developer
* Passionate about building real-world applications

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 💡 Final Note

This project demonstrates how a **simple idea like library management** can be transformed into a **fully functional web application** using modern development practices.

A strong addition to any **developer portfolio 🚀**

---
