import time # Used to manage delays and countdown timing in seconds.
import threading # Enables concurrent execution of code (to run the timer and handle user inputs simultaneously).
import sys # Used to manipulate the output in the terminal for updating countdown visuals.
import copy




title = []
user_input = None
quit_flag = threading.Event()  # Global quit flag to control exit
elapsed_time = 0
archive_dict = {}
title = None


def secs_to_clock(sec):
    mins, secs = divmod(sec, 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02}:{mins:02}:{secs:02}"

# If arguments are passed directly (args), the function parses them similarly to user input.
def args(a):
    if len(a) == 1:
        hours, minutes, seconds = 0, 0, args[0]
    elif len(a) == 2:
        hours, minutes, seconds = 0, args[0], args[1]
    elif len(a) == 3:
        hours, minutes, seconds = args
    else:
        print("e.g. 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec")
        print("Invalid time format. Ensure time is in the).")
        return
    


def timer(*args):
# The timer function accepts an optional set of arguments representing the time in hours, minutes, and seconds.
    global title, user_input, quit_flag, elapsed_time

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
        args(args)
            
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
        
        nonlocal remaining_time, paused_time, pause_count, resume_count, original_total_time
        while remaining_time > 0:
            
            if quit_flag.is_set(): # If quit flag is set, break out of the loop
                break
            if pause_flag.is_set(): 
                # During active countdown (pause_flag.is_set()), it decrements remaining_time.
                # mins, secs = divmod(remaining_time, 60)
                # hours, mins = divmod(mins, 60)
                # Uses divmod to convert seconds into hours, minutes, and seconds.
                print(f"\rRemaining time: {secs_to_clock(remaining_time)} | Press 'p' to pause, Press 'q' to quit: ",end="")

                # Updates the display using \r (carriage return) to overwrite the previous output.

                time.sleep(1)
                remaining_time -= 1
            else:
                # During pause (not pause_flag.is_set()), it tracks paused_time.

                print(f"\rPause time: {secs_to_clock(paused_time)} | Press 'r' to resume, Press 'q' to quit:", end="")
                paused_time += 1
                time.sleep(1)
                
                

        if remaining_time == 0 and not user_input == "q":
            sys.stdout.write("\033[K")
            sys.stdout.write("\rRemaining time: 00:00:00 | Timer completed!    ")
            # Clears the line and displays “Timer completed!”.
            sys.stdout.write("\n")
            paused_time_str = f"{secs_to_clock(total_pause_time)}"
            # Displays the total time the timer was paused.
            
            elapsed_time = original_total_time - remaining_time

            elapsed_time_str = f"{secs_to_clock(elapsed_time)}"

            # Store details in the global list
            title = ({
                "elapsed_time": elapsed_time_str,
                "paused_time": paused_time_str
            })
            return paused_time_str 
                   
            
    
    def input_listener():
        nonlocal remaining_time, paused_time, pause_count, resume_count, total_pause_time_list, total_pause_time
        while remaining_time > 0:
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
                quit_flag.set()  # Set the quit flag to stop both threads

                # Add the current paused time to the total pause list
                if not pause_flag.is_set() and paused_time > 0:
                    total_pause_time_list.append(paused_time )

                # Calculate total pause time
                total_pause_time = sum(total_pause_time_list) - len(total_pause_time_list)

                # Calculate elapsed time
                elapsed_time = original_total_time - remaining_time

                # Format total paused time string

                paused_time_str = f"{secs_to_clock(total_pause_time)}"


                elapsed_time_str = f"{secs_to_clock(elapsed_time)}"


                # Store details in the global list
                key_name = str(title)
                archive_dict[key_name].append({
                    "Elapsed_time": elapsed_time_str,
                    "Total_paused_time": paused_time_str})

                # Display summary
                print("\nTimer Summary:")
                print(f"Elapsed Time: {elapsed_time_str}")
                print(f"Total Pause Time: {paused_time_str}")

                time.sleep(1)
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
    
    print(total_pause_time_list)
    print(total_pause_time)
    print(elapsed_time)
    print(title)
    print(archive_dict)

    
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



def start_or_archive():
    global title
    Start_or_archive = input('Do you want to start a timer?(y/n): ').lower()
    if Start_or_archive == 'y':
        title = input ("Do you want to study, work or others?") .lower()
        if title== "study":
            #default timer for study
            print (f'You have chosen {title}')
            archive_dict[title] = []
            timer()
        elif title == "work":
            #default for study
            print (f'You have chosen {title}')
            archive_dict[title] = []
            timer()
        elif title == "others":
            other_activity= input ("What do you want to do today?") .lower()
            #ask for duration function
            print (f'You have chosen {other_activity}')
            archive_dict[title] = []
            timer()
        

    
        
        # print(f"working session: {title}")
        
    elif Start_or_archive =='n':
        Archive= input ('Do you want to look at your history?(y/n): ').lower()
        if Archive == 'y':
            view_archive()
        elif Archive == 'n':
            print ('Bye! Have a great day!')
        else:
            print("incorrct input, please try again")
    else:
        print ('invalid')


#def view_archive():
    #total_time = 0
    #for i in archive_dict:
        #print(archive_dict)
        #print(i,archive_dict[i]['Elapsed_time'])
        #total_time = total_time + int(archive_dict[i]['Elapsed_time'])

    
    #print(total_time)
def clock_to_secs(clock_time):
    """Converts HH:MM:SS format to total seconds."""
    try:
        hours, minutes, seconds = map(int, clock_time.split(":"))
        return hours * 3600 + minutes * 60 + seconds
    except ValueError:
        print(f"Invalid time format: {clock_time}. Expected HH:MM:SS format.")
        return 0


def view_archive():
    """Displays the archive and calculates total study and work times."""
    total_study_time = 0
    total_work_time = 0

    # Loop through the archive dictionary to process each activity and its sessions
    for activity, sessions in archive_dict.items():
        print(f"{activity.capitalize()} Sessions:")
        for session in sessions:
            elapsed_time = clock_to_secs(session.get("Elapsed_time", "00:00:00"))
            paused_time = session.get("Total_paused_time", "00:00:00")
            print(f"  Elapsed Time: {session.get('Elapsed_time', '00:00:00')}, Paused Time: {paused_time}")

            # Accumulate the elapsed time based on the activity type
            if activity == "study":
                total_study_time += elapsed_time
            elif activity == "work":
                total_work_time += elapsed_time

    # Display the total study and work times in HH:MM:SS format
    print(f"\nTotal Study Time: {secs_to_clock(total_study_time)}")
    print(f"Total Work Time: {secs_to_clock(total_work_time)}")



def data():
    global title
    # Ensure timer_data has entries before processing
    if not title:
        print("No data available.")
        return None

    # Extract elapsed and paused times from timer_data
    study_times = []  # For elapsed work session times
    break_times = []  # For total paused times

    for entry in title:
        # Convert the "elapsed_time" and "paused_time" strings to total minutes
        elapsed_time = entry.get("elapsed_time", "00:00:00")
        paused_time = entry.get("paused_time", "00:00:00")

        study_times.append(secs_to_clock(elapsed_time))
        break_times.append(secs_to_clock(paused_time))

    # Build the dictionary with the summed data
    pomodoro_data = {
        'study': sum(study_times),  # Total study time in minutesy
        'break': sum(break_times)  # Total break time in minutes
    }

    return pomodoro_data

#if __name__ == "__main__":
#    start_or_archive()

while(True):
    quit = input('Do you want to continue?:(y/n)').lower()
    if quit == 'y':
        if quit_flag.is_set():
            quit_flag.clear()
        start_or_archive()
    else:
        break
