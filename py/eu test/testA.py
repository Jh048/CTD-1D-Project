import sys
import os

# Add the parent folder (CTD 1D CODE) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from timer import timer, timer_data  # Match the exact name of Timer.py (case-sensitive)
archive_dict = {}
# timer(10)
# print(timer_data)
# Import the timer function from Timer.py
def start_or_archive():
    Start_or_archieve = input('Do you want to start a timer?(Y/N)').upper()
    if Start_or_archieve == 'Y':
        Title = input ("YES was entered. What are we doing today?")
        
    else:
        Archieve= input ('Do you want to look at your history?(Y/N)').upper()
        if Archieve == 'Y':
            print ('Loading History..........')
            #Histroy function
        else:
            print ('Bye! Have a great day!')


def store():
    import elapsed_time  
archive_dict[Title].append('')

def secs_to_clock(sec):
    mins, secs = divmod(sec, 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02}:{mins:02}:{secs:02}" if hours > 0 else f"{mins:02}:{secs:02}"

# Main entry point
if __name__ == "__main__":
    start_or_archive()
