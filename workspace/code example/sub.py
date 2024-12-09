
import sys 
import data as d
import numpy as np
import matplotlib.pylab as plt 


def rmain(): 
    d.count += 1
    print(d.count)
    print("Invalid selection")
    print(d.menu4)
    sel = input("Please enter your choice: ")
    if sel == "1":
            return
    elif sel == "2":
            print()
            print("Goodbye and Thank you for using the system")
            sys.exit()
    elif d.count >= d.limit:
            d.count = 0
            print()
            print("Exiting the system due to multiple unsuccessful attempts ")
            sys.exit()
    else:
        rmain()
 
#####################################################################

def rbm():
    d.count += 1
    print(d.count)
    print("Invalid selection")
    print(d.menu4)
    sel = input("Please enter your choice: ")
    if sel == "1":
        bm()
    elif sel == "2":
        print()
        print("Goodbye and Thank you for using the system")
        sys.exit()
    elif d.count >= d.limit:
        d.count = 0
        print()
        print("Exiting the system due to multiple unsuccessful attempts ")
        sys.exit()
    else:
        rbm()
##################################################
def bm():

    print(d.menu5)
    sel = input("Please enter your choice: ")
    if sel == "1":
        return
    elif sel == "2":
        print()
        print("Goodbye and Thank you for using the system")
        sys.exit()
    else:
        rbm()
        
######################################################################################
########################################################################################

def a():

    print(f"the exports value(in S$ Million) to Europe for the period {d.year[0]} to {d.year[-1]}")

    for year, amount in zip(d.year, d.Europe):
        print(f"For year {year}, the export value is $ {amount:.2f}")

###########################################################################

def rb1(): 
    d.count += 1
    print()
    print("Invalid selection")
    print(d.menu4)
    sel = input("Please enter your choice: ")
    if sel == "1":
        b1()
    elif sel == "2":
        pass
    elif d.count >= d.limit:
            d.count = 0
            print()
            print("Exiting the system due to multiple unsuccessful attempts ")
            sys.exit()
    else:
        rb1()

###########################################################################


def b1():
    print(d.menu2)
    sel = input("Please a 6-year span (1 or 2): ")

    if sel == "1": 

        print()
        print("America 6-year span 1998 - 2003: ")
        print("Data: " + str(d.America[0:6]))
        print()
        
        ave = sum(d.America[0:6]) / len(d.America[0:6])
        print(f"Average export value is S$ {ave:.2f} Million")
        print()
    
        m = d.America1[0:6]
        m.sort()
        
        b1 = d.America.index(m[0])
        y1 = d.year[b1]
        print(f"The first  lowest export values is S$ {m[0]:.2f} Million in year {y1} ")
        b2 = d.America.index(m[1])
        y2 = d.year[b2]
        print(f"The second lowest export values is S$ {m[1]:.2f} Million in year {y2} ")
        b3 = d.America.index(m[2])
        y3 = d.year[b3]
        print(f"The third  lowest export values is S$ {m[2]:.2f} Million in year {y3} ")
        
    elif sel == "2":
        print()
        print("America 6-year span 2004 - 2009: ")
        print("Data: " + str(d.America[6:12]))
        print()
            
        ave = sum(d.America[6:12]) / len(d.America[6:12])
        print(f"Average export value is S$ {ave:.2f} Million")
        print()    
        
        m = d.America1[6:12]
        m.sort()
        
        b1 = d.America.index(m[0])
        y1 = d.year[b1]
        print(f"The first  lowest export values is S$ {m[0]:.2f} Million in year {y1} ")
        b2 = d.America.index(m[1])
        y2 = d.year[b2]
        print(f"The second lowest export values is S$ {m[1]:.2f} Million in year {y2} ")
        b3 = d.America.index(m[2])
        y3 = d.year[b3]
        print(f"The third  lowest export values is S$ {m[2]:.2f} Million in year {y3} ")
        

    else:
        rb1()       



#############################################################################################

def rb2(): 
    d.count += 1
    print()
    print("Invalid selection")
    print(d.menu4)
    sel = input("Please enter your choice: ")
    if sel == "1":
        b2()
    elif sel == "2":
        pass
    elif d.count >= d.limit:
            d.count = 0
            print()
            print("Exiting the system due to multiple unsuccessful attempts ")
            sys.exit()
    else:
        rb2()

########################################################################################


def b2():
    print(d.menu2)
    sel = input("Please a 6-year span (1 or 2): ")

    if sel == "1":
        print()
        print("Asia 6-year span 1998 - 2003: ")
        print("Data: " + str(d.Asia[0:6]))
        print()
    
        ave = sum(d.Asia[0:6]) / len(d.Asia[0:6])
        print(f"Average export value is S$ {ave:.2f} Million")
        print()
    
        m = d.Asia1[0:6]
        m.sort()
        
        b1 = d.Asia.index(m[0])
        y1 = d.year[b1]
        print(f"The first  lowest export values is S$ {m[0]:.2f} Million in year {y1} ")
        b2 = d.Asia.index(m[1])
        y2 = d.year[b2]
        print(f"The second lowest export values is S$ {m[1]:.2f} Million in year {y2} ")
        b3 = d.Asia.index(m[2])
        y3 = d.year[b3]
        print(f"The third  lowest export values is S$ {m[2]:.2f} Million in year {y3} ")
        
    elif sel == "2":
        print()
        print("Asia 6-year span 2004 - 2009: ")
        print("Data: " + str(d.Asia[6:12]))
        print()
    
        ave = sum(d.Asia[6:12]) / len(d.Asia[6:12])
        print(f"Average export value is S$ {ave:.2f} Million")
        print()
    
        m = d.Asia1[6:12]
        m.sort()
        
        b1 = d.Asia.index(m[0])
        y1 = d.year[b1]
        print(f"The first  lowest export values is S$ {m[0]:.2f} Million in year {y1} ")
        b2 = d.Asia.index(m[1])
        y2 = d.year[b2]
        print(f"The second lowest export values is S$ {m[1]:.2f} Million in year {y2} ")
        b3 = d.Asia.index(m[2])
        y3 = d.year[b3]
        print(f"The third  lowest export values is S$ {m[2]:.2f} Million in year {y3} ")
        
    else:
        rb2()       

        
##########################################################################################

def rb3(): 
    d.count += 1
    print()
    print("Invalid selection")
    print(d.menu4)
    sel = input("Please enter your choice: ")
    if sel == "1":
        b3()
    elif sel == "2":
        pass
    elif d.count >= d.limit:
            d.count = 0
            print()
            print("Exiting the system due to multiple unsuccessful attempts ")
            sys.exit()
    else:
        rb3()

#############################################################################

def b3():
    print(d.menu2)
    sel = input("Please a 6-year span (1 or 2): ")
    if sel == "1":
    
        print()
        print("Europe 6-year span 1998 - 2003: ")
        print("Data: " + str(d.Europe[0:6]))
        print()
    
        ave = sum(d.Europe[0:6]) / len(d.Europe[0:6])
        print(f"Average export value is S$ {ave:.2f} Million")
        print()
    
        m = d.Europe1[0:6]
        m.sort()
        
        b1 = d.Europe.index(m[0])
        y1 = d.year[b1]
        print(f"The first  lowest export values is S$ {m[0]:.2f} Million in year {y1} ")
        b2 = d.Europe.index(m[1])
        y2 = d.year[b2]
        print(f"The second lowest export values is S$ {m[1]:.2f} Million in year {y2} ")
        b3 = d.Europe.index(m[2])
        y3 = d.year[b3]
        print(f"The third  lowest export values is S$ {m[2]:.2f} Million in year {y3} ")
        
    elif sel == "2":
        print()
        print("Europe 6-year span 2004 - 2009: ")
        print("Data: " + str(d.Europe[6:12]))
        print()
        
        ave = sum(d.Europe[6:12]) / len(d.Europe[6:12])
        print(f"Average export value is S$ {ave:.2f} Million")
        print()
   
        m = d.Europe1[6:12]
        m.sort()
        
        b1 = d.Europe.index(m[0])
        y1 = d.year[b1]
        print(f"The first  lowest export values is S$ {m[0]:.2f} Million in year {y1} ")
        b2 = d.Europe.index(m[1])
        y2 = d.year[b2]
        print(f"The second lowest export values is S$ {m[1]:.2f} Million in year {y2} ")
        b3 = d.Europe.index(m[2])
        y3 = d.year[b3]
        print(f"The third  lowest export values is S$ {m[2]:.2f} Million in year {y3} ")
        
    else:
        rb3()          


###################################################################################

def rb4(): 
    d.count += 1
    print()
    print("Invalid selection")
    print(d.menu4)
    sel = input("Please enter your choice: ")
    if sel == "1":
        b4()
    elif sel == "2":
        pass
    elif d.count >= d.limit:
            d.count = 0
            print()
            print("Exiting the system due to multiple unsuccessful attempts ")
            sys.exit()
    else:
        rb4()


###############################################################################

def b4():
    print(d.menu2)
    sel = input("Please a 6-year span (1 or 2): ")
    if sel == "1":
    
        print()
        print("Oceania 6-year span 1998 - 2003: ")
        print("Data: " + str(d.Oceania[0:6]))
        print()
    
        ave = sum(d.Oceania[0:6]) / len(d.Oceania[0:6])
        print(f"Average export value is S$ {ave:.2f} Million")
        print()
    
        m = d.Oceania1[0:6]
        m.sort()
        
        b1 = d.Oceania.index(m[0])
        y1 = d.year[b1]
        print(f"The first  lowest export values is S$ {m[0]:.2f} Million in year {y1} ")
        b2 = d.Oceania.index(m[1])
        y2 = d.year[b2]
        print(f"The second lowest export values is S$ {m[1]:.2f} Million in year {y2} ")
        b3 = d.Oceania.index(m[2])
        y3 = d.year[b3]
        print(f"The third  lowest export values is S$ {m[2]:.2f} Million in year {y3} ")
        
    
    elif sel == "2":
        print()
        print("Asia 6-year span 2004 - 2009: ")
        print("Data: " + str(d.Oceania[6:12]))
        print()
    
        ave = sum(d.Oceania[6:12]) / len(d.Oceania[6:12])
        print(f"Average export value is S$ {ave:.2f} Million")
        print()
    
        m = d.Oceania1[6:12]
        m.sort()
        
        b1 = d.Oceania.index(m[0])
        y1 = d.year[b1]
        print(f"The first  lowest export values is S$ {m[0]:.2f} Million in year {y1} ")
        b2 = d.Oceania.index(m[1])
        y2 = d.year[b2]
        print(f"The second lowest export values is S$ {m[1]:.2f} Million in year {y2} ")
        b3 = d.Oceania.index(m[2])
        y3 = d.year[b3]
        print(f"The third  lowest export values is S$ {m[2]:.2f} Million in year {y3} ")
        
    else:
        rb4()                      
      

#################################################################################

def rb5(): 
    d.count += 1
    print()
    print("Invalid selection")
    print(d.menu4)
    sel = input("Please enter your choice: ")
    if sel == "1":
        b5()
    elif sel == "2":
        pass
    elif d.count >= d.limit:
            d.count = 0
            print()
            print("Exiting the system due to multiple unsuccessful attempts ")
            sys.exit()
    else:
        rb5()


##########################################################################################

def b5():
    print(d.menu2)
    sel = input("Please a 6-year span (1 or 2): ")
    if sel == "1":
    
        print()
        print("Africa 6-year span 1998 - 2003: ")
        print("Data: " + str(d.Africa[0:6]))
        print()
    
        ave = sum(d.Africa[0:6]) / len(d.Africa[0:6])
        print(f"Average export value is S$ {ave:.2f} Million")
        print()
    
        m = d.Africa1[0:6]
        m.sort()
        
        b1 = d.Africa.index(m[0])
        y1 = d.year[b1]
        print(f"The first  lowest export values is S$ {m[0]:.2f} Million in year {y1} ")
        b2 = d.Africa.index(m[1])
        y2 = d.year[b2]
        print(f"The second lowest export values is S$ {m[1]:.2f} Million in year {y2} ")
        b3 = d.Africa.index(m[2])
        y3 = d.year[b3]
        print(f"The third  lowest export values is S$ {m[2]:.2f} Million in year {y3} ")
        

    elif sel == "2":
        print()
        print("Africa 6-year span 2004 - 2009: ")
        print("Data: " + str(d.Africa[6:12]))
        print()
    
        ave = sum(d.Africa[6:12]) / len(d.Africa[6:12])
        print(f"Average export value is S$ {ave:.2f} Million")
        print()
    
        m = d.Africa1[6:12]
        m.sort()
        
        b1 = d.Africa.index(m[0])
        y1 = d.year[b1]
        print(f"The first  lowest export values is S$ {m[0]:.2f} Million in year {y1} ")
        b2 = d.Africa.index(m[1])
        y2 = d.year[b2]
        print(f"The second lowest export values is S$ {m[1]:.2f} Million in year {y2} ")
        b3 = d.Africa.index(m[2])
        y3 = d.year[b3]
        print(f"The third  lowest export values is S$ {m[2]:.2f} Million in year {y3} ")
        
    else:
        rb5()       


#######################################################################################

def rb6(): 
    d.count += 1
    print()
    print("Invalid selection")
    print(d.menu4)
    sel = input("Please enter your choice: ")
    if sel == "1":
        b6()
    elif sel == "2":
        pass
    elif d.count >= d.limit:
            d.count = 0
            print()
            print("Exiting the system due to multiple unsuccessful attempts ")
            sys.exit()
    else:
        rb6()

            
###############################################################################################

def b6():
    print(d.menu2)
    sel = input("Please a 6-year span (1 or 2): ")
    if sel == "1":
     
        print()
        print("European Union 6-year span 1998 - 2003: ")
        print("Data: " + str(d.European_Union[0:6]))
        print()
    
        ave = sum(d.European_Union[0:6]) / len(d.European_Union[0:6])
        print(f"Average export value is S$ {ave:.2f} Million")
        print()
    
        m = d.European_Union1[0:6]
        m.sort()
        
        b1 = d.European_Union.index(m[0])
        y1 = d.year[b1]
        print(f"The first  lowest export values is S$ {m[0]:.2f} Million in year {y1} ")
        b2 = d.European_Union.index(m[1])
        y2 = d.year[b2]
        print(f"The second lowest export values is S$ {m[1]:.2f} Million in year {y2} ")
        b3 = d.European_Union.index(m[2])
        y3 = d.year[b3]
        print(f"The third  lowest export values is S$ {m[2]:.2f} Million in year {y3} ")
        
    elif sel == "2":
        print()
        print("European Union 6-year span 2004 - 2009: ")
        print("Data: " + str(d.Asia[6:12]))
        print()
    
        ave = sum(d.European_Union[6:12]) / len(d.European_Union[6:12])
        print(f"Average export value is S$ {ave:.2f} Million")
        print()
     
        m = d.European_Union1[6:12]
        m.sort()
        
        b1 = d.European_Union.index(m[0])
        y1 = d.year[b1]
        print(f"The first  lowest export values is S$ {m[0]:.2f} Million in year {y1} ")
        b2 = d.European_Union.index(m[1])
        y2 = d.year[b2]
        print(f"The second lowest export values is S$ {m[1]:.2f} Million in year {y2} ")
        b3 = d.European_Union.index(m[2])
        y3 = d.year[b3]
        print(f"The third  lowest export values is S$ {m[2]:.2f} Million in year {y3} ")
        
    else:
        rb6()       

#######################################################################3   

def rb(): 
    d.count += 1
    print()
    print("Invalid selection")
    print(d.menu4)
    sel = input("Please enter your choice: ")
    if sel == "1":
        b()
    elif sel == "2":
        pass
    elif d.count >= d.limit:
            d.count = 0
            print()
            print("Exiting the system due to multiple unsuccessful attempts ")
            sys.exit()
    else:
        rb()

      

####################################################################################
        
def b():
    print(d.menu1)
    sel = input("Please select an Area (1 - 6): ")
    
    if sel == "1":
        b1()
    elif sel == "2":
        b2()
    elif sel == "3":
        b3()        
    elif sel == "4":
        b4()
    elif sel == "5":
        b5()
    elif sel == "6":
        b6()
    else:
        rb()

###########################################################################
#############################################################################


def rc(): 
    print()
    print("Invalid selection")
    print(d.menu4)
    restart = input("Please enter your choice: ")
    if restart == "1":
         c() 
    elif restart == "2":
        print(d.menu5)
        sel = input("Plesae enter your choice: ")
        if sel == "1":
            pass
        elif sel == "2":
            print()
            print("Goodbye and Thank you for using the system")
            sys.exit() 
    else:
        d.count += 1
        if d.count == d.limit:
            d.count = 0
            print()
            print("Exiting the system due to multiple attempts ")
            print()
            sys.exit()
        else:
            rc()
   

##############################################################################

def c():
    print(d.menu1)
    sel = input("Please select an Area (1 - 6): ")
    if sel == "1":
        print()
        print("The years and the export values that are of at least +- 4% over the previous year")
        print()
        for i in range(1,len(d.America)):
            year = d.year[i]
            value = ((d.America[i] - d.America[i-1]) / d.America[i-1])*100  
            if value >= 4 or value <= -4: 
                print(f"For year {year}, the export value is S$ {d.America[i]:.2f} Million")

    elif sel == "2":
        print()
        print("the years and the export values that are of at least +- 4% over the previous year")
        print()
        for i in range(1,len(d.Asia)):
            year = d.year[i] 
            value = ((d.Asia[i] - d.Asia[i-1]) / d.Asia[i-1])*100    
            if value >= 4 or value <= -4: 
                print(f"For year {year}, the export value is S$ {d.Asia[i]:.2f} Million")
                
    elif sel == "3":
        print()
        print("the years and the export values that are of at least +- 4% over the previous year")
        print()
        for i in range(1,len(d.Europe)):
            year = d.year[i] 
            value = ((d.Europe[i] - d.Europe[i-1]) / d.Europe[i-1])*100    
            if value >= 4 or value <= -4: 
                print(f"For year {year}, the export value is S$ {d.Europe[i]:.2f} Million")
            
    elif sel == "4":
        print()
        print("the years and the export values that are of at least +- 4% over the previous year")
        print()
        for i in range(1,len(d.Oceania)):
            year = d.year[i]
            value = ((d.Oceania[i] - d.Oceania[i-1]) / d.Oceania[i-1])*100    
            if value >= 4 or value <= -4: 
                print(f"For year {year}, the export value is S$ {d.Oceania[i]:.2f} Million")
              
    elif sel == "5":
        print()
        print("the years and the export values that are of at least +- 4% over the previous year")
        print()
        for i in range(1,len(d.Africa)):
            year = d.year[i] 
            value = ((d.Africa[i] - d.Africa[i-1]) / d.Africa[i-1])*100    
            if value >= 4 or value <= -4: 
                print(f"For year {year}, the export value is S$ {d.Africa[i]:.2f} Million")
               
    elif sel == "6":
        print()
        print("the years and the export values that are of at least +- 4% over the previous year")
        print()
        for i in range(1,len(d.European_Union)):
            year = d.year[i] 
            value = ((d.European_Union[i] - d.European_Union[i-1]) / d.European_Union[i-1])*100    
            if value >= 4 or value <= -4: 
                print(f"For year {year}, the export value is S$ {d.European_Union[i]:.2f} Million")
        
    else:
        rc()


############################################ #############################
##########################################################################



def rsp():
    print()
    print("Invalid selection")
    print(d.menu4)#try again?
    restart = input("Please enter your choice: ")
    if restart == "1":#Yes
         sp() 
    elif restart == "2":#No
        pass  
    else:
        d.count += 1
        if d.count == d.limit:
            d.count = 0
            print()
            print("Exiting the system due to multiple unsuccessful attempts ")
            print()
            sys.exit()
        else:
            rsp()

###########################################################################


def sp():
    print(d.menu6)
    sel = input("Please enter your choice: ")
    if sel == "1":
        bar1 = np.arange(len(d.year))
        plt.plot(d.America, label= "America",color = "green")
        plt.plot(d.Asia, label= "Asia", color = "blue") 
        plt.xlabel("Year") 
        plt.ylabel("value in ( S$ Million )") 
        plt.grid(True) 
        plt.legend() 
        plt.xticks(bar1,d.year)
        plt.title("Export to America, Asia vs Year") 
        plt.savefig("project_Plot_lineGraph.pdf", bbox_inches = "tight") 
        print()
        print("Line Graph has been saved")
        
    
    elif sel == "2":
        w = 0.35 
        bar1 = np.arange(len(d.year)) 
        bar2 = [i+w for i in bar1] 
        plt.bar(bar1, d.Europe, w, label = "Europe", color = "Green") 
        plt.bar(bar2, d.European_Union, w, label = "European Union", color = "Red") 
        plt.grid(True) 
        plt.xlabel("year") 
        plt.ylabel("value in (S$ Million)") 
        plt.title("Exports to Europe, European Union vs Year")
        plt.legend() 
        plt.xticks(bar1+w/2,d.year) 
        plt.savefig("project_Plot_BarChart.pdf", bbox_inches = "tight")
        print()
        print("Bar Chart has been saved")
    
    elif sel == "3":
        bar1 = np.arange(len(d.year))
        plt.plot(d.America, label= "America",color = "green")
        plt.plot(d.Asia, label= "Asia", color = "blue") 
        plt.xlabel("Year") 
        plt.ylabel("value in ( S$ Million )") 
        plt.grid(True) 
        plt.legend() 
        plt.xticks(bar1,d.year)
        plt.title("Export to America, Asia vs Year") 
        plt.savefig("project_Plot_lineGraph.pdf", bbox_inches = "tight") 
        print()
        print("Line Graph has been saved")
        w = 0.35 
        bar1 = np.arange(len(d.year)) 
        bar2 = [i+w for i in bar1] 
        plt.bar(bar1, d.Europe, w, label = "Europe", color = "Green") 
        plt.bar(bar2, d.European_Union, w, label = "European Union", color = "Red") 
        plt.grid(True) 
        plt.xlabel("year") 
        plt.ylabel("value in (S$ Million)") 
        plt.title("Exports to Europe, European Union vs Year")
        plt.legend() 
        plt.xticks(bar1+w/2,d.year) 
        plt.savefig("project_Plot_BarChart.pdf", bbox_inches = "tight")
        print()
        print("Bar Chart has been saved")
    
    elif sel == "4":
        pass
    else:
        rsp()            



        

###########################################################################################

    
def d1():



    print()
    print("Exports to America, Asia vs Year as line plot")
    bar1 = np.arange(len(d.year))
    plt.plot(d.America, label= "America",color = "green")
    plt.plot(d.Asia, label= "Asia", color = "blue") 
    plt.xlabel("Year") 
    plt.ylabel("value in ( S$ Million )") 
    plt.grid(True) 
    plt.legend() 
    plt.xticks(bar1,d.year)
    plt.title("Export to America, Asia vs Year") 
    plt.show()
    
    print("and")    
    
    print("Exports to Europe, European Union vs Year as bar chart")            
    w = 0.35 
    bar1 = np.arange(len(d.year)) 
    bar2 = [i+w for i in bar1] 
    plt.bar(bar1, d.Europe, w, label = "Europe", color = "Green") 
    plt.bar(bar2, d.European_Union, w, label = "European Union", color = "Red") 
    plt.grid(True) 
    plt.xlabel("year") 
    plt.ylabel("value in (S$ Million)") 
    plt.title("Exports to Europe, European Union vs Year")
    plt.legend() 
    plt.xticks(bar1+w/2,d.year) 
    plt.show()

    sp()        


##################################################################################################

