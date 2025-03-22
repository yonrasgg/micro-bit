# Micro:bit Password Generator and Manager

A secure password generation and management system for BBC micro:bit devices. This project allows you to generate strong passwords and send them via Bluetooth to paired devices.

## Project Structure

```
/micro-bit/
├── main.py                # Main program with simplified, working functionality
├── scripts/               # Helper scripts for development and deployment
│   ├── install_tools.sh   # Script to install required development tools
│   └── deploy.sh          # Script to deploy code to micro:bit (renamed from simplified_deploy.sh)
├── README.md              # This documentation file
└── requirements.txt       # Project dependencies
```

## Functionality

- **Button A**: Generate a new password and display its first 5 characters
- **Button B**: Send the last generated password via Bluetooth

## Current Implementation

The current implementation uses a simplified approach to work reliably on the micro:bit hardware:

- Generates 8-character passwords for improved performance
- Uses direct microbit module imports for better compatibility
- Minimizes memory usage to avoid 504 errors
- Offers full password generation and Bluetooth sending capabilities

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

## Deployment to micro:bit

To deploy the code to your micro:bit device:

1. Make sure your virtual environment is activated:
   ```bash
   source .venv/bin/activate
   ```

2. Connect your micro:bit via USB

3. Use the deployment script:
   ```bash
   chmod +x scripts/deploy.sh
   ./scripts/deploy.sh
   ```

This will deploy the ultra-simplified version that has been confirmed to work properly.

## Testing the Application

1. After deployment, you should see "Ready" scroll across the micro:bit's LED display
2. Press button A to generate a password - you'll see the first 5 characters followed by "OK"
3. Press button B to send the password via Bluetooth - you'll see "Sent" on success

## Troubleshooting

### If you see error code 504:
- Use the deploy.sh script which deploys code optimized to avoid this error
- Try pressing the reset button on the micro:bit
- Make sure you're using the latest version of the code from this repository

### Common Issues

1. **USB Connection Issues**:
   - Try unplugging and reconnecting the micro:bit
   - Try a different USB cable
   - Ensure you have the correct permissions to access the USB device

2. **Bluetooth Pairing**:
   - Make sure your receiving device is paired with the micro:bit
   - Keep devices close together during transmission
   - Check the receiving device has Bluetooth enabled

## Development Notes

The code has been simplified to ensure reliable operation on the micro:bit hardware. While more complex password generation algorithms were implemented in earlier versions, the current version prioritizes stability and core functionality.