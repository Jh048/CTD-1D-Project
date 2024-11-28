import sys
import os

# Add the parent folder (CTD 1D CODE) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Import the timer function from Timer.py
from timer import timer  # Match the exact name of Timer.py (case-sensitive)

# Use the timer function
#print("Calling timer() from Timer.py")
#timer(5)  # Example: Starts a 5-second timer

"""
create session: open code, make new list within dictionary
this is to happen every time the start button is pressed
naming to be the current length of dictionary + 1
"""
archive_dict = {}
# making new list within dictionary, this input will be taken from jennifer
archive_dict[Title] = []


## storing: adding to the new empty list happens every time the 
# 1) loop ends
def store():
    import nonlocal remaining_time
    archive_dict[Title].append('')
    return 
#Get value from timer code for loop ending
# 2) they quit after pausing
def store_pause ():
    archive_dict[Title].append('pause_time_str')
    return 

'''
# use append method for this part

'''
naming: the saved list/value under a specified key
ask for input name/label for study session
ask for confirmation, 
if "no", go back to asking for input
if "yes", save key name for that list
'''


'''
session_time: function to sum the total of a specified session
'''

print(paused_time_str)
