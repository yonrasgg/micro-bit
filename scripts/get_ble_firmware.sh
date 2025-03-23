#!/bin/bash

echo "Downloading BLE-enabled firmware for micro:bit password generator..."

# Get project root
PROJECT_ROOT="$(dirname "$(dirname "$(readlink -f "$0")")")"

# Create firmware directory if it doesn't exist
mkdir -p "${PROJECT_ROOT}/firmware"

# Define firmware URL - this is a specially built firmware hex that bridges radio to BLE
# For demonstration purposes, we're using a placeholder URL - replace with actual URL
FIRMWARE_URL="https://github.com/lancaster-university/microbit-v2-samples/releases/download/v2.0.0/ble-uart-bridge.hex"

# Download firmware
echo "Downloading firmware from ${FIRMWARE_URL}..."
curl -L -o "${PROJECT_ROOT}/firmware/ble-radio-bridge.hex" "${FIRMWARE_URL}" || {
    echo "Error: Failed to download firmware."
    echo ""
    echo "Alternative approach:"
    echo "1. Visit https://makecode.microbit.org/"
    echo "2. Start a new project"
    echo "3. Add the 'Bluetooth' extension"
    echo "4. Use the following blocks:"
    echo "   - On start: enable Bluetooth UART service"
    echo "   - Forever: if radio received then bluetooth UART send value"
    echo "5. Download the hex file and save it to: ${PROJECT_ROOT}/firmware/ble-radio-bridge.hex"
    exit 1
}

echo "Firmware downloaded successfully to: ${PROJECT_ROOT}/firmware/ble-radio-bridge.hex"
echo ""
echo "Now run './scripts/deploy.sh' to deploy your password generator with BLE support."
