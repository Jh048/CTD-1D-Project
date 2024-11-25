

import data as d
import sub as s



loop = True
while loop:

    print(d.menu)
    sel = input("Please enter your choice: ")
    
    if sel == "A" or sel == "a":
        s.a()
        s.bm()

    elif sel == "B" or sel == "b":
        s.b()
        s.bm()

    elif sel == "C" or sel == "c":
        s.c() 
        s.bm()

    elif sel == "D" or sel == "d": 
        s.d1() 
        s.bm()
        
    elif sel == "Q" or sel == "q":
        print("Goodbye and Thank you for using the system")
        loop = False
        
    else:
        s.rmain()  
