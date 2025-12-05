#!/bin/bash

# This script automatically activates the environment and runs your app
# So you don't have to remember the activation command every time.

# 1. Check if the environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found! Please run ./setup.sh first."
    exit 1
fi

# 2. Activate environment
source venv/bin/activate

# 3. Run the camera app
python camera_scan.py