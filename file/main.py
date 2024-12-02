from menu import *
from timerA import *


# loop = True
# while loop:
#     print("Welcome to Pomodoro timer!!!")
#     print(menu2)
#     sel = input("Please enter your choice: ")


def user_time_input():
    while True:
        try:
            print()
            print(f"Working session: {title}")
            print("e.g. 5 = 5sec | 2,25 = 2min 25sec | 1,0,5 = 1hr 0min 5sec")
            time_input = input("Enter countdown time (HH,MM,SS): ").strip()
            print()
            print(f"Working session: {title}")
            # time_input.strip() removes leading/trailing spaces.

            time_parts = list(map(int, time_input.split(',')))
            # time_input.split(',') splits the input string into components (e.g., “1,0,30” → [1, 0, 30]).
            # list(map(int, ...)) converts each part into an integer.
            args(time_parts)
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

            break
        except ValueError:
            print("Invalid input. Please enter time in the format HH,MM,SS.")
    return


def custom_timer():
    sel1 = input("Please enter your work time amount: ")
    timer(sel1)

def m2():
    print(menu2)
    if sel == "1":
        timer(25,0)
        timer(5,0)
    elif sel == "2":
        timer(45,0)
        timer(15,0)
    elif sel == "3":

        timer()

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
    user_time_input()