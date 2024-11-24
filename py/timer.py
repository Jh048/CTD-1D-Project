import time
import threading

def timer(*args):
    # If args is empty, prompt the user for input
    if not args:
        while True:
            try:
                time_input = input("Enter countdown time in HH,MM,SS format (e.g., 1,0,5): ").strip()
                time_parts = list(map(int, time_input.split(',')))

                # Ensure the input has at least 1 part, and up to 3 parts
                if len(time_parts) == 1:
                    hours, minutes, seconds = 0, 0, time_parts[0]
                elif len(time_parts) == 2:
                    hours, minutes, seconds = 0, time_parts[0], time_parts[1]
                elif len(time_parts) == 3:
                    hours, minutes, seconds = time_parts
                else:
                    print("Invalid input. Please enter time in the format HH,MM,SS.")
                    continue

                if hours < 0 or minutes < 0 or seconds < 0 or minutes >= 60 or seconds >= 60:
                    print("Invalid time format. Ensure hours, minutes, and seconds are correct.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter time in the format HH,MM,SS.")
    else:
        # If args is provided, handle different cases based on number of arguments
        if len(args) == 1:
            hours, minutes, seconds = 0, 0, args[0]
        elif len(args) == 2:
            hours, minutes, seconds = 0, args[0], args[1]
        elif len(args) == 3:
            hours, minutes, seconds = args
        else:
            print("Invalid time format. Ensure time is in the format (hours, minutes, seconds).")
            return

    total_seconds = hours * 3600 + minutes * 60 + seconds  # Convert input time to total seconds
    pause_flag = threading.Event()  # Event to manage pause and resume
    pause_flag.set()  # Start in running mode

    remaining_time = total_seconds
    paused_time = 0

    def display_timer():
        """Function to handle countdown and display."""
        nonlocal remaining_time, paused_time

        while remaining_time > 0:
            if pause_flag.is_set():  # If not paused
                mins, secs = divmod(remaining_time, 60)
                hours, mins = divmod(mins, 60)
                print(f"\rRemaining time: {hours:02}:{mins:02}:{secs:02} | Press 'p' to pause:", end="")
                time.sleep(1)
                remaining_time -= 1
            else:  # If paused
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