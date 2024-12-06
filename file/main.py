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
    menu4 = "1. Return to previous program\n2. Exit\n"

d = Data()

def retry(previous_function): 
    d.count += 1
    print()
    print("Invalid selection")
    print(d.menu4)
    sel = input("Please enter your choice: ")
    if sel == "1":
        previous_function() 
    elif sel == "2":
        pass
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
            end()
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
    print(menu_main)
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
        work_time = custom_timer_work()
        print()
        print("Set your rest duration:")
        rest_time = custom_timer_rest()
    

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

def input_formate():
    while True:
        try:
            print()
            print("e.g. 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec")
            time_input = input("Enter countdown time (HH,MM,SS): ").strip()
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

                print("e.g. 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec")
                print("Invalid input. Please enter time in the format HH,MM,SS.")
                # If the input is invalid, it prompts the user again.
                continue

            if hours < 0 or minutes < 0 or seconds < 0 or minutes >= 60 or seconds >= 60:
                # Minutes and seconds must be between 0 and 59.
                # No component can be negative.

                print("e.g. 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec")
                print("Invalid time format. Ensure hours, minutes, and seconds are within limit.")
                continue
            
            
        except ValueError:
            print("Invalid input. Please enter time in the format HH,MM,SS.")

#--------------------------------------------------------------------------------------------------------------------------

def custom_timer_work():
    while True:
        try:
            print("Enter work duration (HH,MM,SS):")
            time_input = input("e.g., 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec: ").strip()
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

def custom_timer_rest():
    while True:
        try:
            print("Enter rest duration (HH,MM,SS):")
            time_input = input("e.g., 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec: ").strip()
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


# def start_or_archive():
#     global title
#     Start_or_archieve = input('Do you want to start a timer?(y/n): ').lower()
#     if Start_or_archieve == 'y':
#         title = input ("Do you want to study,work or others?") .lower()
#         if title== "study":
#             #default timer for study
#             print (f'You have chosen {title}')
#         elif title == "work":
#             #default for study
#             print (f'You have chosen {title}')
#         elif title == "others":
#             other_activity= input ("What do you want to do today?") .lower()
#             #ask for duration function
#             print (f'You have chosen {other_activity}')
#         else:
#             print (invalid)
        
#         # print(f"working session: {title}")
        
#     elif title=='n':
#         Archieve= input ('Do you want to look at your history?(y/n): ').lower()
#         if Archieve == 'y':
#             print ('Loading History..........')
#             #Histroy function
#         elif Archieve == 'n':
#             print ('Bye! Have a great day!')
#         else:
#             print("incorrct input, please try again")
#     else:
#         print ('invalid')

if __name__ == "__main__":
    m3()
    # display_time_summary(total)
