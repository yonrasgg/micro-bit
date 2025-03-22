from microbit import *
import random

# Shorter character set to save memory
CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$"

# Basic UART setup - should work for both USB and Bluetooth
uart.init(baudrate=9600)

# Let user know we're ready
display.scroll("Ready")

# Main loop - absolute minimum version
while True:
    if button_a.was_pressed():
        # Generate a simple 8-char password
        pwd = ""
        for i in range(8):
            pwd += CHARS[random.randint(0, len(CHARS)-1)]
        
        # Show password
        display.scroll(pwd[:5] + "...")
    
    if button_b.was_pressed():
        # Check if we have a password
        if 'pwd' in globals() and pwd:
            # Send via UART
            uart.write(pwd)
            display.scroll("Sent")
        else:
            display.scroll("No pwd")
    
    # Sleep to prevent CPU overuse
    sleep(100)
