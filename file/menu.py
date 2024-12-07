menu1 = """
------------------------
Welcome to Tomoto timer
1) Start a timer
2) View history
3) Exit
------------------------

"""

menu2 = """                    
--------------------------
what do you want to do?
1) study 
2) work
3) others
--------------------------
"""
menu3 = """                    
------------------------------------
What do you want to do today?
math,cook, meditate, etc
------------------------------------
"""



def menu6(title):
    print(f"""
------------------------------------
Working Session = {title}
Enter countdown time in HH,MM,SS format:
eg. 
00,00,10 (10 secs)
00,01,00 (1 min)
01,00,00 (1hr)
01,20,30  (1hr 20min 30 secs)
------------------------------------
""")


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

menu9 = """
--------------------------
Do you wish to continue the {} timer?
1) Yes
2) No
--------------------------
"""

def cont_menu(s):
    print(f"""
-----------------------------------------
Do you want to continue: {s}

1) Yes
2) No

-----------------------------------------
""")


#cont("abc")

def option_m3(s):
    print(f"""
-----------------------------------------
Options to continue: {s}

1) Continue with the {s} timer
2) Edit {s} time
3) change activity name

-----------------------------------------
""")


def edit_change(s):
    print(f"""
-----------------------------------------
Do you want to edit {s}?

1) Change Name
2) Change Time amount

-----------------------------------------
""")

menu9 = """
-----------------------------------
Options:
1) Back to home
2) View history
3) Exit
-----------------------------------
"""

menu10 = """
-----------------------------------
Invalid selection, Please try again.

1) Return to previous program
2) Exit

-----------------------------------
"""
