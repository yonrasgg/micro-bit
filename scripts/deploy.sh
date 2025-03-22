#!/bin/bash

echo "Deploying absolute minimal password generator..."

# Get project root
PROJECT_ROOT="$(dirname "$(dirname "$(readlink -f "$0")")")"

# Create temporary minimal file
TMP_PY="${PROJECT_ROOT}/minimal.py"

cat > "${TMP_PY}" << 'EOF'
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
EOF

echo "Deploying with uflash..."
python -m uflash "${TMP_PY}"

if [ $? -eq 0 ]; then
    echo "Deployment successful!"
    echo ""
    echo "PAIRING INSTRUCTIONS:"
    echo "1. After the micro:bit starts, it will show 'Ready'"
    echo "2. To pair with your phone or computer:"
    echo "   - Press and hold both A and B buttons simultaneously"
    echo "   - Keep holding for 3-5 seconds until you see a Bluetooth symbol"
    echo "   - This activates the micro:bit's built-in pairing mode"
    echo "3. On your device, scan for Bluetooth devices and select 'BBC micro:bit'"
    echo ""
    echo "USAGE:"
    echo "- Press A to generate a password (first 5 characters shown)"
    echo "- Press B to send the current password via Bluetooth UART"
    
    # Cleanup
    rm "${TMP_PY}"
else
    echo "Deployment failed."
    rm "${TMP_PY}"
    exit 1
fi
