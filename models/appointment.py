from datetime import datetime


class Appointment:
    def __init__(
        self,
        patient_id: int,
        doctor_id: int,
        appointment_datetime: str,
        status: str = "Scheduled",
        id: int = None
    ):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_datetime = appointment_datetime
        self.status = status

    def is_future_date(self):
        appointment_time = datetime.fromisoformat(self.appointment_datetime)
        return appointment_time > datetime.now()