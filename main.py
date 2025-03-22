# Ultra-simplified version to avoid 504 errors

# Import only what's absolutely needed for microbit
import random
from microbit import button_a, button_b, display, uart, sleep

# Simple fixed constants - no conditionals
PASSWORD_LENGTH = 8  # Reduced from 16 to use less memory
NUM_NUMBERS = 2      # Reduced from 4
NUM_SPECIAL_CHARS = 1  # Reduced from 3

# Character sets - minimal versions
CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

# Super simple password generator
def generate_password(length=8):
    """Create a simple random password."""
    password = ""
    for i in range(length):
        password += CHARS[random.randint(0, len(CHARS)-1)]
    return password

# Minimal display function
def show_message(msg):
    display.scroll(msg)

# Minimal password display
def show_password(pwd):
    display.scroll(pwd[:5] + "...")

# Minimal Bluetooth function
def send_via_bluetooth(data):
    uart.init(baudrate=9600)
    uart.write(data)

# Main loop - ultra simplified
def main():
    display.scroll("Ready")
    password = None
    
    while True:
        if button_a.was_pressed():
            password = generate_password(PASSWORD_LENGTH)
            show_password(password)
            display.scroll("OK")
        
        if button_b.was_pressed():
            if password:
                try:
                    send_via_bluetooth(password)
                    display.scroll("Sent")
                except:
                    display.scroll("Err")
            else:
                display.scroll("No pwd")
        
        sleep(100)

# Start the program
if __name__ == "__main__":
    main()
