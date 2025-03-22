# Micro:bit Password Generator and Manager

A secure password generation and management system for BBC micro:bit devices. This project allows you to generate strong passwords and send them via Bluetooth to paired devices.

## Project Structure

```
/micro-bit/
├── main.py                # Main program with all necessary functionality
├── scripts/               # Helper scripts for development and deployment
│   ├── install_tools.sh   # Script to install required development tools
│   └── deploy.sh          # Script to deploy code to micro:bit
├── README.md              # This documentation file
└── requirements.txt       # Project dependencies
```

## Code Overview

The main.py file includes all necessary functionality:

- **Password Generation**: Creates secure random passwords with configurable parameters like length, number of digits, and special characters.

- **Bluetooth Communication**: Manages Bluetooth communication to send passwords to paired devices.

- **Display Management**: Controls the micro:bit's LED display to show messages and password feedback.

- **Button Input**: Handles button press detection and input processing.

- **Environment Detection**: Detects whether the code is running on a physical micro:bit or in development mode.

## Development Setup

### Setting Up Virtual Environment

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
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

3. Install Required Tools:
   ```bash
   chmod +x scripts/install_tools.sh
   ./scripts/install_tools.sh
   ```

4. Open a new terminal or reload your environment:
   ```bash
   source ~/.bashrc
   ```

### Working with micro:bit Connected to PC

1. Connect your micro:bit via USB cable to your computer

2. Verify connection:
   - On Windows: Check Device Manager for a new COM port
   - On macOS: Run `ls /dev/tty.*` to see the device (usually appears as `/dev/tty.usbmodem*`)
   - On Linux: Run `ls /dev/ttyACM*` to see the device

## Functionality

- **Button A**: Generate a new secure password
- **Button B**: Send the last generated password via Bluetooth

## Error Handling

- Prevents sending when no password has been generated
- Provides feedback on success/failure of operations

## Development & Deployment

### Development Mode (Simulation)

This code can be run on your computer for testing without an actual micro:bit:
```bash
# Make sure your virtual environment is activated
python3 main.py
```

### Deployment to micro:bit

To deploy the code to your micro:bit device:

1. Make sure your virtual environment is activated and tools installed (see Setup above)

2. Connect your micro:bit via USB

3. Run the deployment script:
   ```bash
   chmod +x scripts/deploy.sh
   ./scripts/deploy.sh
   ```

The script will flash the main.py file to your micro:bit and handle all the necessary setup.

## Troubleshooting

### Common Issues

1. **"No module named 'microbit'"**: 
   - This is expected when running in simulation mode
   - The code will automatically use the mock implementation

2. **USB Connection Issues**:
   - Try unplugging and reconnecting the micro:bit
   - Try a different USB cable
   - Ensure you have the correct permissions to access the USB device

3. **Missing Commands After Installation**:
   - If the `uflash` or `microfs` commands are not found after running install_tools.sh:
   - Try opening a new terminal window
   - Run `source ~/.bashrc` to reload your environment
   - Check if ~/.local/bin is in your PATH with `echo $PATH`

### Checking micro:bit Status

If you need to manually check if your micro:bit is properly connected:

```bash
uflash --help
```

This should display the help information for the uflash tool if it's properly installed.