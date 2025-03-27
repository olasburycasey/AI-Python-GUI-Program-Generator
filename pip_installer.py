import subprocess
import sys

def install_package(package_name):
    print(f"Checking for {package_name} installation...")
    try:
        __import__(package_name)
        print(f"{package_name} is already installed.")
    except ImportError:
        print(f"{package_name} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"{package_name} installed successfully.")
        try:
            __import__(package_name)
            print(f"{package_name} imported successfully.")
        except ImportError:
            print(f"Failed to import {package_name} after installation.")

# Example: Install pygame
install_package("pygame")
