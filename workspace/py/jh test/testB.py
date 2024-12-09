import sys
import os

# Add the parent folder (CTD 1D CODE) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from timer15work import timer, timer_data  # Match the exact name of Timer.py (case-sensitive)
archive_dict = {}
title = None
# timer(10)
# print(timer_data)
# Import the timer function from Timer.py

def start_or_archive():
    global title
    Start_or_archieve = input('Do you want to start a timer?(y/n)').lower()
    if Start_or_archieve == 'y':
        title = input ("YES was entered. What are we doing today?")
        # print(f"working session: {title}")
        timer()
    else:
        Archieve= input ('Do you want to look at your history?(y/n)').lower()
        if Archieve == 'y':
            print ('Loading History..........')
            #Histroy function
        elif Archieve == 'n':
            print ('Bye! Have a great day!')
        else:
            print("incorrct input, please try again")


# def store():
#     import elapsed_time  
# archive_dict[title].append('')

def secs_to_clock(sec):
    mins, secs = divmod(sec, 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02}:{mins:02}:{secs:02}" if hours > 0 else f"{mins:02}:{secs:02}"

# Main entry point
if __name__ == "__main__":
    start_or_archive()
