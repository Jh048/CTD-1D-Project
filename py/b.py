import time
import sys
import threading

def timer(minutes):
    seconds = minutes * 60  # Convert minutes to seconds
    pause_flag = threading.Event()  # Event to manage pause and resume
    pause_flag.set()  # Initially, the countdown is not paused

    # Shared variable for displaying the current message
    prompt_message = ["Enter 'p' to pause: "]

    # Shared variable for the current time string
    time_string = "00:00"

    def input_listener():  # Thread to listen for user input
        nonlocal pause_flag
        while True:
            # Show the updated message and wait for input
            user_input = input(f"\rRemaining time: {time_string} | {prompt_message[0]}").strip().lower()
            if user_input == 'p' and pause_flag.is_set():
                pause_flag.clear()  # Pause the countdown
                prompt_message[0] = "Enter 'r' to resume: "
            elif user_input == 'r' and not pause_flag.is_set():
                pause_flag.set()  # Resume the countdown
                prompt_message[0] = "Enter 'p' to pause: "
 

    # Start the input listener thread
    listener_thread = threading.Thread(target=input_listener, daemon=True)
    listener_thread.start()

    # # Timer countdown logic
    # for remaining in range(seconds, 0, -1):  # Loop time backwards to 0
    #     pause_flag.wait()  # Pause the countdown if needed
    #     mins = (remaining % 3600) // 60  # Convert seconds to minutes
    #     secs = remaining % 60
    #     time_string = f"{mins:02}:{secs:02}"  # Format time as MM:SS

    #     # Update the timer and prompt message on the same line
    #     sys.stdout.write(f"\rRemaining time: {time_string} | {prompt_message[0]}")
    #     sys.stdout.flush()
    #     time.sleep(1)  # Wait for 1 second between each update

    # for remaining in range(0,seconds):  # Loop time backwards to 0
    #     pause_flag.wait()  # Pause the countdown if needed
    #     mins = (remaining % 3600) // 60  # Convert seconds to minutes
    #     secs = remaining % 60
    #     time_string = f"{mins:02}:{secs:02}"  # Format time as MM:SS

    #     # Update the timer and prompt message on the same line
    #     sys.stdout.write(f"\rPause time: {time_string} | {prompt_message[0]}")
    #     sys.stdout.flush()
    #     time.sleep(1)  # Wait for 1 second between each update

    sys.stdout.write("\rCountdown: Time's up!          \n")