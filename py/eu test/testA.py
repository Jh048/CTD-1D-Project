import sys
import os

# Add the parent folder (CTD 1D CODE) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Import the timer function from Timer.py
from timer import timer, timer_data  # Match the exact name of Timer.py (case-sensitive)

timer(10)
print(timer_data)