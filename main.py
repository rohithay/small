#!/usr/bin/env python3
"""
AI Search Hub - Quick access to top AI tools
Main entry point for the GUI application
"""

import sys
import webbrowser
from pathlib import Path

# Try to import tkinter, with fallback message
try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    print("Error: tkinter is required. Install with: sudo apt install python3-tk (Linux) or use Python from python.org")
    sys.exit(1)

# Import the GUI class (adjust path if needed)
try:
    from app import CronTabGUI  # Assuming you saved the previous code as app.py
except ImportError:
    print("Error: Could not find app.py in the same directory.")
    print("Please save the GUI code as 'app.py' first.")
    sys.exit(1)

def main():
    """Main function to launch the AI Search GUI"""
    print("🚀 Starting AI Search Hub...")
    
    # Create and run the GUI
    try:
        app = CronTabGUI("AI Search Hub", "550x450")
        app.run()
    except Exception as e:
        messagebox.showerror("Launch Error", f"Failed to start GUI:\n{str(e)}")
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
