# Micro:bit Password Generator and Manager

A secure password generation and management system for BBC micro:bit devices. This project allows you to generate strong passwords and send them via Bluetooth to paired devices.

## Project Structure

```
/micro-bit/
├── main.py                # Main program entry point and application logic
├── password_generator.py  # Functions for generating secure passwords
├── bluetooth_manager.py   # Handles Bluetooth communication 
├── display_manager.py     # Controls the micro:bit LED display
├── button_manager.py      # Manages button input detection
├── hardware.py            # Hardware abstraction layer for micro:bit features
├── env.py                 # Environment detection (micro:bit vs simulation)
├── utils.py               # Common utility functions
├── config.py              # Application configuration parameters
├── microbit_mock.py       # Simulation of micro:bit for development
└── requirements.txt       # Project dependencies
```

## Code Overview

- **main.py**: Entry point that coordinates all modules. Handles the main program flow, initializing the password generator and managing user input.
  
- **password_generator.py**: Generates secure random passwords with configurable parameters like length, number of digits, and special characters.

- **bluetooth_manager.py**: Manages Bluetooth communication to send passwords to paired devices.

- **display_manager.py**: Controls the micro:bit's LED display to show messages and password feedback.

- **button_manager.py**: Handles button press detection and input processing.

- **hardware.py**: Provides a hardware abstraction layer that works on both the actual micro:bit and in simulation mode.

- **env.py**: Detects whether the code is running on a physical micro:bit or in development mode.

- **config.py**: Contains configuration settings like password length and complexity requirements.

## Development Setup

### Setting Up Virtual Environment

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Working with micro:bit Connected to PC

1. Connect your micro:bit via USB cable to your computer

2. Verify connection:
   - On Windows: Check Device Manager for a new COM port
   - On macOS: Run `ls /dev/tty.*` to see the device (usually appears as `/dev/tty.usbmodem*`)
   - On Linux: Run `ls /dev/ttyACM*` to see the device

3. Development workflow:
   - Make changes to the code
   - Test in simulation mode: `python main.py`
   - When ready to test on hardware, follow the deployment instructions below

## Functionality

- **Button A**: Generate a new secure password
- **Button B**: Send the last generated password via Bluetooth

## Error Handling

- Prevents sending when no password has been generated
- Provides feedback on success/failure of operations

## Development & Deployment

### Development Mode (Simulation)

This code can be run on your computer for testing using the mock microbit module:
```bash
# Make sure your virtual environment is activated
python main.py
```

### Deployment to micro:bit

To deploy the code to your micro:bit device:

1. Make sure your virtual environment is activated and dependencies installed:
   ```bash
   pip install -r requirements.txt
   ```

2. Connect your micro:bit via USB

3. Flash the main code:
   ```bash
   uflash main.py
   ```

4. Transfer additional module files:
   ```bash
   microfs put password_generator.py
   microfs put bluetooth_manager.py
   microfs put display_manager.py
   microfs put button_manager.py
   microfs put hardware.py
   microfs put env.py
   microfs put utils.py
   microfs put config.py
   ```

## Troubleshooting

### Common Issues

1. **"No module named 'microbit'"**: 
   - This is expected when running in simulation mode
   - The code will automatically use the mock implementation

2. **USB Connection Issues**:
   - Try unplugging and reconnecting the micro:bit
   - Try a different USB cable
   - Ensure you have the correct permissions to access the USB device

3. **File Transfer Errors**:
   - Make sure the micro:bit is properly connected
   - Ensure the micro:bit is not in a busy state
   - Try rebooting the micro:bit by disconnecting and reconnecting

### Checking micro:bit Status

To check if your micro:bit is properly connected and accessible:

```bash
microfs ls
```

This should list the files currently on your micro:bit.