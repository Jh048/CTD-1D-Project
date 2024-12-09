import time
import threading
import sys
import copy

# Global variables
timer_data = []
quit_flag = threading.Event()  # Quit flag to control exit


def parse_time_input(args=None):
    """
    Parses time input from user or function arguments.
    Returns the time in hours, minutes, and seconds.
    """
    if args:
        # Handle input as arguments
        if len(args) == 1:
            return 0, 0, args[0]
        elif len(args) == 2:
            return 0, args[0], args[1]
        elif len(args) == 3:
            return args
        else:
            print("Invalid time format. Use HH,MM,SS.")
            return None
    else:
        # Handle user input
        while True:
            try:
                print("\ne.g. 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec")
                time_input = input("Enter countdown time (HH,MM,SS): ").strip()
                time_parts = list(map(int, time_input.split(',')))

                if len(time_parts) == 1:
                    return 0, 0, time_parts[0]
                elif len(time_parts) == 2:
                    return 0, time_parts[0], time_parts[1]
                elif len(time_parts) == 3:
                    return time_parts
                else:
                    print("Invalid input. Please enter time in the format HH,MM,SS.")
            except ValueError:
                print("Invalid input. Please enter numeric values in the format HH,MM,SS.")


def display_timer(total_seconds, pause_flag):
    """
    Displays the countdown timer.
    Pauses the timer if pause_flag is cleared.
    """
    remaining_time = total_seconds
    while remaining_time > 0:
        if quit_flag.is_set():
            break
        if pause_flag.is_set():
            mins, secs = divmod(remaining_time, 60)
            hours, mins = divmod(mins, 60)
            print(f"\rRemaining time: {hours:02}:{mins:02}:{secs:02} | Press 'p' to pause: ", end="")
            time.sleep(1)
            remaining_time -= 1
        else:
            time.sleep(1)
    return remaining_time


def pause_and_resume_timer(pause_flag, total_pause_time_list):
    """
    Listens for user input to pause, resume, or quit the timer.
    Tracks pause durations and updates total_pause_time_list.
    """
    paused_time = 0
    while not quit_flag.is_set():
        user_input = input().strip().lower()
        if user_input == "p" and pause_flag.is_set():
            pause_flag.clear()  # Pause the timer
            paused_time = 0
        elif user_input == "r" and not pause_flag.is_set():
            pause_flag.set()  # Resume the timer
            total_pause_time_list.append(paused_time)
        elif user_input == "q":
            quit_flag.set()  # Quit the timer
            if not pause_flag.is_set():
                total_pause_time_list.append(paused_time)
            break
        elif not pause_flag.is_set():
            paused_time += 1
            mins, secs = divmod(paused_time, 60)
            hours, mins = divmod(mins, 60)
            print(f"\rPause time: {hours:02}:{mins:02}:{secs:02} | Press 'r' to resume: ", end="")
    return paused_time


def calculate_summary(original_seconds, remaining_seconds, total_pause_time_list):
    """
    Calculates elapsed time and total paused time.
    Returns a summary dictionary.
    """
    elapsed_time = original_seconds - remaining_seconds
    total_pause_time = sum(total_pause_time_list) # -len(total_pause_time_list)?

    # Convert elapsed and paused time to HH:MM:SS format
    elapsed_hours, elapsed_remainder = divmod(elapsed_time, 3600)
    elapsed_minutes, elapsed_seconds = divmod(elapsed_remainder, 60)
    elapsed_time_str = f"{elapsed_hours:02}:{elapsed_minutes:02}:{elapsed_seconds:02}"

    pause_hours, pause_remainder = divmod(total_pause_time, 3600)
    pause_minutes, pause_seconds = divmod(pause_remainder, 60)
    paused_time_str = f"{pause_hours:02}:{pause_minutes:02}:{pause_seconds:02}"

    return {"elapsed_time": elapsed_time_str, "total_paused_time": paused_time_str}


def start_timer(hours=0, minutes=0, seconds=0):
    """
    Orchestrates the timer functionality.
    """
    global timer_data

    # Convert to total seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds
    original_total_seconds = copy.deepcopy(total_seconds)

    # Create a threading event for pause/resume
    pause_flag = threading.Event()
    pause_flag.set()

    # Track pause data
    total_pause_time_list = []

    # Threads for display and input
    timer_thread = threading.Thread(target=display_timer, args=(total_seconds, pause_flag), daemon=True)
    input_thread = threading.Thread(target=pause_and_resume_timer, args=(pause_flag, total_pause_time_list), daemon=True)

    # Start threads
    timer_thread.start()
    input_thread.start()

    # Wait for threads to finish
    timer_thread.join()
    input_thread.join()

    # Calculate and display summary
    summary = calculate_summary(original_total_seconds, total_seconds, total_pause_time_list)
    timer_data.append(summary)

    print("\nTimer finished!")
    print(f"Elapsed Time: {summary['elapsed_time']}")
    print(f"Total Paused Time: {summary['total_paused_time']}")


def main():
    """
    Main function to handle user input and call the timer.
    """
    user_input = parse_time_input()
    if user_input:
        hours, minutes, seconds = user_input
        start_timer(hours, minutes, seconds)


if __name__ == "__main__":
    main()
    print(timer_data)