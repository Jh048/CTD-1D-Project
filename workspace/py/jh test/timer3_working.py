# import time
# import threading
# import sys

# def timer(*args):
#     if not args:
#         while True:
#             try:
#                 print("e.g. 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec")
#                 time_input = input("Enter countdown time (HH,MM,SS): ").strip()
#                 time_parts = list(map(int, time_input.split(',')))

#                 if len(time_parts) == 1:
#                     hours, minutes, seconds = 0, 0, time_parts[0]
#                 elif len(time_parts) == 2:
#                     hours, minutes, seconds = 0, time_parts[0], time_parts[1]
#                 elif len(time_parts) == 3:
#                     hours, minutes, seconds = time_parts
#                 else:
#                     print("Invalid input. Please enter time in the format HH,MM,SS.")
#                     continue

#                 if hours < 0 or minutes < 0 or seconds < 0 or minutes >= 60 or seconds >= 60:
#                     print("Invalid time format. Ensure hours, minutes, and seconds are correct.")
#                     continue

#                 break
#             except ValueError:
#                 print("Invalid input. Please enter time in the format HH,MM,SS.")
#     else:
#         if len(args) == 1:
#             hours, minutes, seconds = 0, 0, args[0]
#         elif len(args) == 2:
#             hours, minutes, seconds = 0, args[0], args[1]
#         elif len(args) == 3:
#             hours, minutes, seconds = args
#         else:
#             print("Invalid time format. Ensure time is in the format (hours, minutes, seconds).")
#             return

#     total_seconds = hours * 3600 + minutes * 60 + seconds
#     pause_flag = threading.Event()
#     pause_flag.set()

#     remaining_time = total_seconds
#     paused_time = 0
#     total_paused_time = 0  # Variable to track the total paused time

#     def display_timer():
#         nonlocal remaining_time, paused_time, total_paused_time
#         while remaining_time > 0:
#             if pause_flag.is_set():
#                 mins, secs = divmod(remaining_time, 60)
#                 hours, mins = divmod(mins, 60)

#                 print(f"\rRemaining time: {hours:02}:{mins:02}:{secs:02} | Press 'p' to pause: ", end="")
#                 # sys.stdout.write(f"\rRemaining time: {time_string} | Press 'p' to pause: ")
  
#                 time.sleep(1)
#                 remaining_time -= 1
#             else:
#                 total_paused_time += 1
#                 mins, secs = divmod(paused_time, 60)
#                 hours, mins = divmod(mins, 60)

#                 print(f"\rPause time: {hours:02}:{mins:02}:{secs:02} | Press 'r' to resume:", end="")
#                 time.sleep(1)
#                 paused_time += 1

#         # Handle final case to ensure output says 00:00 or 0:00 correctly
#         if remaining_time == 0:
#             sys.stdout.write("\033[K")
#             sys.stdout.write("\rRemaining time: 00:00 | Timer completed!    ")
#             sys.stdout.write("\n")
#             # Display total paused time
#             mins, secs = divmod(total_paused_time, 60)
#             hours, mins = divmod(mins, 60)
#             if hours > 0:
#                 paused_time_str = f"{hours:02}:{mins:02}:{secs:02}"  # HH:MM:SS
                
#             else:
#                 paused_time_str = f"{mins:02}:{secs:02}"  # MM:SS
#             print(f"Total paused time: {paused_time_str}")

#     def input_listener():
#         nonlocal paused_time
#         while remaining_time > 0:
#             user_input = input().strip().lower()
#             if user_input == "p" and pause_flag.is_set():
#                 pause_flag.clear()
#                 paused_time = 0
#             elif user_input == "r" and not pause_flag.is_set():
#                 pause_flag.set()
#             elif user_input == "q":
#                 remaining_time = 0
#                 print("\nTimer stopped.")
#                 break
                

#     timer_thread = threading.Thread(target=display_timer, daemon=True)
#     input_thread = threading.Thread(target=input_listener, daemon=True)

#     timer_thread.start()
#     input_thread.start()

#     timer_thread.join()
#     input_thread.join()

# # Test the timer function
# timer()

#========================================================================================

import time
import threading
import sys

def timer(*args):
    if not args:
        while True:
            try:
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
                    print("Invalid time format. Ensure hours, minutes, and seconds are correct.")
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
            print("Invalid time format. Ensure time is in the format (hours, minutes, seconds).")
            return

    total_seconds = hours * 3600 + minutes * 60 + seconds
    pause_flag = threading.Event()
    pause_flag.set()

    remaining_time = total_seconds
    paused_time = 0
    total_paused_time = 0  # Variable to track the total paused time

    def display_timer():
        nonlocal remaining_time, paused_time, total_paused_time
        while remaining_time > 0:
            if pause_flag.is_set():
                mins, secs = divmod(remaining_time, 60)
                hours, mins = divmod(mins, 60)

                print(f"\rRemaining time: {hours:02}:{mins:02}:{secs:02} | Press 'p' to pause: ", end="")
                # sys.stdout.write(f"\rRemaining time: {time_string} | Press 'p' to pause: ")
  
                time.sleep(1)
                remaining_time -= 1
            else:
                total_paused_time += 1
                mins, secs = divmod(paused_time, 60)
                hours, mins = divmod(mins, 60)

                print(f"\rPause time: {hours:02}:{mins:02}:{secs:02} | Press 'r' to resume:", end="")
                time.sleep(1)
                paused_time += 1

        # Handle final case to ensure output says 00:00 or 0:00 correctly
        if remaining_time == 0:
            sys.stdout.write("\033[K")
            sys.stdout.write("\rRemaining time: 00:00 | Timer completed!    ")
            sys.stdout.write("\n")
            # Display total paused time
            mins, secs = divmod(total_paused_time, 60)
            hours, mins = divmod(mins, 60)
            if hours > 0:
                paused_time_str = f"{hours:02}:{mins:02}:{secs:02}"  # HH:MM:SS
                
            else:
                paused_time_str = f"{mins:02}:{secs:02}"  # MM:SS
            print(f"Total paused time: {paused_time_str}")

    def input_listener():
        nonlocal paused_time
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

# Test the timer function
timer()