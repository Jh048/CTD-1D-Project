import time  # For managing delays and countdown timing
import threading  # Enables concurrent execution of code
import sys  # Used to manipulate the terminal output
import copy

# Global variables for storing timer data
timer_data = []
quit_flag = threading.Event()  # Global quit flag to control exit
elapsed_time = 0

# Utility function to format seconds into HH:MM:SS
def secs_to_clock(sec):
    mins, secs = divmod(sec, 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02}:{mins:02}:{secs:02}"

# Timer function
def timer(*args, title=None):
    global timer_data, quit_flag

    if not args:
        # If no arguments are passed, prompt the user for input
        while True:
            try:
                print("\nEnter countdown time in the format HH,MM,SS (e.g., 1,30,0):")
                print("Examples: 5 = 5 seconds | 2,25 = 2 min 25 sec | 1,0,5 = 1 hr 0 min 5 sec")
                time_input = input("Enter time: ").strip()
                time_parts = list(map(int, time_input.split(',')))

                if len(time_parts) == 1:
                    hours, minutes, seconds = 0, 0, time_parts[0]
                elif len(time_parts) == 2:
                    hours, minutes, seconds = 0, time_parts[0], time_parts[1]
                elif len(time_parts) == 3:
                    hours, minutes, seconds = time_parts
                else:
                    print("Invalid input. Please use the format HH,MM,SS.")
                    continue

                if hours < 0 or minutes < 0 or seconds < 0 or minutes >= 60 or seconds >= 60:
                    print("Invalid input. Hours, minutes, and seconds must be non-negative, and minutes/seconds < 60.")
                    continue

                break
            except ValueError:
                print("Invalid input. Please enter valid numbers in the format HH,MM,SS.")
    else:
        # Parse arguments if directly passed
        if len(args) == 1:
            hours, minutes, seconds = 0, 0, args[0]
        elif len(args) == 2:
            hours, minutes, seconds = 0, args[0], args[1]
        elif len(args) == 3:
            hours, minutes, seconds = args
        else:
            print("Invalid input. Please ensure time is in the format HH,MM,SS.")
            return

    total_seconds = hours * 3600 + minutes * 60 + seconds
    original_total_time = copy.deepcopy(total_seconds)

    pause_flag = threading.Event()  # Used to pause and resume the timer
    pause_flag.set()  # Start with the timer running
    remaining_time = total_seconds
    paused_time = 0
    total_pause_time = 0

    def display_timer():
        nonlocal remaining_time, paused_time, total_pause_time

        while remaining_time > 0:
            if quit_flag.is_set():  # Quit signal received
                print("\nTimer interrupted. Exiting...")
                return

            if pause_flag.is_set():
                print(f"\rRemaining time: {secs_to_clock(remaining_time)} | Press 'p' to pause, 'q' to quit: ", end="")
                time.sleep(1)
                remaining_time -= 1
            else:
                print(f"\rPaused. Press 'r' to resume, 'q' to quit.", end="")
                paused_time += 1
                time.sleep(1)

        if remaining_time == 0 and not quit_flag.is_set():
            print("\nTimer completed!")
            elapsed_time = original_total_time - remaining_time
            total_pause_time = paused_time
            elapsed_time_str = secs_to_clock(elapsed_time)
            paused_time_str = secs_to_clock(total_pause_time)
            timer_data.append({
                "elapsed_time": elapsed_time_str,
                "paused_time": paused_time_str
            })

    def input_listener():
        nonlocal remaining_time, paused_time, total_pause_time

        while remaining_time > 0:
            user_input = input().strip().lower()
            if user_input == "p" and pause_flag.is_set():
                pause_flag.clear()
                paused_time = 0
            elif user_input == "r" and not pause_flag.is_set():
                pause_flag.set()
            elif user_input == "q":
                quit_flag.set()  # Signal the threads to stop
                print("\nExiting timer...")
                return

    # Threads for the timer display and user input
    timer_thread = threading.Thread(target=display_timer, daemon=True)
    input_thread = threading.Thread(target=input_listener, daemon=True)

    timer_thread.start()
    input_thread.start()

    timer_thread.join()
    input_thread.join()

    # Clean exit
    if quit_flag.is_set():
        quit_flag.clear()  # Reset the quit flag for future calls
        print("\nTimer session ended.")
    return

    

# Main menu
def main_menu():
    global timer_data

    while True:
        print("\n--- Timer Menu ---")
        print("1. Start a Timer")
        print("2. View History")
        print("3. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("Starting timer...")
            timer()
        elif choice == "2":
            if not timer_data:
                print("No history available.")
            else:
                print("\n--- Timer History ---")
                for i, entry in enumerate(timer_data, 1):
                    print(f"{i}. Elapsed Time: {entry['elapsed_time']}, Paused Time: {entry['paused_time']}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu
if __name__ == "__main__":
    timer()