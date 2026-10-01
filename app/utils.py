import random
import string

def generate_password(length, modes):
    chars = ""
    if "numeric" in modes:
        chars += string.digits
    if "alphabet" in modes:
        chars += string.ascii_letters
    if "special" in modes:
        chars += "!@#$%^&*()-_=+[]{};:,.<>?/"

    if not chars:  # fallback if no option selected
        chars = string.ascii_letters + string.digits

    return ''.join(random.choice(chars) for _ in range(length))
