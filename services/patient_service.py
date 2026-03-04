from database.connection import get_connection
from models.patient import Patient

class PatientService:

    @staticmethod
    def add_patient(patient):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO patients
            (name, age, gender, phone, address, disease, doctor_id, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            patient.name,
            patient.age,
            patient.gender,
            patient.phone,
            patient.address,
            patient.disease,
            patient.doctor_id,
            patient.status
        ))

        conn.commit()
        conn.close()

    @staticmethod
    @staticmethod
    def get_all_patients():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, name, age, gender, phone, address,
                disease, doctor_id, status, created_at
            FROM patients
        """)

        rows = cursor.fetchall()
        conn.close()

        return [
            Patient(
                id=row[0],
                name=row[1],
                age=row[2],
                gender=row[3],
                phone=row[4],
                address=row[5],
                disease=row[6],
                doctor_id=row[7],
                status=row[8],
                created_at=row[9]
            )
            for row in rows
        ]

    @staticmethod
    def delete_patient(patient_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM patients WHERE id=?", (patient_id,))
        conn.commit()
        conn.close()