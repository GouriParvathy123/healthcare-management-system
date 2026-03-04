class Doctor:
    def __init__(
        self,
        name,
        specialization,
        age=None,
        phone=None,
        address=None,
        degrees=None,
        cabin_number=None,
        availability="Available",
        id=None,
        created_at=None
    ):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.age = age
        self.phone = phone
        self.address = address
        self.degrees = degrees
        self.cabin_number = cabin_number
        self.availability = availability
        self.created_at = created_at