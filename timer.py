import time # Used to manage delays and countdown timing in seconds.
import threading # Enables concurrent execution of code (to run the timer and handle user inputs simultaneously).
import sys # Used to manipulate the output in the terminal for updating countdown visuals.

def timer(*args):
# The timer function accepts an optional set of arguments representing the time in hours, minutes, and seconds.

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

    pause_flag = threading.Event() # threading.Event is used for pause and resume the timer.
    pause_flag.set() # Initializes the flag as active (running state).

    remaining_time = total_seconds #Tracks the countdown’s remaining seconds.
    paused_time = 0 # Tracks how long the timer has been paused in the current pause session.
    total_paused_time = 0  # Tracks the total duration the timer was paused.

    def display_timer():
        nonlocal remaining_time, paused_time, total_paused_time
        while remaining_time > 0:
            if pause_flag.is_set():
                # During active countdown (pause_flag.is_set()), it decrements remaining_time.
                mins, secs = divmod(remaining_time, 60)
                hours, mins = divmod(mins, 60)
                # Uses divmod to convert seconds into hours, minutes, and seconds.

                print(f"\rRemaining time: {hours:02}:{mins:02}:{secs:02} | Press 'p' to pause: ", end="")
                # Updates the display using \r (carriage return) to overwrite the previous output.

                time.sleep(1)
                remaining_time -= 1
            else:
                # During pause (not pause_flag.is_set()), it tracks paused_time.
                total_paused_time += 1
                mins, secs = divmod(paused_time, 60)
                hours, mins = divmod(mins, 60)

                print(f"\rPause time: {hours:02}:{mins:02}:{secs:02} | Press 'r' to resume:", end="")
                time.sleep(1)
                paused_time += 1

        if remaining_time == 0:
            sys.stdout.write("\033[K")
            sys.stdout.write("\rRemaining time: 00:00:00 | Timer completed!    ")
            # Clears the line and displays “Timer completed!”.
            sys.stdout.write("\n")

            mins, secs = divmod(total_paused_time, 60)
            hours, mins = divmod(mins, 60)
            paused_time_str = f"{hours:02}:{mins:02}:{secs:02}" if hours > 0 else f"{mins:02}:{secs:02}"
            print(f"Total paused time: {paused_time_str}")
            # Displays the total time the timer was paused.
        
            
            

    def input_listener():
        nonlocal remaining_time, paused_time
        while remaining_time > 0:
            user_input = input().strip().lower()
            if user_input == "p" and pause_flag.is_set(): # Pause the time
                pause_flag.clear()
                paused_time = 0
            elif user_input == "r" and not pause_flag.is_set(): # Resume the time
                pause_flag.set()
            elif user_input == "q": # Stop the time
                mins, secs = divmod(remaining_time, 60)
                hours, mins = divmod(mins, 60)
                print()
                sys.stdout.write("\033[K")
                sys.stdout.write(f"\rRemaining time: {hours:02}:{mins:02}:{secs:02} | Timer stopped.    ")
                # Clears the line and displays “Timer completed!”.
                sys.stdout.write("\n")
                remaining_time = 0
                
                mins, secs = divmod(total_paused_time, 60)
                hours, mins = divmod(mins, 60)
                paused_time_str = f"{hours:02}:{mins:02}:{secs:02}" if hours > 0 else f"{mins:02}:{secs:02}"
                print(f"Total paused time: {paused_time_str}")
                # Displays the total time the timer was paused.
                time.sleep(1)
                sys.exit()
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

# Start the timer
# Example 1: timer(5) will start a 5-second countdown
# Example 2: timer(2, 5) will start a 2-minute 5-second countdown
# Example 3: timer(1, 0, 5) will start a 1-hour 0-minute 5-second countdown
# Example 4: timer() will ask the user for input
''' Example 5:
if using timer() in another file under the same folder
can import timer as t
t.timer() to sue i another file'''

# timer()  # Example of calling the function with hours, minutes, and seconds