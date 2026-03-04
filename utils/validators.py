import re


def validate_phone(phone: str):
    pattern = r"^[6-9]\d{9}$"
    return re.match(pattern, phone)


def validate_blood_type(blood_type: str):
    valid_types = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    return blood_type in valid_types


def validate_age(age: int):
    return 0 < age < 120