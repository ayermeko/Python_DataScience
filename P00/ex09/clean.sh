#!/bin/bash

# Clean build files
rm -rf dist/
rm -rf *.egg-info/
rm -rf venv/
rm -rf ft_package/__pycache__
pip uninstall -y ft_package
echo "Cleaned up build artifacts."
