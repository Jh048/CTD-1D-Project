from menu import *
from timerA import *


# loop = True
# while loop:
#     print("Welcome to Pomodoro timer!!!")
#     print(menu2)
#     sel = input("Please enter your choice: ")





def custom_timer_work():
    sel = input("Please enter your work time amount: ")
    selintwork = int(sel)
    return

def custom_timer_rest():
    sel = input("Please enter your rest time amount: ")
    selintrest = int(sel)
    return

def m2():
    print(menu2)
    if sel == "1":
        timer(25,0)
        timer(5,0)
    elif sel == "2":
        timer(45,0)
        timer(15,0)
    elif sel == "3":
        custom_timer_work()
        custom_timer_rest()
        timer(custom_timer_work)
        timer(custom_timer_rest)

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
    custom_timer_work()