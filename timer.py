import time # Used to manage delays and countdown timing in seconds.
import threading # Enables concurrent execution of code (to run the timer and handle user inputs simultaneously).
import sys # Used to manipulate the output in the terminal for updating countdown visuals.
import copy
timer_data = []
user_input = None
quit_flag = threading.Event()  # Global quit flag to control exit
elapsed_time = 0

def timer(*args):
# The timer function accepts an optional set of arguments representing the time in hours, minutes, and seconds.
    global timer_data, user_input, quit_flag, elapsed_time

    if not args:
    # If no arguments are passed, the function prompts the user to enter a countdown time in the format HH,MM,SS

        while True:
            try:
                print()
                print("e.g. 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec")
                time_input = input("Enter countdown time (HH,MM,SS): ").strip()
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
        
        nonlocal remaining_time, paused_time, pause_count, resume_count
        while remaining_time > 0:
            if quit_flag.is_set(): # If quit flag is set, break out of the loop
                break
            if pause_flag.is_set(): 
                # During active countdown (pause_flag.is_set()), it decrements remaining_time.
                mins, secs = divmod(remaining_time, 60)
                hours, mins = divmod(mins, 60)
                # Uses divmod to convert seconds into hours, minutes, and seconds.

                print(f"\rRemaining time: {hours:02}:{mins:02}:{secs:02} | Press 'p' to pause, Press 'q' to quit: ",end="")
                # Updates the display using \r (carriage return) to overwrite the previous output.

                time.sleep(1)
                remaining_time -= 1
            else:
                # During pause (not pause_flag.is_set()), it tracks paused_time.
                
                mins, secs = divmod(paused_time, 60)
                hours, mins = divmod(mins, 60)

                print(f"\rPause time: {hours:02}:{mins:02}:{secs:02} | Press 'r' to resume, Press 'q' to quit:", end="")
                paused_time += 1
                time.sleep(1)
                
                

        if remaining_time == 0 and not user_input == "q":
            sys.stdout.write("\033[K")
            sys.stdout.write("\rRemaining time: 00:00:00 | Timer completed!    ")
            # Clears the line and displays “Timer completed!”.
            sys.stdout.write("\n")

            mins, secs = divmod((paused_time - resume_count), 60)
            hours, mins = divmod(mins, 60)
            paused_time_str = f"{hours:02}:{mins:02}:{secs:02}" if hours > 0 else f"{mins:02}:{secs:02}"
            # Displays the total time the timer was paused.
            
            elapsed_time = original_total_time - remaining_time
            elapsed_mins, elapsed_secs = divmod(elapsed_time, 60)
            elapsed_hours, elapsed_mins = divmod(elapsed_mins, 60)
            elapsed_time_str = f"{elapsed_hours:02}:{elapsed_mins:02}:{elapsed_secs:02}" if hours > 0 else f"{mins:02}:{secs:02}"

            # Store details in the global list
            timer_data.append({
                "elapsed_time": elapsed_time_str,
                "paused_time": paused_time_str
            })
            return paused_time_str 
                   
            
    
    def input_listener():
        nonlocal remaining_time, paused_time, pause_count, resume_count, total_pause_time_list, total_pause_time
        while remaining_time > 0 :
            user_input = input().strip().lower()
            if user_input == "p" and pause_flag.is_set(): # Pause the time
                pause_flag.clear()
                paused_time = 0
                pause_count += 1

            elif user_input == "r" and not pause_flag.is_set(): # Resume the time
                pause_flag.set()
                total_pause_time_list.append(paused_time-1)
                resume_count += 1

            elif user_input == "q": # Stop the time
                quit_flag.set()  # Set quit flag to stop both threads
                total_pause_time_list.append(paused_time-1)


                mins, secs = divmod(remaining_time, 60)
                hours, mins = divmod(mins, 60)
                print()
                sys.stdout.write("\033[K")
                sys.stdout.write(f"\rRemaining time: {hours:02}:{mins:02}:{secs:02} | Timer stopped.    ")
                # Clears the line and displays “Timer completed!”.
                sys.stdout.write("\n")
              
                mins, secs = divmod(total_pause_time, 60)
                hours, mins = divmod(mins, 60)
                paused_time_str = f"{hours:02}:{mins:02}:{secs:02}" if hours > 0 else f"{mins:02}:{secs:02}"

                elapsed_time = original_total_time - remaining_time
                elapsed_mins, elapsed_secs = divmod(elapsed_time, 60)
                elapsed_hours, elapsed_mins = divmod(elapsed_mins, 60)
                elapsed_time_str = f"{elapsed_hours:02}:{elapsed_mins:02}:{elapsed_secs:02}" if hours > 0 else f"{mins:02}:{secs:02}"

                # Store details in the global list
                timer_data.append({
                    "elapsed_time": elapsed_time_str,
                    "Total paused_time": paused_time_str
                })
                
                # Displays the total time the timer was paused.
                
                
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
    print(timer_data)
    print(total_pause_time_list)


    
# Start the timer
# Example 1: timer(5) will start a 5-second countdown
# Example 2: timer(2, 5) will start a 2-minute 5-second countdown
# Example 3: timer(1, 0, 5) will start a 1-hour 0-minute 5-second countdown
# Example 4: timer() will ask the user for input
''' Example 5:
if using timer() in another file under the same folder
can import timer as t
t.timer() to use i another file'''

timer()  # Example of calling the function with hours, minutes, and seconds
