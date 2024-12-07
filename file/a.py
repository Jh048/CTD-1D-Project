import time # Used to manage delays and countdown timing in seconds.
import threading # Enables concurrent execution of code (to run the timer and handle user inputs simultaneously).
import sys # Used to manipulate the output in the terminal for updating countdown visuals.
import copy
from menu import *
from datetime import timedelta



timer_data = []
user_input = None
quit_flag = threading.Event()  # Global quit flag to control exit
elapsed_time = 0
archive_dict = {}
title = None
user_input = ""
time_up = False



def secs_to_clock(sec):
    mins, secs = divmod(sec, 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02}:{mins:02}:{secs:02}"


#=========================================================================================================


def timer(*args,title =None):

# The timer function accepts an optional set of arguments representing the time in hours, minutes, and seconds.
    global timer_data, user_input, quit_flag, elapsed_time, user_input, time_up
    time_up = False
    quit_flag.clear()
    if not args:
    # If no arguments are passed, the function prompts the user to enter a countdown time in the format HH,MM,SS

        while True:
            try:
                print()
                print(f"Working session: {title}")
                menu6(title)
                time_input = input("Enter countdown time (HH,MM,SS): ").strip()
                print()
                print(f"Working session: {title}")
                # time_input.strip() removes leading/trailing spaces.

                time_parts = list(map(int, time_input.split(',')))
                # time_input.split(',') splits the input string into components (e.g., “1,0,30” → [1, 0, 30]).
                # list(map(int, ...)) converts each part into an integer.

                if len(time_parts) == 1:
                    hours, minutes, seconds = 0, 0, time_parts[0] # Interpreted as seconds.
                elif len(time_parts) == 2:
                    hours, minutes, seconds = 0, time_parts[0], time_parts[1] # Interpreted as minutes and seconds.
                elif len(time_parts) == 3:
                    hours, minutes, seconds = time_parts # Interpreted as hours, minutes, and seconds.
                else:
                    print("Invalid input. Please enter time in the format HH,MM,SS.")
                    retry(timer)
                    # If the input is invalid, it prompts the user again.
                    continue

                if hours < 0 or minutes < 0 or seconds < 0 or minutes >= 60 or seconds >= 60:
                    # Minutes and seconds must be between 0 and 59.
                    # No component can be negative.

                    print(menu6)
                    print("Invalid time format. Ensure hours, minutes, and seconds are within limit.")
                    continue

                break
            except ValueError:
                print("Invalid input. Please enter time in the format HH,MM,SS.")
    else:
        # If arguments are passed directly (args), the function parses them similarly to user input.

        if len(args) == 1:
            hours, minutes, seconds = 0, 0, args[0]
        elif len(args) == 2:
            hours, minutes, seconds = 0, args[0], args[1]
        elif len(args) == 3:
            hours, minutes, seconds = args
        else:
            print("Invalid input. Please enter time in the format HH,MM,SS.")
            retry(timer)
            return 
    total_seconds = hours * 3600 + minutes * 60 + seconds
    # Converts the time into total seconds for easier countdown calculation.
    original_total_time = copy.deepcopy(total_seconds)

    pause_flag = threading.Event() # threading.Event is used for pause and resume the timer.
    pause_flag.set() # Initializes the flag as active (running state).
    remaining_time = total_seconds #Tracks the countdown’s remaining seconds.
    paused_time = 0 # Tracks how long the timer has been paused in the current pause session.
    total_pause_time_list = []

    pause_count = 0
    resume_count = 0

    def display_timer():
        
        global time_up
        nonlocal remaining_time, paused_time, pause_count, resume_count, original_total_time, total_pause_time_list
        while remaining_time > 0:
            if quit_flag.is_set():  # If quit flag is set, break out of the loop
                break
            if pause_flag.is_set(): 
                print(f"\rRemaining time: {secs_to_clock(remaining_time)} | Press 'p' to pause, Press 'q' to quit: ", end="")
                time.sleep(1)
                remaining_time -= 1
            else:
                print(f"\rPause time: {secs_to_clock(paused_time)} | Press 'r' to resume, Press 'q' to quit:", end="")
                paused_time += 1
                time.sleep(1)

        if remaining_time == 0:  # When timer completes
            time_up = True
            sys.stdout.write("\033[K")
            sys.stdout.write("\rRemaining time: 00:00:00 | Timer completed!                           ")
            sys.stdout.write("\n")


            # Calculate total pause time
            total_pause_time = sum(total_pause_time_list) - pause_count
            paused_time_str = f"{secs_to_clock(total_pause_time)}"
            
            elapsed_time = original_total_time - remaining_time
            elapsed_time_str = f"{secs_to_clock(elapsed_time)}"


            # Store details in the global list
            key_name = str(title or "No Title")
            if key_name not in archive_dict:
                archive_dict[key_name] = []
            archive_dict[key_name].append({
                "Elapsed_time": elapsed_time_str,
                "Total_paused_time": paused_time_str})
            # Display summary
            print("\nTimer Summary:")
            print(f"Elapsed Time: {elapsed_time_str}")
            print(f"Total Pause Time: {paused_time_str}")
            # Trigger quit flag to terminate `input_listener`
            print("Press enter to continue.")
            
            quit_flag.set()


    def input_listener():
        global time_up
        nonlocal remaining_time, paused_time, pause_count, resume_count, total_pause_time_list

        while not quit_flag.is_set():  # Continues running unless quit_flag is set
            try:
                user_input = input().strip().lower()

                if user_input == "p" and pause_flag.is_set():  # Pause the timer
                    pause_flag.clear()
                    paused_time = 0  # Reset pause time tracker for the new pause session
                    pause_count += 1

                elif user_input == "r" and not pause_flag.is_set():  # Resume the timer
                    pause_flag.set()

                    total_pause_time_list.append(paused_time)  # Add the paused time to the list
                    resume_count += 1
                elif user_input == "q":  # Quit the timer
                    

                    # Add the current paused time to the total pause list

                    total_pause_time_list.append(paused_time)

                    # Calculate total pause time
                    total_pause_time = sum(total_pause_time_list) - pause_count

                    # Calculate elapsed time
                    elapsed_time = original_total_time - remaining_time

                    # Format total paused time string
                    paused_time_str = f"{secs_to_clock(total_pause_time)}"
                    elapsed_time_str = f"{secs_to_clock(elapsed_time)}"

                    key_name = str(title or "No Title")
                    if key_name not in archive_dict:
                        archive_dict[key_name] = []
                    archive_dict[key_name].append({
                        "Elapsed_time": elapsed_time_str,
                        "Total_paused_time": paused_time_str})


                    # Display summary
                    print("\nTimer Summary:")
                    print(f"Elapsed Time: {elapsed_time_str}")
                    print(f"Total Pause Time: {paused_time_str}")
                    quit_flag.set()  # Set the quit flag to stop both threads
                    time_up = False
                
                    exit_option()

            except EOFError:
                # Handle input interruptions
                quit_flag.set()
                break 
    
    timer_thread = threading.Thread(target=display_timer, daemon=True)
    # Displays the countdown.
    input_thread = threading.Thread(target=input_listener, daemon=True)
    # Listens for user input.

    # Threads are started using .start() and synchronized with .join().
    timer_thread.start()
    input_thread.start()

    timer_thread.join()
    input_thread.join()
    return time_up




#===================================================================================================

def calculate_total_times(archive_dict):
    def time_string_to_seconds(time_str):
        hours, minutes, seconds = map(int, time_str.split(':'))
        return timedelta(hours=hours, minutes=minutes, seconds=seconds).total_seconds()

    def seconds_to_time_string(seconds):
        return str(timedelta(seconds=seconds))

    total_times = {}

    for key_name, activities in archive_dict.items():
        total_elapsed = 0
        total_paused = 0
        
        for activity in activities:
            total_elapsed += time_string_to_seconds(activity['Elapsed_time'])
            total_paused += time_string_to_seconds(activity['Total_paused_time'])
        
        total_elapsed_time_str = seconds_to_time_string(total_elapsed)
        total_paused_time_str = seconds_to_time_string(total_paused)
        
        total_times[key_name] = {
            'Elapsed_time': total_elapsed_time_str,  # Match key names
            'Paused_time': total_paused_time_str    # Match key names
        }

    return total_times
total = calculate_total_times(archive_dict)



def display_time_summary(total):
    print("\nActivity-wise Breakdown:\n")
    for activity, time_data in total.items():
        print(f"Activity: {activity}")
        print(f"  Total Elapsed Time: {time_data['Elapsed_time']}")
        print(f"  Total Paused Time: {time_data['Paused_time']}\n")
    
    total_elapsed_time = sum(
        [convert_to_seconds(t['Elapsed_time']) for t in total.values()]
    )
    total_paused_time = sum(
        [convert_to_seconds(t['Paused_time']) for t in total.values()]
    )
    print("Total Time Across All Activities:")
    print(f"Total Elapsed Time: {convert_to_hms(total_elapsed_time)}")
    print(f"Total Paused Time: {convert_to_hms(total_paused_time)}\n")    

def convert_to_seconds(hms):
    try:
        if "day" in hms:  # Handle strings like '-1 day, 23:59:59'
            days, time = hms.split(", ")
            days = int(days.split()[0])  # Extract the numeric part of days
            h, m, s = map(int, time.split(":"))
            total_seconds = days * 86400 + h * 3600 + m * 60 + s
        else:
            h, m, s = map(int, hms.split(":"))
            total_seconds = h * 3600 + m * 60 + s
        return max(0, total_seconds)  # Ensure non-negative result
    except ValueError as e:
        print(f"Error in convert_to_seconds: {e}")
        return 0

def convert_to_hms(seconds):
    """
    Convert seconds into HH:MM:SS format.
    
    Args:
        seconds (int): Total time in seconds.
        
    Returns:
        str: Time in HH:MM:SS format.
    """
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02}:{m:02}:{s:02}"


# def convert_to_hms(seconds):
#     """
#     Convert seconds into HH:MM:SS format.
    
#     Args:
#         seconds (int): Total time in seconds.
        
#     Returns:
#         str: Time in HH:MM:SS format.
#     """
#     h = seconds // 3600
#     m = (seconds % 3600) // 60
#     s = seconds % 60
#     return f"{h:02}:{m:02}:{s:02}"

#===================================================================================================

def reset_timer_flag():
    global quit_flag
    quit_flag.clear()

#==========================================================================================================================

def reset_history():
    global archive_dict
    archive_dict = {}  # Reset archive_dict to an empty dictionary

#==========================================================================================================================

class Data:
    count = 0
    limit = 3
d = Data()

def retry(previous_function): 
    d.count += 1
    print()
    print(menu10)
    sel = input("Please enter your choice: ")
    if sel == "1":
        previous_function() 
    elif sel == "2":
        exit_option()
    elif d.count >= d.limit:
            d.count = 0
            print()
            print("Exiting the system due to multiple unsuccessful attempts ")
            sys.exit()
    else:
        retry(previous_function)
#==========================================================================================================================

def ask_cont(name= None, b = None):
    cont_menu(name)
    sel = input("Please enter your choice: ")
    if sel == "1":
        b()
    elif sel == "2":
        exit_option()
    else:
        retry(ask_cont)


#==========================================================================================================================

def history():
        total = calculate_total_times(archive_dict)
        display_time_summary(total)
        sel = input("Press enter to continue ")
        exit_option()



#==========================================================================================================================
                
def end():
    reset_history()
    print()
    print("Goodbye and Thank you for using the system")
    sys.exit()


#==========================================================================================================================


def exit_option():
    print(menu9)
    sel = input("Please enter your choice: ")
    if sel == "1":
        m()
    elif sel == "2":
        history()
    elif sel == "3":
        end()
    else:
        retry(exit_option)


#==========================================================================================================================


def m():
    print(menu1)
    sel = input("Please enter your choice: ")
    if sel == "1":
        m2()
    elif sel == "2":
        history()
    elif sel == "3":
        end()
    else:
        retry(m)


#==========================================================================================================================



def m2():
    """                    
--------------------------
What do you want to do?
1) study 
2) work
3) others
--------------------------
    """
    print(menu2)
    sel = input("Please enter your choice: ")
 
    if sel == "1":
        m2_1()
    elif sel == "2":
        m2_2()
    elif sel == "3":
        m3()
    else:
        retry(m2)

def m2_1():
    time_up = timer(25,0 ,title ="study")  # Unpack the time tuple and pass it to the timer

    # Check if time_up is False (i.e., the timer did not finish or was interrupted)
    if time_up:
        print("Time's up!")
        print("Starting rest session...")
        reset_timer_flag()
        
        time_up = timer(5,0, title = "study_break")  # Unpack the time tuple and pass it to the timer
        if time_up:
            print("Rest session completed.")
            pass
        else:
            print("Rest session was interrupted.")
            return
    else:
        print("Work session was interrupted.")
        return

    

def m2_2():
    time_up = timer(45,0 ,title ="work")  # Unpack the time tuple and pass it to the timer

    # Check if time_up is False (i.e., the timer did not finish or was interrupted)
    if time_up:
        print("Time's up!")
        print("Starting rest session...")
        reset_timer_flag()
        
        time_up = timer(15,0, title = "work_break")  # Unpack the time tuple and pass it to the timer
        if time_up:
            print("Rest session completed.")
            ask_cont(title, m2_1)
        else:
            print("Rest session was interrupted.")
            return
    else:
        print("Work session was interrupted.")
        return


#==========================================================================================================================


def m3():
    """                    
    --------------------------
    "What do you want to do today?"
    cooking, meditation, etc
    --------------------------
    """
    print(menu3)
    sel = input("Please enter your activity: ").strip()
    
    def m3_1():
        # Get work and rest durations
        print("Set your work duration:")
        work_time = custom_timer_work(sel)
        print()
        print("Set your rest duration:")
        rest_time = custom_timer_rest(sel)
        def edit_change(sel):
            option_m3(sel)
            sel1 = input("Please enter your choice: ") 
            if sel1 == '1':
                pass
            elif sel1 == "2":
                m3_1()
            elif sel1 == "3":
                m3()
            else:
                retry(edit_change(sel))
        edit_change(sel)

    

        def m3_2():
            global time_up
            # Pass durations to the timer
            print(f"Starting work session: {sel}")
            # reset_timer_flag()
            time_up = timer(*work_time, title=sel)  # Unpack the time tuple and pass it to the timer

            # Check if time_up is False (i.e., the timer did not finish or was interrupted)
            if time_up:
                print(f"Time's up for {sel}")
                print("Starting rest session...")
                reset_timer_flag()
                
                time_up = timer(*rest_time, title=f"{sel}_break")  # Unpack the time tuple and pass it to the timer
                if time_up:
                    print("Rest session completed.")
                    ask_cont(sel,m3_2)
                else:
                    print("Rest session was interrupted.")
                    exit_option()
                    
            else:
                print("Work session was interrupted.")
                exit_option()
                
        m3_2()
    m3_1()
    

#--------------------------------------------------------------------------------------------------------------------------

def input_formate(title=None):
    while True:
        try:
            print()
            menu6(title)
            time_input = input("Please enter your choice: ").strip()
            print()

            # time_input.strip() removes leading/trailing spaces.

            time_parts = list(map(int, time_input.split(',')))
            # time_input.split(',') splits the input string into components (e.g., “1,0,30” → [1, 0, 30]).
            # list(map(int, ...)) converts each part into an integer.

            if len(time_parts) == 1:
                hours, minutes, seconds = 0, 0, time_parts[0] # Interpreted as seconds.
            elif len(time_parts) == 2:
                hours, minutes, seconds = 0, time_parts[0], time_parts[1] # Interpreted as minutes and seconds.
            elif len(time_parts) == 3:
                hours, minutes, seconds = time_parts # Interpreted as hours, minutes, and seconds.
            else:

                menu6(title)
                print("Invalid input. Please enter time in the format HH,MM,SS.")
                # If the input is invalid, it prompts the user again.
                continue

            if hours < 0 or minutes < 0 or seconds < 0 or minutes >= 60 or seconds >= 60:
                # Minutes and seconds must be between 0 and 59.
                # No component can be negative.

                menu6(title)
                print("Invalid time format. Ensure hours, minutes, and seconds are within limit.")
                continue
            
            
        except ValueError:
            print("Invalid input. Please enter time in the format HH,MM,SS.")

#--------------------------------------------------------------------------------------------------------------------------

def custom_timer_work(sel):
    while True:
        try:
            menu6(sel)
            time_input = input("Please enter your working time: ").strip()
            time_parts = list(map(int, time_input.split(',')))
            if len(time_parts) == 1:
                return 0, 0, time_parts[0]  # Seconds only
            elif len(time_parts) == 2:
                return 0, time_parts[0], time_parts[1]  # Minutes and seconds
            elif len(time_parts) == 3:
                return time_parts  # Hours, minutes, seconds
            else:
                print("Invalid input format. Please enter time in HH,MM,SS format.")
                
        except ValueError:
            print("Invalid input. Please enter time in HH,MM,SS format.")

#--------------------------------------------------------------------------------------------------------------------------

def custom_timer_rest(sel):
    while True:
        try:
            menu6(sel)
            time_input = input("Please enter your resting time: ").strip()
            time_parts = list(map(int, time_input.split(',')))
            if len(time_parts) == 1:
                return 0, 0, time_parts[0]  # Seconds only
            elif len(time_parts) == 2:
                return 0, time_parts[0], time_parts[1]  # Minutes and seconds
            elif len(time_parts) == 3:
                return time_parts  # Hours, minutes, seconds
            else:
                print("Invalid input format. Please enter time in HH,MM,SS format.")
        except ValueError:
            print("Invalid input. Please enter time in HH,MM,SS format.")


#==========================================================================================================================


if __name__ == "__main__":
    m()
    # display_time_summary(total)


