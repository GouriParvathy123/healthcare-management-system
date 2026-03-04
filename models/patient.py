class Patient:
    def __init__(
        self,
        name,
        age=None,
        gender=None,
        phone=None,
        address=None,
        disease=None,
        doctor_id=None,
        status="Admitted",
        id=None,
        created_at=None
    ):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.address = address
        self.disease = disease
        self.doctor_id = doctor_id
        self.status = status
        self.created_at = created_at