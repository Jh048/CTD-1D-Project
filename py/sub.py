#jiahao - done def countdown()
import time
import sys
import threading


#===============================================================================================

def check_pause():
    """Thread to listen for pause/resume input."""
    while True:
        user_input = input("\nPress 'p' to pause or 'r' to resume: ").strip().lower()
        if user_input == 'p':
            paused.clear()  # Pause the countdown
        elif user_input == 'r':
            paused.set()  # Resume the countdown


def lst():
# Start a thread to listen for user input
    threading.Thread(target=check_pause, daemon=True).start()


def ps():
    paused = threading.Event()  # Event to manage pause state
    paused.set()  # Initially not paused
    check_pause()
    lst()



#===============================================================================================
# default countdown timer
# just put countdown(25) for 25 min countdown n so on
def countdown(minutes): # in minutes
    seconds = (minutes*60) #convert minutes to seconds
    for remaining in range(seconds, 0, -1): #loop time backwards to 0
        seconds = remaining % 60 
        minutes = (remaining % 3600) //60 # convert seconds to minutes
        time_string = f"{minutes:02}:{seconds:02}" # formate the time in ( min : sec )
        # Use '\r' to overwrite the line
        # sys.stdout.write: Prints the text without adding a newline (\n).
        sys.stdout.write(f"\rRemaining time: {time_string}")
        sys.stdout.flush()
        time.sleep(1) # time.sleep: Waits for 1 second between each update.
    sys.stdout.write("\rCountdown: Times up!          \n")

#=======================================================================================

# custom countdown timer for user to imput thet time
def custom_countdown():
    user_input = input("Enter countdown time (HH,MM,SS): ")
    try:
        hours, minutes, seconds = map(int, user_input.split(","))
    except ValueError:
        print("Invalid format. Please enter time in HH:MM:SS format.")
        return
    
    total_time = (hours*3600)+(minutes*60)+seconds
    for remaining in range(total_time, 0, -1):
        seconds = remaining % 60
        minutes = (remaining % 3600) //60
        hours = (remaining // 3600)
        if hours > 0:
            time_string = f"{hours:02}:{minutes:02}:{seconds:02}"
        else:
            time_string = f"{minutes:02}:{seconds:02}"
        # Use '\r' to overwrite the line
        # sys.stdout.write: Prints the text without adding a newline (\n).
        
        sys.stdout.write(f"\rRemaining time: {time_string}")
        sys.stdout.write("\033[K")
        # sys.stdout.write: Prints the text without adding a newline (\n).
        sys.stdout.flush()
        # time.sleep: Waits for 1 second between each update.
        time.sleep(1)
    sys.stdout.write("\rCountdown: Times up!          \n")

#=======================================================================================
