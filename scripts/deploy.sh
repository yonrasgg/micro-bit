#!/bin/bash

echo "Deploying micro:bit code..."

# Get the project root directory (parent of scripts directory)
PROJECT_ROOT="$(dirname "$(dirname "$(readlink -f "$0")")")"
MAIN_PY="${PROJECT_ROOT}/main.py"
TEMP_PY="${PROJECT_ROOT}/main_deploy.py"

# Check python environment path
echo "Python executable: $(which python3)"
echo "PATH: $PATH"

# Create a temporary copy and replace f-strings and other incompatible features
echo "Converting code to MicroPython compatible format..."
cat "${MAIN_PY}" | 
  sed 's/f"\([^"]*\){/"\1" + str(/g; s/}"/)/g' |
  sed 's/import random, string/import random/' > "${TEMP_PY}"

# Skip microfs check and go straight to flashing
echo "Skipping connection check and proceeding to flash the device..."

# Try to find uflash - first check if it's in PATH
UFLASH_CMD=$(which uflash 2>/dev/null)

# If not in PATH, try using the full path in the virtual environment
if [ -z "$UFLASH_CMD" ]; then
    echo "uflash not found in PATH, trying to find it in virtual environment..."
    VENV_BIN="${PROJECT_ROOT}/.venv/bin"
    
    if [ -x "${VENV_BIN}/uflash" ]; then
        UFLASH_CMD="${VENV_BIN}/uflash"
        echo "Found uflash at ${UFLASH_CMD}"
    else
        echo "uflash not found in virtual environment either."
        echo "Make sure you have activated your virtual environment with:"
        echo "source .venv/bin/activate"
        echo "and installed the required tools with:"
        echo "./scripts/install_tools.sh"
        rm "${TEMP_PY}"
        exit 1
    fi
fi

# Flash the temporary file to the micro:bit
echo "Flashing with command: ${UFLASH_CMD} ${TEMP_PY}"
if "${UFLASH_CMD}" "${TEMP_PY}"; then
    echo "Main code successfully flashed to micro:bit!"
    echo "Using main.py from: ${MAIN_PY}"
    # Cleanup
    rm "${TEMP_PY}"
else
    echo "Error flashing code. Please check if micro:bit is connected properly."
    rm "${TEMP_PY}"
    exit 1
fi

echo "Deployment complete!"
echo "Reminder: All code is now in the main.py file - no need to transfer other modules."
echo "If you see error codes on the micro:bit, try pressing the reset button."
echo ""
echo "IMPORTANT: If you're using a virtual environment, ensure it's activated with:"
echo "source .venv/bin/activate"
echo ""
echo "If uflash still isn't found, you may need to install it directly:"
echo "pip install --user uflash==2.0.0"
echo "And then try again after restarting your terminal or running: source ~/.bashrc"
