from password_generator import generate_password
from bluetooth_manager import send_password
from display_manager import show_message, show_password
from button_manager import wait_for_input
from config import PASSWORD_LENGTH, NUM_NUMBERS, NUM_SPECIAL_CHARS

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
