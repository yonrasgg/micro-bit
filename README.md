# Micro:bit Password Generator and Manager

## Overview

This project turns your BBC micro:bit into a portable password generator and manager. Using the built-in buttons and Bluetooth capabilities, you can:

1. Generate secure random passwords
2. View passwords on the LED display 
3. Send passwords via Bluetooth to your paired devices

Perfect for quickly generating secure passwords when you're away from your computer, or for securely transferring passwords to your phone or tablet.

## How It Works

The micro:bit runs a simple but effective password generator that creates randomized 8-character passwords containing a mix of letters, numbers, and special characters. The password is then either displayed on the micro:bit's LED screen or transmitted via Bluetooth.

### Project Structure

```
/micro-bit/
├── main.py                # All the code that runs on the micro:bit
├── scripts/               # Helper scripts for your computer
│   ├── install_tools.sh   # Sets up the development tools
│   └── deploy.sh          # Transfers the code to your micro:bit
├── README.md              # This documentation
└── requirements.txt       # Python package dependencies
```

## Features in Detail

### Password Generation
When you press button A, the micro:bit creates a random 8-character password with:
- Uppercase and lowercase letters
- Numbers
- Special characters like !@#$%^&*()

For security reasons, only the first 5 characters of the password are shown on the display, followed by "..." to indicate there are more characters.

### Bluetooth Transfer
When you press button B, the micro:bit sends the most recently generated password over Bluetooth. This allows you to:
- Transfer passwords to your phone or tablet
- Use generated passwords without having to type them manually
- Share passwords securely between devices

## Getting Started

### What You'll Need
- A BBC micro:bit (any version)
- USB cable to connect to your computer
- A computer with Python installed
- A device with Bluetooth for receiving passwords (optional)

### Setting Up Your Development Environment

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/micro-bit-password-generator.git
   cd micro-bit
   ```

2. **Create a Python virtual environment:**
   This keeps the project dependencies separate from your system Python.
   ```bash
   python3 -m venv .venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   You'll see `(.venv)` at the beginning of your command prompt when it's active.

4. **Install the necessary tools:**
   ```bash
   chmod +x scripts/install_tools.sh
   ./scripts/install_tools.sh
   ```
   This installs software that lets your computer communicate with the micro:bit.

## Deploying to Your Micro:bit

1. **Connect your micro:bit** to your computer using a USB cable.
   - Your computer should recognize it as a new device or drive.

2. **Ensure your virtual environment is activated:**
   Look for `(.venv)` at the start of your command prompt. If not visible, run:
   ```bash
   source .venv/bin/activate
   ```

3. **Deploy the code:**
   ```bash
   chmod +x scripts/deploy.sh
   ./scripts/deploy.sh
   ```
   This will transfer the program to your micro:bit. You'll see the LEDs flash during this process.

## Using Your Password Generator

Once the code is deployed, your micro:bit will display "Ready" and then show "A:Gen B:Send" to remind you of the button functions.

### Basic Usage:

1. **Generate a password:** Press button A
   - The micro:bit will display the first 5 characters of the generated password
   - Then show "OK" to confirm generation is complete

2. **Send the password via Bluetooth:** Press button B
   - If no password has been generated yet, it will show "No pwd"
   - Otherwise, it will attempt to send the password and show "Sent" on success
   - If there's an error, it will display "Err"

### Connecting to Bluetooth:

1. Enable Bluetooth on your receiving device (phone, tablet, etc.)
2. Pair with the micro:bit (it will appear in your device's Bluetooth settings)
3. Once paired, the password will be transmitted when you press button B

## Troubleshooting

### 504 Error Code
If you see "504" on your micro:bit display:
- This indicates a memory overflow error
- Our simplified code is specifically designed to avoid this error
- Make sure you're using the latest version from this repository
- Try pressing the micro:bit's reset button (on the back)

### No Response When Pressing Buttons
- Check that the deployment completed successfully
- Try unplugging and reconnecting your micro:bit
- Press the reset button on the back of the micro:bit

### Bluetooth Connection Issues
- Ensure Bluetooth is enabled on your receiving device
- Keep the micro:bit close to the receiving device
- Try resetting both the micro:bit and restarting Bluetooth on your device
- Some devices may require a specific app to receive UART data over Bluetooth

## Technical Details

The code is intentionally simplified to work within the micro:bit's limited memory constraints. Earlier versions included more complex password generation algorithms, but the current approach prioritizes reliability and effectiveness.

The password generator uses the micro:bit's hardware random number generator for better randomness, and the program is optimized to use minimal memory while still providing secure passwords.

## Limitations and Future Improvements

- Current implementation uses 8-character passwords to avoid memory issues
- Password complexity requirements are simplified
- Future versions could include:
  - Ability to store multiple passwords
  - Custom password length setting
  - Different password generation modes

## Development Notes

The code is written in MicroPython, a version of Python designed for microcontrollers. Due to the limited resources on the micro:bit, we've optimized for:

- Minimal memory usage
- Simple control flow
- Reliable operation over advanced features

The single-file approach was chosen for simplicity and reliability, as modular code caused memory issues on the hardware.