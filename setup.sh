#!/bin/bash
set -e  # Exit on error

# Install system dependencies
echo "Installing system dependencies..."
sudo apt-get update
sudo apt-get install -y ffmpeg python3-pip python3-venv

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate || {
    echo "Failed to activate virtual environment"
    exit 1
}

# Install dependencies
echo "Installing Python packages..."
pip install --upgrade pip wheel setuptools
pip install numpy>=1.20.0

# Install PyTorch CPU version first
pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu
pip install --no-cache-dir torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install remaining requirements
pip install -r requirements.txt

# Verify critical imports
python3 -c "
import numpy
import torch
import librosa
import moviepy
import whisper
print('All dependencies installed successfully!')
"
