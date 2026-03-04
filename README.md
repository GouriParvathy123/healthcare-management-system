
# 🏥 Healthcare Management System (HMS) – v1.0

A modular **Healthcare Management System** built using **Flask + SQLite**, designed to manage doctors, patients, and appointments efficiently.

This version is independently designed and implemented with a structured service-layer architecture, improving upon an earlier academic team project (2021) by redesigning and modernizing the system.

---

## 🚀 Features

### 👨‍⚕️ Doctor Management
- Add / delete doctors  
- Update availability  
- Filter by specialization  
- View doctor-specific patients  

### 🧑‍🤝‍🧑 Patient Management
- Add / delete patients  
- Assign doctor  
- Track admission status  

### 📅 Appointment Booking
- Book appointments  
- Prevent scheduling conflicts  
- View all scheduled appointments  

---

## 🧠 Project Architecture

Healthcare Management/
│
├── app.py
├── database/
│ ├── connection.py
│ └── schema.py
├── models/
│ ├── doctor.py
│ ├── patient.py
│ └── appointment.py
├── services/
│ ├── doctor_service.py
│ ├── patient_service.py
│ └── appointment_service.py
├── templates/
│ ├── dashboard.html
│ ├── doctors.html
│ ├── patient.html
│ └── appointments.html
└── static/


## 🛠 Tech Stack

- Python 3  
- Flask  
- SQLite  
- HTML / CSS (Jinja Templates)  
- Git (Version Control)  

---

# ⚙️ How To Run This Project

Follow the steps below to run the application locally.

---

### 1️⃣ Clone the Repository

## 🛠 Tech Stack

- Python 3
- Flask
- SQLite
- HTML / CSS (Jinja Templates)
- Git (Version Control)

---

## ⚙️ How To Run This Project

Follow the steps below to run the application locally.

### 1. Clone the Repository

```bash
git clone https://github.com/GouriParvathy123/healthcare-management-system.git
cd healthcare-management-system
