#jiahao - done def countdown()
import time
import sys
import threading


#===============================================================================================

# def check_pause():
#     """Thread to listen for pause/resume input."""
#     while True:
#         user_input = input("\nPress 'p' to pause or 'r' to resume: ").strip().lower()
#         if user_input == 'p':
#             paused.clear()  # Pause the countdown
#         elif user_input == 'r':
#             paused.set()  # Resume the countdown


# def lst():
# # Start a thread to listen for user input
#     threading.Thread(target=check_pause, daemon=True).start()


# def ps():
#     paused = threading.Event()  # Event to manage pause state
#     paused.set()  # Initially not paused
#     check_pause()
#     lst()



#===============================================================================================
# default countdown timer
# just put countdown(25) for 25 min countdown n so on
# def countdown(minutes): # in minutes
#     seconds = (minutes*60) #convert minutes to seconds
#     for remaining in range(seconds, 0, -1): #loop time backwards to 0
#         seconds = remaining % 60 
#         minutes = (remaining % 3600) //60 # convert seconds to minutes
#         time_string = f"{minutes:02}:{seconds:02}" # formate the time in ( min : sec )
#         # Use '\r' to overwrite the line
#         # sys.stdout.write: Prints the text without adding a newline (\n).
#         sys.stdout.write(f"\rRemaining time: {time_string}")
#         sys.stdout.flush()
#         time.sleep(1) # time.sleep: Waits for 1 second between each update.
#     sys.stdout.write("\rCountdown: Times up!          \n")

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
        
        sys.stdout.write(f"\rRemaining time: {time_string} | Press 'p' to pause: ")
        #sys.stdout.write("\033[K")
        # sys.stdout.write: Prints the text without adding a newline (\n).
        sys.stdout.flush()
        
        # time.sleep: Waits for 1 second between each update.
        time.sleep(1)
    sys.stdout.write("\rCountdown: Times up!          \n")
custom_countdown()
#=======================================================================================
import time
import sys
import threading

def timer(minutes):
    seconds = minutes * 60  # Convert minutes to seconds
    pause_flag = threading.Event()  # Event to manage pause and resume
    pause_flag.set()  # Initially, the countdown is not paused

    def input_listener():  # Thread to listen for user input
        nonlocal pause_flag
        while True:
            user_input = input().strip().lower()
            if user_input == 'p':
                pause_flag.clear()  # Pause the countdown
                print("\rPress 'r' to resume: ")
            elif user_input == 'r':
                pause_flag.set()  # Resume the countdown
                print("\rPress 'p' to pause: ")

    # Start the input listener thread
    listener_thread = threading.Thread(target=input_listener, daemon=True)
    listener_thread.start()
    # sys.stdout.write(f"'p' to pause or 'r' to resume:")
    # sys.stdout.write(f"\n")
    for remaining in range(seconds, 0, -1):  # Loop time backwards to 0
        pause_flag.wait()  # Wait here if paused
        mins = (remaining % 3600) // 60  # Convert seconds to minutes
        secs = remaining % 60
        time_string = f"{mins:02}:{secs:02}"  # Format time as MM:SS
        sys.stdout.write(f"\rRemaining time: {time_string}   ")  # Overwrite the line
        sys.stdout.flush()
        time.sleep(1)  # Wait for 1 second between each update

    sys.stdout.write("\rCountdown: Time's up!          \n")

# Example usage
#timer(25)