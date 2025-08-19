# 🏅 Sportify – Sports Court Booking System

Sportify is a **web application** for booking sports courts (football, basketball, tennis, etc.).  
It provides users with an easy way to view available slots and reserve their preferred times.

The project is built with:

- **Frontend:** Vanilla JavaScript, CSS, and TailwindCSS
- **Backend:** Python with Flask
- **Architecture:** Object-Oriented Programming (OOP) to handle dates, time generation, and booking logic

---

## 🚀 Features

- 📅 Generate available booking times dynamically (start from 3 pm until 11 pm where: time now is larger than 2 hours from reserve time)
- 🏟 Reserve courts for different sports
- 👤 User-friendly interface styled with TailwindCSS
- 🧩 OOP-based design for time table and date handling
- 🔗 REST API endpoints built with Flask

---

## 🛠 Tech Stack

- **Frontend:** Vanilla JS, CSS, TailwindCSS
- **Backend:** Python, Flask
- **Data Handling:** JSON files (for now, can be extended to databases later)

---

## 📂 Project Structure

Sportify/
│── api/ api files to handle requests and response
│── json/ # JSON files for reservations and courts and users
│── modules/reserve / # Class Reserve booking & time generation & date handling g
│── static/ # CSS, JS, and images
│── templates/ # HTML pages (Jinja templates for Flask)
│── main.py # Flask entry point
│── README.md # Project documentation

## ⚡ Installation & Setup

```bash
   git clone https://github.com/Ehabzakout/sportify

```

## Install Flask

```bash
  pip install flask

```

## Run

```bash
python main.py

```

## Requirements Checklist

### 🗓 Datetime Module

- Used to generate and save dates in:
  - `/api/booking.py`
  - `/modules/reserve.py`

---

### 🏷 Class Reserve

- Implemented in `/modules/reserve.py`
- Contains:
  - **Properties:** `courtId`, `userId`
  - **Methods:** More than 3 methods for booking and time handling

---

### 💾 Local Storage

- Saves logged user data (`username`, `userId`) in:
  - `/static/js/auth.js` → `login` function

---

### ⚡ Modern JavaScript

- All variables are defined using `let` and `const`

---

### 📂 File Handling

- Reading and writing JSON in the same file:
  - `/api/booking.py` → `create_book` function

---

### 🔁 Control Structures

- Loops and conditional statements used in:
  - `/api/auth/login.py`

---

### 👤 User Registration & Login

- **Register:** `/api/auth/register` → checks if user exists before creating a new one
- **Login:** `/api/auth/login` → authenticates users and returns their info

---

### 🎨 Styling

- TailwindCSS + custom CSS (`/static/css`)

## 👨‍💻 Author

Developed by Ehab Zakout
