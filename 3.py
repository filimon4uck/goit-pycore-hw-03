import re


def normalize_phone(phone_number):
    pattern = r"[^+0-9]"
    phone_number = re.sub(pattern, "", phone_number)
    if phone_number.startswith("38"):
        phone_number = "+" + phone_number
    elif not phone_number.startswith("+38"):
        phone_number = "+38" + phone_number
    return phone_number
