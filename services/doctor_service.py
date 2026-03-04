from database.connection import get_connection
from models.doctor import Doctor


class DoctorService:

    @staticmethod
    def add_doctor(doctor):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO doctors
            (name, specialization, age, phone, address, degrees, cabin_number, availability)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            doctor.name,
            doctor.specialization,
            doctor.age,
            doctor.phone,
            doctor.address,
            doctor.degrees,
            doctor.cabin_number,
            doctor.availability
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all_doctors():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, name, specialization, availability
            FROM doctors
        """)

        rows = cursor.fetchall()
        conn.close()

        # Convert DB rows → Doctor objects
        return [
            Doctor(id=row[0], name=row[1], specialization=row[2], availability=row[3])
            for row in rows
        ]

    @staticmethod
    def get_doctors_by_specialization(specialization):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, name, specialization, availability
            FROM doctors
            WHERE specialization = ?
        """, (specialization,))

        rows = cursor.fetchall()
        conn.close()

        return [
            Doctor(id=row[0], name=row[1], specialization=row[2], availability=row[3])
            for row in rows
        ]

    @staticmethod
    def get_all_specializations():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT DISTINCT specialization FROM doctors
        """)

        specializations = cursor.fetchall()
        conn.close()

        return [spec[0] for spec in specializations]

    @staticmethod
    def update_availability(doctor_id, status):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE doctors
            SET availability = ?
            WHERE id = ?
        """, (status, doctor_id))

        conn.commit()
        conn.close()

    @staticmethod
    def get_doctor_by_id(doctor_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, name, specialization, availability
            FROM doctors
            WHERE id = ?
        """, (doctor_id,))

        row = cursor.fetchone()
        conn.close()

        if row:
            return Doctor(id=row[0], name=row[1], specialization=row[2], availability=row[3])
        return None
    
    @staticmethod
    def delete_doctor(doctor_id):
        conn = get_connection()
        cursor = conn.cursor()

        # First delete related appointments
        cursor.execute("""
            DELETE FROM appointments
            WHERE doctor_id = ?
        """, (doctor_id,))

        # Then remove doctor from patients (set doctor_id NULL)
        cursor.execute("""
            UPDATE patients
            SET doctor_id = NULL
            WHERE doctor_id = ?
        """, (doctor_id,))

        # Finally delete doctor
        cursor.execute("""
            DELETE FROM doctors
            WHERE id = ?
        """, (doctor_id,))

        conn.commit()
        conn.close()