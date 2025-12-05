#!/bin/bash

# 1. Create a virtual environment named 'venv' if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment 'venv' already exists."
fi

# 2. Activate the virtual environment
# Note: This activation only lasts for the duration of this script.
# You must activate it manually in your terminal afterward.
source venv/bin/activate

# 3. Upgrade pip to ensure smooth installation
echo "Upgrading pip..."
pip install --upgrade pip

# 4. Install requirements
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
    echo "Success! Dependencies installed."
else
    echo "Error: requirements.txt not found!"
fi

echo ""
echo "================================================"
echo "Setup complete!"
echo "To start working, run this command in your terminal:"
echo "source venv/bin/activate"
echo ""
echo "Then run your app with:"
echo "python camera_scan.py"
echo "================================================"