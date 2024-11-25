import time # This module provides functions for manipulating time, including sleeping for a specific duration.
import threading # This module allows us to run multiple tasks concurrently (in parallel), such as handling the countdown and listening for user input simultaneously.

def timer(*args): # Defines the timer function that accepts variable arguments (*args). This allows the user to either pass in a time duration (e.g., 5 for 5 seconds) or leave it blank, prompting the function to ask for user input.
# 	*args allows the function to handle cases where the user may provide a specific time duration (e.g., 5 seconds, 2, 5 for 2 minutes 5 seconds, or 1, 0, 5 for 1 hour 0 minutes 5 seconds).
# 	If no arguments are passed (if not args), the function prompts the user to enter a time manually. If arguments are passed, the function processes them directly.

# Summary:

# 	*args is useful when you want to make your function flexible to accept any number of arguments.
# 	The arguments are accessed as a tuple within the function.
#   The name args is a convention, but you can use any name (e.g., *values, *numbers).

    # If args is empty, prompt the user for input
    if not args:
        while True:
            try:
                print("e.g. 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec")
                time_input = input("Enter countdown time in HH,MM,SS format: ").strip() #	.strip() removes any leading or trailing spaces from the input.
                time_parts = list(map(int, time_input.split(','))) # .split(',') splits the input string at commas, and map(int, ...) converts each part into an integer, resulting in a list of integers (time_parts).

                # Ensure the input has at least 1 part, and up to 3 parts
                # allow the input to be flexable instead of keeping it fix at xx,xx,xx
                if len(time_parts) == 1: 
                    hours, minutes, seconds = 0, 0, time_parts[0] # Only seconds are specified, so hours and minutes are set to 0.
                elif len(time_parts) == 2:
                    hours, minutes, seconds = 0, time_parts[0], time_parts[1] # Minutes and seconds are specified, so hours is set to 0.
                elif len(time_parts) == 3:
                    hours, minutes, seconds = time_parts # All three (hours, minutes, and seconds) are specified.
                else:
                    # If the input doesn’t contain 1, 2, or 3 parts, an error message is displayed, and the loop continues.
                    print("e.g. 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec")
                    print("Invalid input. Please enter time in the format HH,MM,SS.") 
                    continue
                # This block checks if any of the time components are negative or exceed valid ranges (minutes and seconds should be less than 60). 
                # If invalid, it prints an error and continues the loop.
                if hours < 0 or minutes < 0 or seconds < 0 or minutes >= 60 or seconds >= 60:
                    print("Invalid time format. Ensure hours, minutes, and seconds are correct.")
                    continue
                # If the user enters invalid values (e.g., non-numeric characters), a ValueError is raised, and the loop continues after printing the error message.
                break
            except ValueError:
                print("Invalid input. Please enter time in the format HH,MM,SS.")
    else:
        # If args is provided, handle different cases based on number of arguments
        # e.g. calling the function timer(1,0,5)
        if len(args) == 1:
            hours, minutes, seconds = 0, 0, args[0]
        elif len(args) == 2:
            hours, minutes, seconds = 0, args[0], args[1]
        elif len(args) == 3:
            hours, minutes, seconds = args
        else:
            print("e.g. 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec")
            print("Invalid time format. Ensure time is in the format (hours, minutes, seconds).")
            return

    total_seconds = hours * 3600 + minutes * 60 + seconds  # Convert input time to total seconds
    pause_flag = threading.Event()  # Event to manage pause and resume
    pause_flag.set()  # Start in running mode

    remaining_time = total_seconds # remaining_time holds the total time in seconds for the countdown.
    paused_time = 0 # paused_time is used to track the time spent in the paused state.

    def display_timer(): # to handle countdown and display.
        nonlocal remaining_time, paused_time
        # The statement nonlocal remaining_time, paused_time in Python is used within a nested function to indicate that the variables remaining_time
        # and paused_time are not local to the nested function but are instead defined in the nearest enclosing function scope.

        while remaining_time > 0: # The countdown loop continues while there’s remaining time (remaining_time > 0).
            if pause_flag.is_set():  # If not paused
                mins, secs = divmod(remaining_time, 60)
                hours, mins = divmod(mins, 60)
                # Parameters:
                #     •	remaining_time : The dividend (the number to be divided).
                #     •	60 : The divisor (the number to divide by).
                # Returns:
                #     •	A tuple (quotient, remainder):
                #     •	quotient = remaining_time // 60 (result of integer division).
                #     •	remainder = remainign_time % 60 (remainder after division).                
                print(f"\rRemaining time: {hours:02}:{mins:02}:{secs:02} | Press 'p' to pause:", end="") #	\r overwriting text dynamically on the same line.
                # The program then waits for 1 second using time.sleep(1) and decrements remaining_time by 1.
                time.sleep(1)
                remaining_time -= 1
            else:  # If paused (pause_flag.is_set() is False), it displays the paused time and increments paused_time.
                mins, secs = divmod(paused_time, 60)
                hours, mins = divmod(mins, 60)
                print(f"\rPause time: {hours:02}:{mins:02}:{secs:02} | Press 'r' to resume:", end="")
                time.sleep(1)
                paused_time += 1

        # Handle the final 0:00 case to ensure the time reaches 00:00
        if remaining_time == 0:
            print(f"\rRemaining time: 00:00:00 | Press 'p' to pause:", end="")

        print("\nTimer completed!")

    def input_listener():
        """Function to handle user input."""
        nonlocal paused_time
        while remaining_time > 0:
            user_input = input().strip().lower()
            if user_input == "p" and pause_flag.is_set():  # Pause
                pause_flag.clear()
                paused_time = 0  # Reset paused time counter
            elif user_input == "r" and not pause_flag.is_set():  # Resume
                pause_flag.set()
            elif remaining_time == 0:  # Exit when time is up
                break

    # Start threads for timer and user input
    timer_thread = threading.Thread(target=display_timer, daemon=True)
    input_thread = threading.Thread(target=input_listener, daemon=True)

    timer_thread.start()
    input_thread.start()

    # Wait for both threads to finish
    timer_thread.join()
    input_thread.join()

# Start the timer
# Example 1: timer(5) will start a 5-second countdown
# Example 2: timer(2, 5) will start a 2-minute 5-second countdown
# Example 3: timer(1, 0, 5) will start a 1-hour 0-minute 5-second countdown
timer()  # Example of calling the function with hours, minutes, and seconds