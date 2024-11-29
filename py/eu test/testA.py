import sys
import os

# Add the parent folder (CTD 1D CODE) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Import the timer function from Timer.py
from timer import timer, timer_data  # Match the exact name of Timer.py (case-sensitive)
archive_dict = {}
# timer(10)
# print(timer_data)

# def store():
#     import elapsed_time  
#     archive_dict[Title].append('')

def secs_to_clock(s):
    mins, secs = divmod(s, 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02}:{mins:02}:{secs:02}" if hours > 0 else f"{mins:02}:{secs:02}"


print(secs_to_clock(108576))
