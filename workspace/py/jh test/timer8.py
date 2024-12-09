# Define a global list to store the timer details
timer_data = []  # Each entry will be a tuple of (total_time_used, paused_time_str)

def timer(*args):
    # The timer function (rest of the implementation remains the same)
    global timer_data  # Ensure access to the global list
    
    # Parse input time (HH,MM,SS) and calculate total_seconds (existing logic)

    total_seconds = hours * 3600 + minutes * 60 + seconds  # Converts the time into total seconds
    original_total_time = total_seconds  # Store the original total time for tracking

    # Initialize variables (existing logic)
    pause_flag = threading.Event()
    pause_flag.set()
    remaining_time = total_seconds
    paused_time = 0
    total_paused_time = 0

    # Display timer logic (existing)
    def display_timer():
        nonlocal remaining_time, paused_time, total_paused_time
        while remaining_time > 0:
            if pause_flag.is_set():
                mins, secs = divmod(remaining_time, 60)
                hours, mins = divmod(mins, 60)
                print(f"\rRemaining time: {hours:02}:{mins:02}:{secs:02} | Press 'p' to pause: ", end="")
                time.sleep(1)
                remaining_time -= 1
            else:
                total_paused_time += 1
                mins, secs = divmod(paused_time, 60)
                hours, mins = divmod(mins, 60)
                print(f"\rPause time: {hours:02}:{mins:02}:{secs:02} | Press 'r' to resume:", end="")
                time.sleep(1)
                paused_time += 1

        if remaining_time == 0:
            sys.stdout.write("\033[K")
            sys.stdout.write("\rRemaining time: 00:00:00 | Timer completed!    \n")

            # Calculate the paused time and elapsed time
            mins, secs = divmod(total_paused_time, 60)
            hours, mins = divmod(mins, 60)
            paused_time_str = f"{hours:02}:{mins:02}:{secs:02}" if hours > 0 else f"{mins:02}:{secs:02}"

            elapsed_time = original_total_time - remaining_time
            elapsed_mins, elapsed_secs = divmod(elapsed_time, 60)
            elapsed_hours, elapsed_mins = divmod(elapsed_mins, 60)
            elapsed_time_str = f"{elapsed_hours:02}:{elapsed_mins:02}:{elapsed_secs:02}"

            # Print paused time
            print(f"Total paused time: {paused_time_str}")
            print(f"Total elapsed time: {elapsed_time_str}")

            # Store details in the global list
            timer_data.append((elapsed_time_str, paused_time_str))
            return paused_time_str

    # Input listener logic (existing)
    def input_listener():
        nonlocal remaining_time, paused_time
        while remaining_time > 0:
            user_input = input().strip().lower()
            if user_input == "p" and pause_flag.is_set():  # Pause the timer
                pause_flag.clear()
                paused_time = 0
            elif user_input == "r" and not pause_flag.is_set():  # Resume the timer
                pause_flag.set()
            elif user_input == "q":  # Stop the timer
                mins, secs = divmod(remaining_time, 60)
                hours, mins = divmod(mins, 60)
                print(f"\nTimer stopped at: {hours:02}:{mins:02}:{secs:02}")
                remaining_time = 0
                
                # Calculate the paused time and elapsed time
                mins, secs = divmod(total_paused_time, 60)
                hours, mins = divmod(mins, 60)
                paused_time_str = f"{hours:02}:{mins:02}:{secs:02}" if hours > 0 else f"{mins:02}:{secs:02}"

                elapsed_time = original_total_time - remaining_time
                elapsed_mins, elapsed_secs = divmod(elapsed_time, 60)
                elapsed_hours, elapsed_mins = divmod(elapsed_mins, 60)
                elapsed_time_str = f"{elapsed_hours:02}:{elapsed_mins:02}:{elapsed_secs:02}"

                # Print paused time
                print(f"Total paused time: {paused_time_str}")
                print(f"Total elapsed time: {elapsed_time_str}")

                # Store details in the global list
                timer_data.append((elapsed_time_str, paused_time_str))
                time.sleep(1)
                sys.exit()

    # Create and start threads (existing)
    timer_thread = threading.Thread(target=display_timer, daemon=True)
    input_thread = threading.Thread(target=input_listener, daemon=True)
    timer_thread.start()
    input_thread.start()
    timer_thread.join()
    input_thread.join()