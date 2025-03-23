#!/bin/bash

echo "Installing micro:bit development tools..."

# Ensure pip is up to date
pip install --upgrade pip

# Install microfs, uflash and their dependencies
pip install microfs==1.4.5 uflash==2.0.0 pyserial==3.5

# Make sure the commands are available in PATH
echo "Adding ~/.local/bin to PATH if needed..."
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
    echo "PATH updated. Please restart your terminal or run: source ~/.bashrc"
fi

echo "Installation complete! Try running: uflash --help and microfs --help"
