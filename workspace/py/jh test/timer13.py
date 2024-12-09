import time
import threading
import sys

# Global variables
timer_data = []
quit_flag = threading.Event()
pause_flag = threading.Event()

def parse_timer_input(input_str):
    """
    Parses a timer input string in the format 'HH:MM:SS' or 'MM:SS' or 'SS'.
    """
    try:
        parts = list(map(int, input_str.split(':')))
        if len(parts) == 1:
            return 0, 0, parts[0]
        elif len(parts) == 2:
            return 0, parts[0], parts[1]
        elif len(parts) == 3:
            return parts[0], parts[1], parts[2]
        else:
            raise ValueError
    except ValueError:
        print("Invalid input format. Please use HH:MM:SS, MM:SS, or SS.")
        return None

def run_timer(duration, timer_type):
    """
    Runs the countdown timer for the specified duration with pause and resume.
    """
    global timer_data
    total_seconds = duration[0] * 3600 + duration[1] * 60 + duration[2]
    remaining_time = total_seconds
    paused_time = 0
    pause_count = 0
    session_data = {"type": timer_type, "elapsed_time": 0, "paused_time": 0, "pause_count": 0}

    while remaining_time > 0:
        if quit_flag.is_set():
            break

        if pause_flag.is_set():  # Timer is running
            mins, secs = divmod(remaining_time, 60)
            hours, mins = divmod(mins, 60)
            print(f"\r{timer_type} Time: {hours:02}:{mins:02}:{secs:02} | Press 'p' to pause, 'q' to quit.", end="")
            time.sleep(1)
            remaining_time -= 1
            session_data["elapsed_time"] += 1
        else:  # Timer is paused
            mins, secs = divmod(paused_time, 60)
            hours, mins = divmod(mins, 60)
            print(f"\r{timer_type} Paused: {hours:02}:{mins:02}:{secs:02} | Press 'r' to resume, 'q' to quit.", end="")
            time.sleep(1)
            paused_time += 1

    if remaining_time == 0 and not quit_flag.is_set():
        print(f"\n{timer_type} session complete!")

    session_data["paused_time"] = paused_time
    session_data["pause_count"] = pause_count
    timer_data.append(session_data)

def pomodoro_timer(work_time, rest_time):
    """
    Runs the Pomodoro timer with alternating work and rest sessions.
    """
    while not quit_flag.is_set():
        print("\nStarting work session...")
        pause_flag.set()  # Start in the running state
        run_timer(work_time, "Work")
        if quit_flag.is_set():
            break
        print("\nStarting rest session...")
        pause_flag.set()
        run_timer(rest_time, "Rest")

    print("\nPomodoro timer stopped.")
    print("\nSession Summary:", timer_data)

def user_input_listener():
    """
    Listens for user input to pause, resume, or quit the timer.
    """
    global pause_flag
    while not quit_flag.is_set():
        user_input = input().strip().lower()
        if user_input == 'p' and pause_flag.is_set():  # Pause
            pause_flag.clear()
        elif user_input == 'r' and not pause_flag.is_set():  # Resume
            pause_flag.set()
        elif user_input == 'q':  # Quit
            quit_flag.set()

def timer(work_and_rest):
    """
    Accepts two durations for work and rest in the format 'HH:MM:SS, HH:MM:SS' or simpler.
    Example: timer("25:0, 5:0") -> 25 minutes work, 5 minutes rest.
    """
    try:
        # Split input into two parts
        work_str, rest_str = work_and_rest.split(',')
        work_time = parse_timer_input(work_str.strip())
        rest_time = parse_timer_input(rest_str.strip())

        if work_time is None or rest_time is None:
            print("Invalid input. Please try again.")
            return

        # Start the input listener in a separate thread
        input_thread = threading.Thread(target=user_input_listener, daemon=True)
        input_thread.start()

        # Start the Pomodoro timer
        pomodoro_timer(work_time, rest_time)
    except ValueError:
        print("Invalid input format. Use 'HH:MM:SS, HH:MM:SS' or similar.")
        return

# Example usage
print("Enter work and rest times in the format 'HH:MM:SS, HH:MM:SS'.")
user_input = input("Timer Input: ").strip()
timer(user_input)