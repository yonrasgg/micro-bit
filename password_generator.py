import random
import string

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """Genera una contraseña aleatoria según los requisitos especificados."""
    
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/|"

    all_characters = letters + digits + symbols

    while True:
        password = ''.join(random.choice(all_characters) for _ in range(length))

        if (sum(c.isdigit() for c in password) >= nums and
            sum(c.islower() for c in password) >= lowercase and
            sum(c.isupper() for c in password) >= uppercase and
            sum(c in symbols for c in password) >= special_chars):
            return password