# Include all necessary code in a single file to avoid import errors

# Configuration constants
PASSWORD_LENGTH = 16
NUM_NUMBERS = 4
NUM_SPECIAL_CHARS = 3

# Environment detection
try:
    import microbit
    from microbit import button_a, button_b, display, uart
    IS_MICROBIT = True
    print("Running on micro:bit hardware")
except ImportError:
    IS_MICROBIT = False
    print("Running in development mode with mock microbit")
    import time
    
    class MockDisplay:
        def scroll(self, text):
            print(f"[DISPLAY] Scrolling: {text}")
    
    class MockButton:
        def __init__(self, name):
            self.name = name
        
        def was_pressed(self):
            return input(f"Press 'y' if button {self.name} was pressed: ").lower() == 'y'

    class MockUart:
        def init(self, baudrate=9600, tx=None, rx=None):
            print(f"[UART] Initialized with baudrate {baudrate}")
        
        def write(self, data):
            if isinstance(data, bytes):
                print(f"[UART] Sending: {data.decode('utf-8', errors='replace')}")
            else:
                print(f"[UART] Sending: {data}")
    
    display = MockDisplay()
    button_a = MockButton('A')
    button_b = MockButton('B')
    uart = MockUart()

# Hardware functions
def sleep(ms):
    if IS_MICROBIT:
        microbit.sleep(ms)
    else:
        time.sleep(ms / 1000)

def show_text(text):
    display.scroll(text)

def button_a_pressed():
    return button_a.was_pressed()

def button_b_pressed():
    return button_b.was_pressed()

def init_bluetooth(baudrate=9600):
    uart.init(baudrate=baudrate, tx=None, rx=None)

def send_bluetooth(data):
    if not IS_MICROBIT and isinstance(data, str):
        data = data.encode()
    uart.write(data)

# Password generator function
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

# Display manager functions
def show_message(message):
    """Muestra un mensaje en la pantalla LED del Micro:bit."""
    show_text(message)

def show_password(password):
    """Muestra la contraseña de manera segura (solo los primeros 5 caracteres)."""
    show_text(password[:5] + "...")

# Button manager function
def wait_for_input():
    """Espera hasta que un botón sea presionado y devuelve cuál fue."""
    while True:
        if button_a_pressed():
            return "A"
        elif button_b_pressed():
            return "B"
        sleep(100)

# Bluetooth manager function
def send_password(password):
    """Envía la contraseña generada a un dispositivo vía Bluetooth."""
    try:
        # Initialize UART over BLE
        init_bluetooth(baudrate=9600)
        # Send password
        send_bluetooth(password)
        show_text("Sent!")
    except Exception as e:
        show_text("Error")
        print("Error al enviar: ", e)

# Main function
def main():
    show_message("Ready")
    password = None  # Initialize password variable
    
    while True:
        show_message("A: Gen / B: Send")
        button = wait_for_input()
        
        if button == "A":
            password = generate_password(PASSWORD_LENGTH, NUM_NUMBERS, NUM_SPECIAL_CHARS)
            show_password(password)
            show_message("Gen OK")

        elif button == "B":
            if password is None:
                show_message("No pwd")
            else:
                send_password(password)
                show_message("Sent")

if __name__ == "__main__":
    main()
