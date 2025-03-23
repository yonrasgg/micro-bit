#!/bin/bash

echo "Deploying secure password generator..."

# Get project root
PROJECT_ROOT="$(dirname "$(dirname "$(readlink -f "$0")")")"

# Check if we're using BLE-enabled approach
if [ -f "${PROJECT_ROOT}/firmware/ble-radio-bridge.hex" ]; then
    echo "Deploying with BLE-enabled approach..."
    echo "Using custom BLE-enabled firmware..."
    
    # Instead of using the deprecated 'runtime' flag, we can use the merged hex approach
    # First, convert Python code to hex
    python -m uflash --format hex "${PROJECT_ROOT}/main.py" -o "${PROJECT_ROOT}/firmware/python_code.hex"
    
    # Then merge our code with the BLE firmware
    # Note: This requires the microfs (ufs) package to be installed
    python -c "
import microfs
microfs.save_hex('${PROJECT_ROOT}/firmware/python_code.hex', '${PROJECT_ROOT}/firmware/ble-radio-bridge.hex', '${PROJECT_ROOT}/firmware/merged.hex')
"
    
    # Finally flash the merged hex
    python -m uflash "${PROJECT_ROOT}/firmware/merged.hex"
else
    echo "Deploying standard version..."
    # Standard deployment without custom firmware
    python -m uflash "${PROJECT_ROOT}/main.py"
fi

if [ $? -eq 0 ]; then
    echo "Deployment successful!"
else
    echo "Deployment failed."
    exit 1
fi
