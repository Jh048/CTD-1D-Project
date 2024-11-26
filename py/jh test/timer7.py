import time
import threading
import sys

# Utility functions
def parse_time_input(time_input):
    time_parts = list(map(int, time_input.split(',')))
    if len(time_parts) == 1:
        return 0, 0, time_parts[0]
    elif len(time_parts) == 2:
        return 0, time_parts[0], time_parts[1]
    elif len(time_parts) == 3:
        return time_parts
    else:
        raise ValueError("Invalid input format. Use HH,MM,SS.")

def validate_time(hours, minutes, seconds):
    if hours < 0 or minutes < 0 or seconds < 0 or minutes >= 60 or seconds >= 60:
        raise ValueError("Time format is invalid. Ensure hours, minutes, and seconds are within limits.")

def convert_seconds_to_hms(total_seconds):
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return hours, minutes, seconds

def get_user_input():
    while True:
        try:
            print("\ne.g. 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec")
            time_input = input("Enter countdown time (HH,MM,SS): ").strip()
            hours, minutes, seconds = parse_time_input(time_input)
            validate_time(hours, minutes, seconds)
            return hours, minutes, seconds
        except ValueError as e:
            print(e)

# Timer functions
def display_timer(pause_flag, remaining_time_ref, total_paused_time_ref):
    while remaining_time_ref[0] > 0:
        if pause_flag.is_set():
            hours, minutes, seconds = convert_seconds_to_hms(remaining_time_ref[0])
            print(f"\rRemaining time: {hours:02}:{minutes:02}:{seconds:02} | Press 'p' to pause: ", end="")
            time.sleep(1)
            remaining_time_ref[0] -= 1
        else:
            total_paused_time_ref[0] += 1
            paused_hours, paused_minutes, paused_seconds = convert_seconds_to_hms(total_paused_time_ref[0])
            print(f"\rPause time: {paused_hours:02}:{paused_minutes:02}:{paused_seconds:02} | Press 'r' to resume:", end="")
            time.sleep(1)

    if remaining_time_ref[0] == 0:
        sys.stdout.write("\033[K")
        sys.stdout.write("\rRemaining time: 00:00:00 | Timer completed!")
        sys.stdout.write("\n")

def input_listener(pause_flag, remaining_time_ref, total_paused_time_ref):
    while remaining_time_ref[0] > 0:
        user_input = input().strip().lower()
        if user_input == "p" and pause_flag.is_set():
            pause_flag.clear()
        elif user_input == "r" and not pause_flag.is_set():
            pause_flag.set()
        elif user_input == "q":
            hours, minutes, seconds = convert_seconds_to_hms(remaining_time_ref[0])
            print(f"\nTimer stopped at: {hours:02}:{minutes:02}:{seconds:02}")
            remaining_time_ref[0] = 0
            total_paused_time = convert_seconds_to_hms(total_paused_time_ref[0])
            print(f"Total paused time: {total_paused_time[0]:02}:{total_paused_time[1]:02}:{total_paused_time[2]:02}")
            sys.exit()

def start_timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    remaining_time_ref = [total_seconds]
    total_paused_time_ref = [0]
    pause_flag = threading.Event()
    pause_flag.set()

    timer_thread = threading.Thread(target=display_timer, args=(pause_flag, remaining_time_ref, total_paused_time_ref), daemon=True)
    input_thread = threading.Thread(target=input_listener, args=(pause_flag, remaining_time_ref, total_paused_time_ref), daemon=True)

    timer_thread.start()
    input_thread.start()

    timer_thread.join()
    input_thread.join()

# Main function to wrap everything
def run_timer(*args):
    """
    Wrapper function to start the timer.
    Accepts:
        - No arguments (prompts user input).
        - Up to three arguments (hours, minutes, seconds).
    """
    if not args:
        hours, minutes, seconds = get_user_input()
    else:
        try:
            if len(args) == 1:
                hours, minutes, seconds = 0, 0, args[0]
            elif len(args) == 2:
                hours, minutes, seconds = 0, args[0], args[1]
            elif len(args) == 3:
                hours, minutes, seconds = args
            else:
                raise ValueError()
            validate_time(hours, minutes, seconds)
        except ValueError:
            print("Invalid input. Ensure time is in HH,MM,SS format.")
            return

    start_timer(hours, minutes, seconds)

# Example usage
# Uncomment the lines below to use the timer:
# run_timer(5)          # 5-second countdown
# run_timer(2, 25)      # 2 minutes, 25 seconds
# run_timer(1, 0, 5)    # 1 hour, 0 minutes, 5 seconds
# run_timer()           # Prompt user for input
run_timer(5)