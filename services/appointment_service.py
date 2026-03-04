from database.connection import get_connection
from models.appointment import Appointment
from datetime import datetime


class AppointmentService:

    @staticmethod
    def book_appointment(appointment: Appointment):

        if not appointment.is_future_date():
            raise ValueError("Appointment must be in the future")

        conn = get_connection()
        cursor = conn.cursor()

        # 🔒 Conflict Check
        cursor.execute("""
            SELECT * FROM appointments
            WHERE doctor_id = ?
            AND appointment_datetime = ?
        """, (appointment.doctor_id, appointment.appointment_datetime))

        conflict = cursor.fetchone()

        if conflict:
            conn.close()
            raise ValueError("Doctor already booked at this time")

        # Insert appointment
        cursor.execute("""
            INSERT INTO appointments (patient_id, doctor_id, appointment_datetime, status)
            VALUES (?, ?, ?, ?)
        """, (
            appointment.patient_id,
            appointment.doctor_id,
            appointment.appointment_datetime,
            appointment.status
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all_appointments():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT a.id, p.name AS patient_name, d.name AS doctor_name,
                   a.appointment_datetime, a.status
            FROM appointments a
            JOIN patients p ON a.patient_id = p.id
            JOIN doctors d ON a.doctor_id = d.id
        """)

        appointments = cursor.fetchall()
        conn.close()
        return appointments