import sys
import os

# Add the parent folder (CTD 1D CODE) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Import the timer function from Timer.py
from timer import timer  # Match the exact name of Timer.py (case-sensitive)

# Use the timer function
print("Calling timer() from Timer.py")
timer(5)  # Example: Starts a 5-second timer

"""
create session: open code, make new list within dictionary
this is to happen every time the start button is pressed
naming to be the current length of dictionary + 1
"""
# making new list within dictionary 
"""Example dictionary"""
#my_dict = {"key1": [1, 2, 3], "key2": [4, 5, 6]}
"""Adding a new key with an empty list"""
#my_dict["key3"] = []
"""Printing the updated dictionary"""
#print(my_dict)


'''
storing: adding to the new empty list happens every time the 
1) loop ends
2) they quit after pausing
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
