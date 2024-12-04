from menu import *
from timerA import *


# loop = True
# while loop:
#     print("Welcome to Pomodoro timer!!!")
#     print(menu2)
#     sel = input("Please enter your choice: ")


    # print("e.g. 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec")
    # time_input = input("Enter countdown time (HH,MM,SS): ").strip()
    # print()
    # print(f"Working session: {title}")
    # # time_input.strip() removes leading/trailing spaces.

    # time_parts = list(map(int, time_input.split(',')))
def reset_timer_flag():
    global quit_flag
    quit_flag.clear()

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

def m3():
    """                    
    --------------------------
    "What do you want to do today?"
    cooking, meditation, etc
    --------------------------
    """

    print(menu3)
    sel = input("Please enter your activity (e.g., 'study', 'work', 'others'): ").strip()


    # Get work and rest durations
    print("Set your work duration:")
    work_time = custom_timer_work()
    print()
    
    print("Set your rest duration:")
    rest_time = custom_timer_rest()

    def m3_1():
        global time_up

        # Pass durations to the timer
        print(f"Starting work session: {sel}")
        reset_timer_flag()
        time_up = timer(*work_time, title=sel)  # Unpack the time tuple and pass it to the timer

        # Check if time_up is False (i.e., the timer did not finish or was interrupted)
        if time_up:
            print("Time's up for work!")
            print("Starting rest session...")
            reset_timer_flag()
            
            time_up = timer(*rest_time, title=f"{sel}_break")  # Unpack the time tuple and pass it to the timer
            if time_up:
                print("Rest session completed.")
                rm3_1()
            else:
                print("Rest session was interrupted.")
                return
        else:
            print("Work session was interrupted.")
            return
    

    def rm3_1():
        input1 = input("Do you want to continue the timer?")
        if input1 == "1":
            m3_1()
        elif input1 == "2":
            print(timer_data)
            rm3()

 
            return
        else:
            print("invalid input, please try again.")
            rm3_1()

    m3_1()

def rm3():
    sel = input("1: m3,2:quit:")
    if sel =="1":
        m3()
    elif sel == "2":
        return
    else:
        print("wrong input, try again")
        rm3()
    

def m2():
    print(menu2)
    sel = input("Please enter your choice: ")
 
    if sel == "1":
        timer(25,0 ,title ="study")
        timer(5,0, title = "study_break")
    elif sel == "2":
        timer(45,0, title = "work")
        timer(15,0, title = "work_break")
    elif sel == "3":
        m3()
        


def m1():
    print(menu1)
    if sel == "1":
        m2()
    


def start_or_archive():
    global title
    Start_or_archieve = input('Do you want to start a timer?(y/n): ').lower()
    if Start_or_archieve == 'y':
        title = input ("Do you want to study,work or others?") .lower()
        if title== "study":
            #default timer for study
            print (f'You have chosen {title}')
        elif title == "work":
            #default for study
            print (f'You have chosen {title}')
        elif title == "others":
            other_activity= input ("What do you want to do today?") .lower()
            #ask for duration function
            print (f'You have chosen {other_activity}')
        else:
            print (invalid)
        
        # print(f"working session: {title}")
        
    elif title=='n':
        Archieve= input ('Do you want to look at your history?(y/n): ').lower()
        if Archieve == 'y':
            print ('Loading History..........')
            #Histroy function
        elif Archieve == 'n':
            print ('Bye! Have a great day!')
        else:
            print("incorrct input, please try again")
    else:
        print ('invalid')

if __name__ == "__main__":
    m3()