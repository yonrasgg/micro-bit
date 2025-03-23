from microbit import *
import random

# Shorter character set to save memory
CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$"

# Initialize regular UART - we'll use a different approach for BLE
uart.init(baudrate=9600)

# Let user know we're ready
display.scroll("Ready")
display.show(Image.HEART)

# Main loop
while True:
    if button_a.was_pressed():
        # Generate a simple 8-char password
        pwd = ""
        for i in range(8):
            pwd += CHARS[random.randint(0, len(CHARS)-1)]
        
        # Show password
        display.scroll(pwd)
        display.show(Image.YES)
    
    if button_b.was_pressed():
        # Check if we have a password
        if 'pwd' in globals() and pwd:
            try:
                # For BLE UART, the best approach is to use the built-in radio module
                # which is automatically bridged to BLE in special firmware builds
                import radio
                radio.on()
                radio.config(group=1)
                radio.send(pwd)
                display.scroll("Sent")
                display.show(Image.YES)
            except Exception as e:
                # Fall back to regular UART if radio module fails
                uart.write(bytes(pwd + "\r\n", 'utf-8'))
                display.scroll("USB")
        else:
            display.scroll("No pwd")
    
    # Check for pairing sequence (A+B pressed together)
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.DIAMOND)
        sleep(1000)  # Wait to see if buttons remain pressed
        if button_a.is_pressed() and button_b.is_pressed():
            # This is primarily a visual indicator, actual pairing mode
            # is handled by the firmware layer
            display.show(Image.DIAMOND_SMALL)
            sleep(3000)
            display.scroll("BT PAIR")
    
    # Sleep to prevent CPU overuse
    sleep(100)
