#!/bin/bash

echo "Deploying micro:bit code..."

# Get the project root directory (parent of scripts directory)
PROJECT_ROOT="$(dirname "$(dirname "$(readlink -f "$0")")")"
MAIN_PY="${PROJECT_ROOT}/main.py"

# Flash the main.py file to the micro:bit
if uflash "${MAIN_PY}"; then
    echo "Main code successfully flashed to micro:bit!"
    echo "Using main.py from: ${MAIN_PY}"
else
    echo "Error flashing code. Please check if micro:bit is connected properly."
    exit 1
fi

echo "Deployment complete!"
echo "Reminder: All code is now in the main.py file - no need to transfer other modules."
