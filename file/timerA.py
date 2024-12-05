import time # Used to manage delays and countdown timing in seconds.
import threading # Enables concurrent execution of code (to run the timer and handle user inputs simultaneously).
import sys # Used to manipulate the output in the terminal for updating countdown visuals.
import copy
import menu as m
import signal

from datetime import timedelta



timer_data = []
user_input = None
quit_flag = threading.Event()  # Global quit flag to control exit
elapsed_time = 0
archive_dict = {}
title = None
user_input = ""
time_up = False






def secs_to_clock(sec):
    mins, secs = divmod(sec, 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02}:{mins:02}:{secs:02}"


#=========================================================================================================


def timer(*args,title =None):

# The timer function accepts an optional set of arguments representing the time in hours, minutes, and seconds.
    global timer_data, user_input, quit_flag, elapsed_time, user_input, time_up
    time_up = False
    quit_flag.clear()
    if not args:
    # If no arguments are passed, the function prompts the user to enter a countdown time in the format HH,MM,SS

        while True:
            try:
                print()
                print(f"Working session: {title}")
                print("e.g. 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec")
                time_input = input("Enter countdown time (HH,MM,SS): ").strip()
                print()
                print(f"Working session: {title}")
                # time_input.strip() removes leading/trailing spaces.

                time_parts = list(map(int, time_input.split(',')))
                # time_input.split(',') splits the input string into components (e.g., “1,0,30” → [1, 0, 30]).
                # list(map(int, ...)) converts each part into an integer.

                if len(time_parts) == 1:
                    hours, minutes, seconds = 0, 0, time_parts[0] # Interpreted as seconds.
                elif len(time_parts) == 2:
                    hours, minutes, seconds = 0, time_parts[0], time_parts[1] # Interpreted as minutes and seconds.
                elif len(time_parts) == 3:
                    hours, minutes, seconds = time_parts # Interpreted as hours, minutes, and seconds.
                else:

                    print("e.g. 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec")
                    print("Invalid input. Please enter time in the format HH,MM,SS.")
                    # If the input is invalid, it prompts the user again.
                    continue

                if hours < 0 or minutes < 0 or seconds < 0 or minutes >= 60 or seconds >= 60:
                    # Minutes and seconds must be between 0 and 59.
                    # No component can be negative.

                    print("e.g. 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec")
                    print("Invalid time format. Ensure hours, minutes, and seconds are within limit.")
                    continue

                break
            except ValueError:
                print("Invalid input. Please enter time in the format HH,MM,SS.")
    else:
        # If arguments are passed directly (args), the function parses them similarly to user input.

        if len(args) == 1:
            hours, minutes, seconds = 0, 0, args[0]
        elif len(args) == 2:
            hours, minutes, seconds = 0, args[0], args[1]
        elif len(args) == 3:
            hours, minutes, seconds = args
        else:
            print("e.g. 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec")
            print("Invalid time format. Ensure time is in the).")
            return 
    total_seconds = hours * 3600 + minutes * 60 + seconds
    # Converts the time into total seconds for easier countdown calculation.
    original_total_time = copy.deepcopy(total_seconds)

    pause_flag = threading.Event() # threading.Event is used for pause and resume the timer.
    pause_flag.set() # Initializes the flag as active (running state).
    remaining_time = total_seconds #Tracks the countdown’s remaining seconds.
    paused_time = 0 # Tracks how long the timer has been paused in the current pause session.
    total_pause_time_list = []
    total_pause_time = sum(total_pause_time_list) - len(total_pause_time_list)
    pause_count = 0
    resume_count = 0
 
    

    def display_timer():
        
        global time_up
        nonlocal remaining_time, paused_time, pause_count, resume_count, original_total_time
        while remaining_time > 0:
            if quit_flag.is_set():  # If quit flag is set, break out of the loop
                break
            if pause_flag.is_set(): 
                print(f"\rRemaining time: {secs_to_clock(remaining_time)} | Press 'p' to pause, Press 'q' to quit: ", end="")
                time.sleep(1)
                remaining_time -= 1
            else:
                print(f"\rPause time: {secs_to_clock(paused_time)} | Press 'r' to resume, Press 'q' to quit:", end="")
                paused_time += 1
                time.sleep(1)

        if remaining_time == 0:  # When timer completes
            time_up = True
            sys.stdout.write("\033[K")
            sys.stdout.write("\rRemaining time: 00:00:00 | Timer completed!                           ")
            sys.stdout.write("\n")
            paused_time_str = f"{secs_to_clock(total_pause_time)}"
            
            elapsed_time = original_total_time - remaining_time
            elapsed_time_str = f"{secs_to_clock(elapsed_time)}"


            # Store details in the global list
            key_name = str(title or "No Title")
            if key_name not in archive_dict:
                archive_dict[key_name] = []
            archive_dict[key_name].append({
                "Elapsed_time": elapsed_time_str,
                "Total_paused_time": paused_time_str})
            # Display summary
            print("\nTimer Summary:")
            print(f"Elapsed Time: {elapsed_time_str}")
            print(f"Total Pause Time: {paused_time_str}")
            # Trigger quit flag to terminate `input_listener`
            print("Press enter to continue.")
            
            quit_flag.set()


    def input_listener():
        global time_up
        nonlocal remaining_time, paused_time, pause_count, resume_count, total_pause_time_list, total_pause_time

        while not quit_flag.is_set():  # Continues running unless quit_flag is set
            try:
                user_input = input().strip().lower()

                if user_input == "p" and pause_flag.is_set():  # Pause the timer
                    pause_flag.clear()
                    paused_time = 0  # Reset pause time tracker for the new pause session
                    pause_count += 1

                elif user_input == "r" and not pause_flag.is_set():  # Resume the timer
                    pause_flag.set()
                    if paused_time > 0:
                        total_pause_time_list.append(paused_time)  # Add the paused time to the list
                    resume_count += 1
                elif user_input == "q":  # Quit the timer
                    

                    # Add the current paused time to the total pause list
                    if not pause_flag.is_set() and paused_time > 0:
                        total_pause_time_list.append(paused_time)

                    # Calculate total pause time
                    total_pause_time = sum(total_pause_time_list) - len(total_pause_time_list)

                    # Calculate elapsed time
                    elapsed_time = original_total_time - remaining_time

                    # Format total paused time string
                    paused_time_str = f"{secs_to_clock(total_pause_time)}"
                    elapsed_time_str = f"{secs_to_clock(elapsed_time)}"

                    key_name = str(title or "No Title")
                    if key_name not in archive_dict:
                        archive_dict[key_name] = []
                    archive_dict[key_name].append({
                        "Elapsed_time": elapsed_time_str,
                        "Total_paused_time": paused_time_str})


                    # Display summary
                    print("\nTimer Summary:")
                    print(f"Elapsed Time: {elapsed_time_str}")
                    print(f"Total Pause Time: {paused_time_str}")
                    quit_flag.set()  # Set the quit flag to stop both threads
                    time_up = False
                
                    break

            except EOFError:
                # Handle input interruptions
                quit_flag.set()
                break 


              
    timer_thread = threading.Thread(target=display_timer, daemon=True)
    # Displays the countdown.
    input_thread = threading.Thread(target=input_listener, daemon=True)
    # Listens for user input.

    # Threads are started using .start() and synchronized with .join().
    timer_thread.start()
    input_thread.start()

    timer_thread.join()
    input_thread.join()
    print(archive_dict)
    return time_up



    
# Start the timer
# Example 1: timer(5) will start a 5-second countdown
# Example 2: timer(2, 5) will start a 2-minute 5-second countdown
# Example 3: timer(1, 0, 5) will start a 1-hour 0-minute 5-second countdown
# Example 4: timer() will ask the user for input
''' Example 5:
if using timer() in another file under the same folder
can import timer as t
t.timer() to use i another file'''

  # Example of calling the function with hours, minutes, and seconds
# Main entry point


#=========================================================================================================
def a():
    print(m.menu1)

def start_or_archive():
    global title
    Start_or_archieve = input('Do you want to start a timer?(y/n): ').lower()
    if Start_or_archieve == 'y':
        title = input ("Do you want to study,work or others?") .lower()
        if title== "study":
            #default timer for study
            print (f'You have chosen {title}')
        elif title == "work":
            #default for study
            print (f'You have chosen {title}')
        elif title == "others":
            other_activity= input ("What do you want to do today?") .lower()
            #ask for duration function
            print (f'You have chosen {other_activity}')
        else:
            print (invalid)
        
        # print(f"working session: {title}")
        
    elif title=='n':
        Archieve= input ('Do you want to look at your history?(y/n): ').lower()
        if Archieve == 'y':
            print ('Loading History..........')
            #Histroy function
        elif Archieve == 'n':
            print ('Bye! Have a great day!')
        else:
            print("incorrct input, please try again")
    else:
        print ('invalid')





def data():
    global timer_data
    # Ensure timer_data has entries before processing
    if not timer_data:
        print("No data available.")
        return None

    # Extract elapsed and paused times from timer_data
    study_times = []  # For elapsed work session times
    break_times = []  # For total paused times

    for entry in timer_data:
        # Convert the "elapsed_time" and "paused_time" strings to total minutes
        elapsed_time = entry.get("elapsed_time", "00:00:00")
        paused_time = entry.get("paused_time", "00:00:00")

        study_times.append(secs_to_clock(elapsed_time))
        break_times.append(secs_to_clock(paused_time))

    # Build the dictionary with the summed data
    pomodoro_data = {
        'study': sum(study_times),  # Total study time in minutes
        'break': sum(break_times)  # Total break time in minutes
    }

    return pomodoro_data

# time_calculator.py


def calculate_total_times(archive_dict):
    def time_string_to_seconds(time_str):
        hours, minutes, seconds = map(int, time_str.split(':'))
        return timedelta(hours=hours, minutes=minutes, seconds=seconds).total_seconds()

    def seconds_to_time_string(seconds):
        return str(timedelta(seconds=seconds))

    total_times = {}

    for key_name, activities in archive_dict.items():
        total_elapsed = 0
        total_paused = 0
        
        for activity in activities:
            total_elapsed += time_string_to_seconds(activity['Elapsed_time'])
            total_paused += time_string_to_seconds(activity['Total_paused_time'])
        
        total_elapsed_time_str = seconds_to_time_string(total_elapsed)
        total_paused_time_str = seconds_to_time_string(total_paused)
        
        total_times[key_name] = {
            'Total Elapsed Time': total_elapsed_time_str,
            'Total Paused Time': total_paused_time_str
        }


    return total_times

total = calculate_total_times(archive_dict)
def display_time_summary(total):
    
    """
    Displays the activity-wise breakdown and total elapsed and paused times across all activities.

    Args:
        total (dict): A dictionary containing aggregated times for each activity.

    Returns:
        dict: Total elapsed and paused times across all activities in HH:MM:SS format.
    """
    def time_string_to_seconds(time_str):
        """Convert HH:MM:SS formatted time string to seconds."""
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours * 3600 + minutes * 60 + seconds

    def secs_to_clock(sec):
        """Convert seconds into HH:MM:SS format."""
        mins, secs = divmod(sec, 60)
        hours, mins = divmod(mins, 60)
        return f"{hours:02}:{mins:02}:{secs:02}"

    total_elapsed_time = 0
    total_paused_time = 0

    # Activity-wise breakdown
    print("Activity-wise Breakdown:")
    for activity, times in total.items():
        # If 'times' is a list of dictionaries, you need to sum up the times
        if isinstance(times, list):
            activity_elapsed_time = 0
            activity_paused_time = 0
            for time_entry in times:
                activity_elapsed_time += time_string_to_seconds(time_entry['Elapsed_time'])
                activity_paused_time += time_string_to_seconds(time_entry['Total_paused_time'])

            elapsed_time_str = secs_to_clock(activity_elapsed_time)
            paused_time_str = secs_to_clock(activity_paused_time)

            total_elapsed_time += activity_elapsed_time
            total_paused_time += activity_paused_time

            print(f"\nActivity: {activity}")
            print(f"  Total Elapsed Time: {elapsed_time_str}")
            print(f"  Total Paused Time: {paused_time_str}")

    # Total time across all activities
    total_elapsed_time_str = secs_to_clock(total_elapsed_time)
    total_paused_time_str = secs_to_clock(total_paused_time)

    print("\nTotal Time Across All Activities:")
    print(f"Total Elapsed Time: {total_elapsed_time_str}")
    print(f"Total Paused Time: {total_paused_time_str}")

    # Return total times as a dictionary
    return {
        "Total Elapsed Time": total_elapsed_time_str,
        "Total Paused Time": total_paused_time_str
    }

# # Example archive_dict
# archive_dict = {
#     'math': {'Total Elapsed Time': '00:00:10', 'Total Paused Time': '00:00:00'},
#     'math_break': {'Total Elapsed Time': '00:00:06', 'Total Paused Time': '00:00:00'},
#     'work': {'Total Elapsed Time': '00:00:03', 'Total Paused Time': '00:00:00'},
#     'work_break': {'Total Elapsed Time': '00:00:05', 'Total Paused Time': '00:00:00'}
# }




if __name__ == "__main__":
    display_time_summary(total)

