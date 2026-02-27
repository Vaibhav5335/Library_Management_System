# 📚 Library Management System (LMS)

The **Library Management System (LMS)** is a full-stack Django-based web application designed to digitize and streamline library operations. It provides a centralized platform for managing books, users, and borrowing activities with a clean interface and efficient backend logic.

This system transforms traditional manual library workflows into a **smart, automated, and scalable digital solution**, improving accessibility, tracking, and management efficiency.

Built using Django, the application integrates authentication, database management, and dynamic UI rendering to deliver a seamless experience for both administrators and users.

---

<p align="center">
  <strong>📖 Library Management System</strong><br/>
  <em>A Complete Digital Solution for Smart Library Operations</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/Django-Framework-green?style=flat-square&logo=django"/>
  <img src="https://img.shields.io/badge/SQLite-Database-lightgrey?style=flat-square&logo=sqlite"/>
  <img src="https://img.shields.io/badge/HTML-CSS-orange?style=flat-square&logo=html5"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square"/>
</p>

---

## 📋 Table of Contents

* [Overview](#-overview)
* [Key Features](#-key-features)
* [Technology Stack](#-technology-stack)
* [Architecture](#-architecture)
* [Core Modules](#-core-modules)
* [Database Schema](#-database-schema)
* [Application Flow](#-application-flow)
* [Project Structure](#-project-structure)
* [Getting Started](#-getting-started)

---

## 🌟 Overview

The **Library Management System** is designed to handle all essential library operations in a structured and efficient manner. It allows administrators to manage books and users while enabling users to browse, borrow, and return books seamlessly.

The system follows a **Model-View-Template (MVT)** architecture powered by Django, ensuring clear separation between business logic, database models, and user interface.

Key goals of this system:

* 📚 Simplify book management
* 👤 Manage user interactions
* 🔄 Automate borrowing workflows
* 📊 Maintain accurate records

---

## ✨ Key Features

| Feature                 | Description                          |
| ----------------------- | ------------------------------------ |
| 📖 Book Management      | Add, update, delete, and view books  |
| 👤 User Authentication  | Secure login and registration system |
| 🔄 Borrow & Return      | Track issued books and returns       |
| 📊 Admin Control        | Full control over books and users    |
| 🗄 Database Integration | Persistent storage using SQLite      |
| 🎨 Clean UI             | Simple and user-friendly interface   |

---

## 🛠 Technology Stack

| Layer                 | Technology      | Purpose                  |
| --------------------- | --------------- | ------------------------ |
| **Backend**           | Python + Django | Business logic & routing |
| **Frontend**          | HTML, CSS       | UI rendering             |
| **Database**          | SQLite          | Data storage             |
| **Framework Pattern** | Django MVT      | Structured architecture  |

---

## 🏗 Architecture

The system follows Django’s **MVT Architecture**:

```
┌──────────────────────────────┐
│        User Interface        │
│     (HTML Templates)        │
└─────────────┬────────────────┘
              │
              ▼
┌──────────────────────────────┐
│           Views              │
│   Business Logic & Control   │
└─────────────┬────────────────┘
              │
              ▼
┌──────────────────────────────┐
│           Models             │
│   Database Structure (ORM)   │
└──────────────────────────────┘
```

---

## 📦 Core Modules

### 📖 1. Book Management

* Add new books
* Edit book details
* Delete books
* Track availability

---

### 👤 2. User Management

* User registration
* Login/logout system
* Session handling

---

### 🔄 3. Borrow & Return System

* Issue books to users
* Track borrowing history
* Return books
* Update availability

---

### 🛠 4. Admin Panel

* Manage all records
* Monitor system activity
* Django admin integration

---

## 🗄 Database Schema

### 📚 Book Table

* ID
* Title
* Author
* Availability

### 👤 User Table

* Username
* Email
* Password

### 🔄 Issue Table

* User reference
* Book reference
* Issue date
* Return date

---

## 🔄 Application Flow

```
User Registers/Login
        ↓
Access Dashboard
        ↓
View Books
        ↓
Borrow Book
        ↓
System Updates Database
        ↓
Return Book
        ↓
Availability Updated
```

---

## 📁 Project Structure

```
Library_Management_System/
│
├── LMS/                    # Main Django project
│   ├── settings.py
│   ├── urls.py
│
├── library/                # Core app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│
├── templates/              # UI Templates
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── book_list.html
│
├── static/                 # CSS/JS
├── db.sqlite3              # Database
├── manage.py               # Entry point
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8+
* Django installed

---

### Installation

```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
```

```bash
pip install django
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

---

### Access Application

```
http://127.0.0.1:8000/
```

---

## 🌟 Highlights

✔ Full-stack Django application
✔ Real-world project use case
✔ Authentication + CRUD operations
✔ Clean architecture
✔ Portfolio-ready

---

## 💡 Final Note

The **Library Management System** showcases how traditional systems can be transformed into efficient digital solutions using modern web technologies.

It reflects strong understanding of:

* Backend development
* Database management
* Full-stack architecture

---

<p align="center">
  Built with ❤️ using Django & Python  
</p>
