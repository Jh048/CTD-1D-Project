import time
import threading
import sys
import copy

timer_data = []
user_input = None
quit_flag = threading.Event()  # Global quit flag to control exit

def timer(*args):
    global timer_data, user_input, quit_flag

    if not args:
        # If no arguments are passed, the function prompts the user to enter a countdown time in the format HH,MM,SS
        while True:
            try:
                print()
                print("e.g. 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec")
                time_input = input("Enter countdown time (HH,MM,SS): ").strip()
                time_parts = list(map(int, time_input.split(',')))

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
                    print("Invalid time format. Ensure hours, minutes, and seconds are within limit.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter time in the format HH,MM,SS.")
    else:
        if len(args) == 1:
            hours, minutes, seconds = 0, 0, args[0]
        elif len(args) == 2:
            hours, minutes, seconds = 0, args[0], args[1]
        elif len(args) == 3:
            hours, minutes, seconds = args
        else:
            print("Invalid time format.")
            return

    total_seconds = hours * 3600 + minutes * 60 + seconds
    original_total_time = copy.deepcopy(total_seconds)

    pause_flag = threading.Event()  # threading.Event is used for pause and resume the timer.
    pause_flag.set()  # Initializes the flag as active (running state).
    remaining_time = total_seconds  # Tracks the countdown’s remaining seconds.
    paused_time = 0  # Tracks how long the timer has been paused in the current pause session.

    def display_timer():
        nonlocal remaining_time, paused_time
        while remaining_time > 0:
            if quit_flag.is_set():  # If quit flag is set, break out of the loop
                break
            if pause_flag.is_set():
                mins, secs = divmod(remaining_time, 60)
                hours, mins = divmod(mins, 60)
                print(f"\rRemaining time: {hours:02}:{mins:02}:{secs:02} | Press 'p' to pause: ", end="")
                time.sleep(1)
                remaining_time -= 1
            else:
                mins, secs = divmod(paused_time, 60)
                hours, mins = divmod(mins, 60)
                print(f"\rPause time: {hours:02}:{mins:02}:{secs:02} | Press 'r' to resume:", end="")
                paused_time += 1
                time.sleep(1)

        if remaining_time == 0:
            sys.stdout.write("\033[K")
            sys.stdout.write("\rRemaining time: 00:00:00 | Timer completed!    ")
            sys.stdout.write("\n")

            mins, secs = divmod(paused_time, 60)
            hours, mins = divmod(mins, 60)
            paused_time_str = f"{hours:02}:{mins:02}:{secs:02}" if hours > 0 else f"{mins:02}:{secs:02}"
            elapsed_time = original_total_time - remaining_time
            elapsed_mins, elapsed_secs = divmod(elapsed_time, 60)
            elapsed_hours, elapsed_mins = divmod(elapsed_mins, 60)
            elapsed_time_str = f"{elapsed_hours:02}:{elapsed_mins:02}:{elapsed_secs:02}" if hours > 0 else f"{mins:02}:{secs:02}"

            timer_data.append({
                "elapsed_time": elapsed_time_str,
                "paused_time": paused_time_str
            })

    def input_listener():
        nonlocal remaining_time, paused_time
        while remaining_time > 0:
            user_input = input().strip().lower()
            if user_input == "p" and pause_flag.is_set():
                pause_flag.clear()
                paused_time = 0
            elif user_input == "r" and not pause_flag.is_set():
                pause_flag.set()
            elif user_input == "q":
                quit_flag.set()  # Set quit flag to stop both threads
                sys.stdout.write("\033[K")
                sys.stdout.write(f"\rTimer stopped. Exiting...    ")
                sys.stdout.write("\n")
                break

    timer_thread = threading.Thread(target=display_timer, daemon=True)
    input_thread = threading.Thread(target=input_listener, daemon=True)

    timer_thread.start()
    input_thread.start()

    timer_thread.join()
    input_thread.join()
    print(timer_data)

timer()  # Start the timer