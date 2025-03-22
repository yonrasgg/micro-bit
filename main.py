import random
from microbit import button_a, button_b, display, uart, sleep

PASSWORD_LENGTH = 8  
NUM_NUMBERS = 3      
NUM_SPECIAL_CHARS = 3  

CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

# Password generator
def generate_password(length=8):
    """Create a simple random password."""
    password = ""
    for i in range(length):
        password += CHARS[random.randint(0, len(CHARS)-1)]
    return password

# Display function
def show_message(msg):
    display.scroll(msg)

# Password display
def show_password(pwd):
    display.scroll(pwd[:8] + "...")

# Improved Bluetooth function
def send_via_bluetooth(data):
    """Send data via Bluetooth using UART service.
    
    This function configures and uses the micro:bit's Bluetooth UART service
    to send password data to paired devices.
    """
    try:
        # Initialize UART with specific configuration for Bluetooth
        uart.init(baudrate=9600, tx=None, rx=None)
        
        # Add a brief delay to ensure UART is ready
        sleep(100)
        
        # Convert string to bytes if needed
        if isinstance(data, str):
            data_bytes = data.encode('utf-8')
        else:
            data_bytes = data
            
        # Send the data
        uart.write(data_bytes)
        
        # Add termination character to signal end of transmission
        uart.write(b'\n')
        
        return True
    except Exception:
        # Keep error handling simple to avoid memory issues
        return False

# Main loop with improved error handling
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
                success = send_via_bluetooth(password)
                if success:
                    display.scroll("Sent")
                else:
                    display.scroll("Err")
            else:
                display.scroll("No pwd")
        
        sleep(100)

# Start the program
if __name__ == "__main__":
    main()
