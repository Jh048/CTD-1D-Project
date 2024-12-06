from menu import *
from timerA import *
import sys



#==========================================================================================================================

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

def ask_cont(name= None, *b):
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
        print(menu4)
        sel = input("Please enter your choice: ")
        if sel == "1":
            total = calculate_total_times(archive_dict)
            print(total)
            display_time_summary(total)
            return
        elif sel == "2":
            exit_option()
        else:
            retry(history)


#==========================================================================================================================
                
def end():
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


# def m1():
#     print(menu1)
#     sel = input("Please enter your choice: ")
#     if sel == "1":
#         m2()
#     elif sel == "2":
#         history()
#     else:
#         retry(m1)



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
            ask_cont(title, m2_1)
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
                    return
            else:
                print("Work session was interrupted.")
                exit_option()
                return
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
