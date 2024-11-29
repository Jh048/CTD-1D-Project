import sys
import os

# Add the parent folder (CTD 1D CODE) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Import the timer function from Timer.py
from timer import timer  # Match the exact name of Timer.py (case-sensitive)





Start_or_archieve = input('Do you want to start a timer?(Y/N)'). upper ()
if Start_or_archieve == 'Y':
    Title = input ("YES was entered. What are we doing today?")
    #timer function
    timer()
else:
    Archieve= input ('Do you want to look at your history?(Y/N)') .upper()
    if Archieve == 'Y':
        print ('Loading History..........')
        #Histroy function
    else:
        print ('Bye! Have a great day!')
        #go back main (main function)