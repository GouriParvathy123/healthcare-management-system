from faker import Faker
import random
import sqlite3

fake = Faker()

DB_PATH = "healthcare.db"  # Change if your DB path is different

specializations = [
    "Cardiology", "Neurology", "Orthopedics", "Pediatrics",
    "Dermatology", "Oncology", "Gynecology", "Urology",
    "Psychiatry", "ENT", "Radiology", "Gastroenterology",
    "Pulmonology", "Endocrinology", "Nephrology"
]

genders = ["Male", "Female", "Other"]

def seed_doctors(cursor):
    for _ in range(100):
        name = fake.name()
        specialization = random.choice(specializations)
        age = random.randint(30, 65)
        phone = fake.phone_number()
        address = fake.address().replace("\n", ", ")
        degrees = random.choice(["MBBS", "MD", "MBBS, MD", "MBBS, MS", "MBBS, DM"])
        cabin_number = f"C-{random.randint(1,50)}"
        availability = random.choice(["Available", "Not Available"])

        cursor.execute("""
            INSERT INTO doctors
            (name, specialization, age, phone, address, degrees, cabin_number, availability)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, specialization, age, phone, address, degrees, cabin_number, availability))


def seed_patients(cursor):
    doctor_ids = [row[0] for row in cursor.execute("SELECT id FROM doctors").fetchall()]

    for _ in range(250):
        name = fake.name()
        age = random.randint(1, 90)
        gender = random.choice(genders)
        phone = fake.phone_number()
        address = fake.address().replace("\n", ", ")
        disease = fake.word().capitalize()
        doctor_id = random.choice(doctor_ids)
        status = random.choice(["Admitted", "Discharged"])

        cursor.execute("""
            INSERT INTO patients
            (name, age, gender, phone, address, disease, doctor_id, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, age, gender, phone, address, disease, doctor_id, status))


def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("Seeding Doctors...")
    seed_doctors(cursor)

    print("Seeding Patients...")
    seed_patients(cursor)

    conn.commit()
    conn.close()

    print("Database seeded successfully!")


if __name__ == "__main__":
    main()