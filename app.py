from flask import Flask, render_template, request, redirect
from database.schema import create_tables
from services.patient_service import PatientService
from services.appointment_service import AppointmentService
from services.doctor_service import DoctorService
from models.patient import Patient
from models.appointment import Appointment
from models.doctor import Doctor

app = Flask(__name__)

# Create tables on startup
create_tables()


# ==========================
# DASHBOARD
# ==========================
@app.route("/")
def dashboard():
    return render_template("dashboard.html")


# ==========================
# DOCTORS SECTION
# ==========================
@app.route("/doctors", methods=["GET"])
def view_doctors():
    specialization = request.args.get("specialization")

    specializations = DoctorService.get_all_specializations()

    doctors = []
    if specialization:
        doctors = DoctorService.get_doctors_by_specialization(specialization)
    else:
        doctors = DoctorService.get_all_doctors()

    return render_template(
        "doctors.html",
        doctors=doctors,
        specializations=specializations,
        selected_specialization=specialization
    )


@app.route("/add_doctor", methods=["POST"])
def add_doctor():
    doctor = Doctor(
        name=request.form["name"],
        specialization=request.form["specialization"],
        availability=request.form.get("availability", "Available")
    )

    DoctorService.add_doctor(doctor)
    return redirect("/doctors")

@app.route("/delete_doctor", methods=["POST"])
def delete_doctor():
    doctor_id = request.form["doctor_id"]
    DoctorService.delete_doctor(doctor_id)
    return redirect("/doctors")

@app.route("/update_availability", methods=["POST"])
def update_availability():
    doctor_id = request.form["doctor_id"]
    status = request.form["status"]

    DoctorService.update_availability(doctor_id, status)
    return redirect("/doctors")


@app.route("/doctor/<int:doctor_id>")
def doctor_detail(doctor_id):
    doctor = DoctorService.get_doctor_by_id(doctor_id)
    patients = PatientService.get_all_patients()

    return render_template(
        "doctor_detail.html",
        doctor=doctor,
        patients=patients
    )

# ==========================
# PATIENTS SECTION
# ==========================
from models.patient import Patient
from services.patient_service import PatientService

@app.route("/patients")
def patients():
    patients = PatientService.get_all_patients()
    doctors = DoctorService.get_all_doctors()
    return render_template("patient.html", patients=patients, doctors=doctors)


@app.route("/add_patient", methods=["POST"])
def add_patient():
    patient = Patient(
        name=request.form["name"],
        age=request.form.get("age"),
        gender=request.form.get("gender"),
        phone=request.form.get("phone"),
        address=request.form.get("address"),
        disease=request.form.get("disease"),
        doctor_id=request.form.get("doctor_id"),
        status=request.form.get("status", "Admitted")
    )

    PatientService.add_patient(patient)
    return redirect("/patients")


@app.route("/delete_patient", methods=["POST"])
def delete_patient():
    PatientService.delete_patient(request.form["patient_id"])
    return redirect("/patients")

# ==========================
# APPOINTMENTS SECTION
# ==========================
@app.route("/appointments")
def view_appointments():
    appointments = AppointmentService.get_all_appointments()
    patients = PatientService.get_all_patients()
    doctors = DoctorService.get_all_doctors()

    return render_template(
        "appointments.html",
        appointments=appointments,
        patients=patients,
        doctors=doctors
    )

@app.route("/book_appointment", methods=["POST"])
def book_appointment():
    appointment = Appointment(
        patient_id=int(request.form["patient_id"]),
        doctor_id=int(request.form["doctor_id"]),
        appointment_datetime=request.form["appointment_datetime"]
    )

    try:
        AppointmentService.book_appointment(appointment)
    except ValueError as e:
        return str(e)

    return redirect("/appointments")


# ==========================
# RUN SERVER
# ==========================
if __name__ == "__main__":
    app.run(debug=True)