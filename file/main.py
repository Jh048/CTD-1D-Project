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
    print(menu3)
    sel = input("Please enter your activity (e.g., 'study', 'work', 'others'): ").strip()

    # Get work and rest durations
    print("Set your work duration:")
    work_time = custom_timer_work()
    
    print("Set your rest duration:")
    rest_time = custom_timer_rest()

    # Pass durations to the timer
    while True:
        print(f"Starting work session: {sel}")
        timer(*work_time, title=sel)  # Unpack the time tuple and pass it to the timer
        
        print("Starting rest session...")
        timer(*rest_time, title="rest")  # Unpack the time tuple and pass it to the timer


def m2():
    print(menu2)
    sel = input("Please enter your choice: ")
 
    if sel == "1":
        timer(25,0 ,title ="study")
        timer(5,0, title = "break")
    elif sel == "2":
        timer(45,0, title = "work")
        timer(15,0, title = "break")
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