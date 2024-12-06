menu = '''
Welcome to Pomodoro timer!!!
'''
menu_main = """
-------------------------------------
Welcome to Pomodoro timer!!!
1) Start a timer
2) View history
3) Exit
-------------------------------------


"""

menu1 ="""
----------------------------
Do you want to start a timer?
1) Yes
2) No
----------------------------
"""

menu2 = """                    
--------------------------
Do you want to do?
1) study 
2) work
3) others
--------------------------
"""
menu3 = """                    
--------------------------
"What do you want to do today?"
cooking, meditation, etc

--------------------------
"""
menu4 = """
------------------------------------
Do you want to look at your history?
1) Yes
2) No
------------------------------------
"""

menu6 ="""
------------------------------------
Working Session = {Title}
Enter countdown time in HH,MM,SS format:
eg. 
00,00,10 (10 secs)
00,01,00 (1 min)
01,00,00 (1hr)
01,20,30  (1hr 20min 30 secs)
(N)) No
------------------------------------
"""


menu7 = """
--------------------------
Do you wish to try again?
1) Yes
2) No
--------------------------
"""
menu8 = """
------------------------------------
Do you want to go back to the Menu?
1) Yes
2) No
------------------------------------
"""

menu7 = """
--------------------------
Do you wish to contimue the {} timer?
1) Yes
2) No
--------------------------
"""

def cont(s):
    print(f"""
-----------------------------------------
Do you want to continue with {s}?

1) Yes
2) No

-----------------------------------------
""")


#cont("abc")

def option_m3(s):
    print(f"""
-----------------------------------------
Options to continue: {s}

1) Continue with the {s} time
2) Edit {s} time
3) change activity name

-----------------------------------------
""")


def edit_change(s):
    print(f"""
-----------------------------------------
Do you want to edit {s}?

1) Change Name
2) Change time amount

-----------------------------------------
""")

menu9 = """
-----------------------------------
Options:
1) Back to home
2) View history
3) exit
-----------------------------------
"""