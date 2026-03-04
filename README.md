
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

## 📂 Project Structure

```text
Healthcare Management/
│
├── app.py
├── database/
│   ├── connection.py
│   └── schema.py
├── models/
│   ├── doctor.py
│   ├── patient.py
│   └── appointment.py
├── services/
│   ├── doctor_service.py
│   ├── patient_service.py
│   └── appointment_service.py
├── templates/
│   ├── dashboard.html
│   ├── doctors.html
│   ├── patient.html
│   └── appointments.html
└── static/
```

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
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

For Windows 
```bash
venv\Scripts\activate
```

For Linux/MAC
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in Browser

Open the following URL in your browser:

```text
http://127.0.0.1:5000/
```
The database tables are automatically created on startup.


## 📌 Version History

### ✅ v1.0
- Doctor, Patient, Appointment modules  
- Service-layer architecture  
- Modular backend structure  
- Clean UI layout  

### 🔜 v2.0 (In Progress)
- Billing system  
- Revenue tracking  
- Dashboard analytics  

---

### 📖 Background

An earlier academic version of this project was built collaboratively during undergraduate coursework (2021).

This repository represents a redesigned and independently implemented version with improved architecture, cleaner structure, and extended functionality.

