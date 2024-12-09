import time
import threading
import sys

def parse_time_input(input_string):
    """
    Parses the input time string into hours, minutes, and seconds.

    Args:
        input_string (str): Time input as a string (e.g., "5", "2,25", "1,0,5").

    Returns:
        tuple: (hours, minutes, seconds) if valid, None otherwise.
    """
    try:
        time_parts = list(map(int, input_string.split(',')))

        if len(time_parts) == 1:
            return 0, 0, time_parts[0]
        elif len(time_parts) == 2:
            return 0, time_parts[0], time_parts[1]
        elif len(time_parts) == 3:
            return time_parts[0], time_parts[1], time_parts[2]
        else:
            return None
    except ValueError:
        return None

def format_time(hours, minutes, seconds):
    """
    Formats time into a string as HH:MM:SS or MM:SS.

    Args:
        hours (int): Hours.
        minutes (int): Minutes.
        seconds (int): Seconds.

    Returns:
        str: Formatted time string.
    """
    if hours > 0:
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    else:
        return f"{minutes:02}:{seconds:02}"

def timer(hours=0, minutes=0, seconds=0):
    """
    Starts a countdown timer with pause and resume functionality.

    Args:
        hours (int): Hours for the timer.
        minutes (int): Minutes for the timer.
        seconds (int): Seconds for the timer.
    """
    total_seconds = hours * 3600 + minutes * 60 + seconds
    if total_seconds <= 0:
        print("Invalid time. Please enter a positive value.")
        return

    pause_flag = threading.Event()
    pause_flag.set()

    remaining_time = total_seconds
    paused_time = 0
    total_paused_time = 0

    def display_timer():
        """
        Displays the countdown timer and handles updates.
        """
        nonlocal remaining_time, paused_time, total_paused_time
        while remaining_time > 0:
            if pause_flag.is_set():
                mins, secs = divmod(remaining_time, 60)
                hrs, mins = divmod(mins, 60)
                print(f"\rRemaining time: {format_time(hrs, mins, secs)} | Press 'p' to pause, 'q' to quit: ", end="")
                sys.stdout.flush()
                time.sleep(1)
                remaining_time -= 1
            else:
                total_paused_time += 1
                mins, secs = divmod(paused_time, 60)
                hrs, mins = divmod(mins, 60)
                print(f"\rPaused time: {format_time(hrs, mins, secs)} | Press 'r' to resume, 'q' to quit: ", end="")
                sys.stdout.flush()
                time.sleep(1)
                paused_time += 1

        print("\nTimer completed!")
        mins, secs = divmod(total_paused_time, 60)
        hrs, mins = divmod(mins, 60)
        print(f"Total paused time: {format_time(hrs, mins, secs)}")

    def input_listener():
        """
        Listens for user input to pause, resume, or quit the timer.
        """
        nonlocal paused_time, remaining_time
        while remaining_time > 0:
            user_input = input().strip().lower()
            if user_input == "p" and pause_flag.is_set():
                pause_flag.clear()
                paused_time = 0
            elif user_input == "r" and not pause_flag.is_set():
                pause_flag.set()
            elif user_input == "q":
                remaining_time = 0
                print("\nTimer stopped.")
                break

    timer_thread = threading.Thread(target=display_timer, daemon=True)
    input_thread = threading.Thread(target=input_listener, daemon=True)

    timer_thread.start()
    input_thread.start()

    timer_thread.join()
    input_thread.join()

if __name__ == "__main__":
    print("Enter countdown time in the format:")
    print("  - Seconds: 30")
    print("  - Minutes and seconds: 2,30")
    print("  - Hours, minutes, and seconds: 1,2,15")
    print("Type 'q' at any time to quit the timer.")

    while True:
        time_input = input("Enter countdown time (HH,MM,SS): ").strip()
        if time_input.lower() == 'q':
            print("Exiting timer.")
            break

        parsed_time = parse_time_input(time_input)
        if parsed_time is None:
            print("Invalid input. Please try again.")
            continue

        hours, minutes, seconds = parsed_time
        if hours < 0 or minutes < 0 or seconds < 0 or minutes >= 60 or seconds >= 60:
            print("Invalid time format. Ensure hours, minutes, and seconds are correct.")
            continue

        timer(hours, minutes, seconds)
        break