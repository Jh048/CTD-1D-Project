# # import time
# # import sys
# # import threading

# # def timer(minutes):
# #     seconds = minutes * 60  # Convert minutes to seconds
# #     pause_flag = threading.Event()  # Event to manage pause and resume
# #     pause_flag.set()  # Initially, the countdown is not paused

# #     def input_listener():  # Thread to listen for user input
# #         nonlocal pause_flag
# #         while True:
# #             user_input = input().strip().lower()
# #             if user_input == 'p':
# #                 pause_flag.clear()  # Pause the countdown
# #                 a = "\nPress 'r' to resume: ", end='', flush=True
# #                 return a
# #             elif user_input == 'r':
# #                 pause_flag.set()  # Resume the countdown
# #                 a = "\nPress 'p' to pause: ", end='', flush=True
# #                 return a


# #     # Start the input listener thread
# #     listener_thread = threading.Thread(target=input_listener, daemon=True)
# #     listener_thread.start()

# #     # Display initial instruction
# #     print(a)

# #     for remaining in range(seconds, 0, -1):  # Loop time backwards to 0
# #         pause_flag.wait()  # Wait here if paused
# #         mins = (remaining % 3600) // 60  # Convert seconds to minutes
# #         secs = remaining % 60
# #         time_string = f"{mins:02}:{secs:02}"  # Format time as MM:SS

# #         # Update the timer display
# #         sys.stdout.write(f"\rRemaining time: {time_string}   ")
# #         sys.stdout.flush()
# #         time.sleep(1)  # Wait for 1 second between each update

# #     sys.stdout.write("\rCountdown: Time's up!          \n")

# # # Example usage
# # timer(1)  # Example with 1 minute

# =======================================================================================


# import time
# import sys
# import threading

# def timer(minutes):
#     seconds = minutes * 60  # Convert minutes to seconds
#     pause_flag = threading.Event()  # Event to manage pause and resume
#     pause_flag.set()  # Initially, the countdown is not paused

#     # Shared variable for displaying the current message
#     prompt_message = ["Press 'p' to pause: "]

#     def input_listener():  # Thread to listen for user input
#         nonlocal pause_flag
#         while True:
#             user_input = input().strip().lower()
#             if user_input == 'p':
#                 pause_flag.clear()  # Pause the countdown
#                 prompt_message[0] = "Press 'r' to resume: "
#             elif user_input == 'r':
#                 pause_flag.set()  # Resume the countdown
#                 prompt_message[0] = "Press 'p' to pause: "

#     # Start the input listener thread
#     listener_thread = threading.Thread(target=input_listener, daemon=True)
#     listener_thread.start()

#     # Timer countdown logic
#     for remaining in range(seconds, 0, -1):  # Loop time backwards to 0
#         pause_flag.wait()  # Wait here if paused
#         mins = (remaining % 3600) // 60  # Convert seconds to minutes
#         secs = remaining % 60
#         time_string = f"{mins:02}:{secs:02}"  # Format time as MM:SS

#         # Update the timer and prompt message on separate lines
#         sys.stdout.write(f"\rRemaining time: {time_string} | {prompt_message[0]}")
#         sys.stdout.flush()
#         time.sleep(1)  # Wait for 1 second between each update

#     sys.stdout.write("\rCountdown: Time's up!          \n")

# # Example usage
# timer(1)  # Example with 1 minute
# =======================================================================================

## working####################################
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

    # Timer countdown logic
    for remaining in range(seconds, 0, -1):  # Loop time backwards to 0
        pause_flag.wait()  # Pause the countdown if needed
        mins = (remaining % 3600) // 60  # Convert seconds to minutes
        secs = remaining % 60
        time_string = f"{mins:02}:{secs:02}"  # Format time as MM:SS

        # Update the timer and prompt message on the same line
        sys.stdout.write(f"\rRemaining time: {time_string} | {prompt_message[0]}")
        sys.stdout.flush()
        time.sleep(1)  # Wait for 1 second between each update

    for remaining in range(0,seconds):  # Loop time backwards to 0
        pause_flag.wait()  # Pause the countdown if needed
        mins = (remaining % 3600) // 60  # Convert seconds to minutes
        secs = remaining % 60
        time_string = f"{mins:02}:{secs:02}"  # Format time as MM:SS

        # Update the timer and prompt message on the same line
        sys.stdout.write(f"\rPause time: {time_string} | {prompt_message[0]}")
        sys.stdout.flush()
        time.sleep(1)  # Wait for 1 second between each update

    sys.stdout.write("\rCountdown: Time's up!          \n")

# Example usage
timer(1)  # Example with 1 minute
# =======================================================================================
# import time
# import sys
# import threading
# import queue

# def timer(minutes):
#     seconds = minutes * 60  # Convert minutes to seconds
#     pause_flag = threading.Event()  # Event to manage pause and resume
#     pause_flag.set()  # Initially, the countdown is not paused

#     # Shared variable for the current message
#     prompt_message = ["Press 'p' to pause: "]

#     # Queue for handling user input
#     input_queue = queue.Queue()

#     # Track pause time
#     total_pause_time = 0
#     pause_start = None

#     def input_listener():  # Thread to listen for user input
#         while True:
#             user_input = input().strip().lower()
#             input_queue.put(user_input)

#     # Start the input listener thread
#     listener_thread = threading.Thread(target=input_listener, daemon=True)
#     listener_thread.start()

#     # Timer countdown logic
#     for remaining in range(seconds, 0, -1):
#         if not input_queue.empty():
#             user_input = input_queue.get()
#             if user_input == 'p' and pause_flag.is_set():
#                 pause_flag.clear()  # Pause the countdown
#                 prompt_message[0] = "Press 'r' to resume: "
#                 pause_start = time.time()  # Start tracking pause time
#                 sys.stdout.write(f"\nTime pause:       00:00 | {prompt_message[0]}")
#                 sys.stdout.flush()
#             elif user_input == 'r' and not pause_flag.is_set():
#                 pause_flag.set()  # Resume the countdown
#                 if pause_start is not None:
#                     pause_duration = time.time() - pause_start
#                     total_pause_time += pause_duration
#                     pause_start = None
#                     mins, secs = divmod(int(total_pause_time), 60)
#                     sys.stdout.write(f"\rTime pause:       {mins:02}:{secs:02} | ")
#                     prompt_message[0] = "Press 'p' to pause: "

#         pause_flag.wait()  # Pause the countdown if needed

#         mins = (remaining % 3600) // 60  # Convert seconds to minutes
#         secs = remaining % 60
#         time_string = f"{mins:02}:{secs:02}"  # Format time as MM:SS

#         # Update the timer and prompt message on the same line
#         sys.stdout.write(f"\rRemaining time:  {time_string} | {prompt_message[0]}")
#         sys.stdout.flush()
#         time.sleep(1)  # Wait for 1 second between each update

#     sys.stdout.write("\nCountdown: Time's up!\n")

# # Example usage
# timer(1)  # Example with 1 minute
# =======================================================================================
