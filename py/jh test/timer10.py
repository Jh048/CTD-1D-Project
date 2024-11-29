import time
import threading
import sys
import copy
import argparse
from pynput import keyboard

# Global variables for data tracking
timer_data = []
quit_flag = threading.Event()  # Global quit flag to control exit


def timer(hours=0, minutes=0, seconds=0):
    """
    Countdown timer function with pause, resume, and quit features.
    """
    global timer_data, quit_flag

    total_seconds = hours * 3600 + minutes * 60 + seconds
    if total_seconds <= 0:
        print("Timer duration must be greater than zero!")
        return

    original_total_time = copy.deepcopy(total_seconds)
    pause_flag = threading.Event()  # Pause flag
    pause_flag.set()  # Start in running state
    remaining_time = total_seconds
    paused_time = 0
    total_pause_time_list = []
    pause_count = 0
    resume_count = 0

    def display_timer():
        nonlocal remaining_time, paused_time
        while remaining_time > 0:
            if quit_flag.is_set():  # Stop the timer if quit flag is set
                break
            if pause_flag.is_set():  # Timer is running
                mins, secs = divmod(remaining_time, 60)
                hours, mins = divmod(mins, 60)
                print(f"\rRemaining time: {hours:02}:{mins:02}:{secs:02} | Press 'p' to pause: ", end="")
                time.sleep(1)
                remaining_time -= 1
            else:  # Timer is paused
                mins, secs = divmod(paused_time, 60)
                hours, mins = divmod(mins, 60)
                print(f"\rPause time: {hours:02}:{mins:02}:{secs:02} | Press 'r' to resume: ", end="")
                paused_time += 1
                time.sleep(1)

        if remaining_time == 0 and not quit_flag.is_set():
            sys.stdout.write("\033[K")
            print("\rRemaining time: 00:00:00 | Timer completed!")
            paused_time_str = format_time(paused_time)
            elapsed_time_str = format_time(original_total_time)
            log_timer_data(elapsed_time_str, paused_time_str)

    def input_listener():
        nonlocal paused_time, pause_count, resume_count
        while remaining_time > 0:
            user_input = input().strip().lower()
            if user_input == "p" and pause_flag.is_set():  # Pause
                pause_flag.clear()
                pause_count += 1
                paused_time = 0
            elif user_input == "r" and not pause_flag.is_set():  # Resume
                pause_flag.set()
                total_pause_time_list.append(paused_time)
                resume_count += 1
            elif user_input == "q":  # Quit
                quit_flag.set()
                total_pause_time_list.append(paused_time)
                break

    def log_timer_data(elapsed_time_str, paused_time_str):
        """
        Logs timer data into a global list.
        """
        timer_data.append({
            "elapsed_time": elapsed_time_str,
            "paused_time": paused_time_str
        })
        print("\nTimer Summary:")
        print(f"Elapsed Time: {elapsed_time_str}")
        print(f"Paused Time: {paused_time_str}")

    timer_thread = threading.Thread(target=display_timer, daemon=True)
    input_thread = threading.Thread(target=input_listener, daemon=True)

    timer_thread.start()
    input_thread.start()

    timer_thread.join()
    input_thread.join()


def format_time(total_seconds):
    """
    Formats total seconds into HH:MM:SS format.
    """
    mins, secs = divmod(total_seconds, 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02}:{mins:02}:{secs:02}"


def parse_input(input_time):
    """
    Parses input string into hours, minutes, and seconds.
    """
    try:
        time_parts = list(map(int, input_time.split(',')))
        if len(time_parts) == 1:
            return 0, 0, time_parts[0]
        elif len(time_parts) == 2:
            return 0, time_parts[0], time_parts[1]
        elif len(time_parts) == 3:
            return time_parts[0], time_parts[1], time_parts[2]
    except ValueError:
        print("Invalid input. Use format HH,MM,SS.")
    return 0, 0, 0


def main():
    """
    Entry point for CLI usage.
    """
    parser = argparse.ArgumentParser(description="Countdown Timer with Pause/Resume/Quit features")
    parser.add_argument("-t", "--time", type=str, help="Timer duration in HH,MM,SS format (e.g., 1,30 for 1 min 30 sec)")
    args = parser.parse_args()

    if args.time:
        hours, minutes, seconds = parse_input(args.time)
        timer(hours, minutes, seconds)
    else:
        print("Interactive mode: Enter time in HH,MM,SS format")
        input_time = input("Enter countdown time: ")
        hours, minutes, seconds = parse_input(input_time)
        timer(hours, minutes, seconds)


if __name__ == "__main__":
    print("Press 'p' to pause, 'r' to resume, or 'q' to quit the timer during execution.")
    print("Alternatively, use --time argument to specify timer duration.")
    main()