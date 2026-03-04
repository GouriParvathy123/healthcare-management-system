from database.connection import get_connection  # pyright: ignore[reportMissingImports]


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # -------------------------
    # Doctors Table (CREATE FIRST - because patients references it)
    # -------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialization TEXT NOT NULL,
        age INTEGER,
        phone TEXT,
        address TEXT,
        degrees TEXT,
        cabin_number TEXT,
        availability TEXT DEFAULT 'Available',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
""")
    # -------------------------
    # Patients Table
    # -------------------------
    cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    phone TEXT,
    address TEXT,
    disease TEXT,
    doctor_id INTEGER,
    status TEXT DEFAULT 'Admitted',
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (doctor_id) REFERENCES doctors(id)
)
""")
    # -------------------------
    # Appointments Table
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            doctor_id INTEGER NOT NULL,
            appointment_datetime TEXT NOT NULL,
            status TEXT DEFAULT 'Scheduled',

            FOREIGN KEY(patient_id) REFERENCES patients(id),
            FOREIGN KEY(doctor_id) REFERENCES doctors(id)
        )
    """)

    conn.commit()
    conn.close()