import sys
import os

# Add the parent folder (CTD 1D CODE) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Import the timer function from Timer.py
from timer import timer, timer_data  # Match the exact name of Timer.py (case-sensitive)

# Use the timer function
#print("Calling timer() from Timer.py")
timer()  # Example: Starts a 5-second timer
print("Timer data summary:")
for entry in timer_data:
    print(f"Elapsed Time: {entry['elapsed_time']}, Paused Time: {entry['paused_time']}")