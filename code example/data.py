


import csv

value = []
area = []
year = []
America=[]
Asia = []
Europe = []
Oceania = []
Africa = []
European_Union = []
area1 = []

openfile = open("sgexports_dataset.csv")
csvreader = csv.reader(openfile)

for i in csvreader:
    value.append(i)
    

for i in value[0][1:]:
    year.append(int(i))
for i in value[1][1:]:
    America.append(float(i))
for i in value[2][1:]:
    Asia.append(float(i))
for i in value[3][1:]:
    Europe.append(float(i))
for i in value[4][1:]:
    Oceania.append(float(i))
for i in value[5][1:]:
    Africa.append(float(i))
for i in value[6][1:]:
    European_Union.append(float(i))

America1 = America[:]
Asia1 = Asia[:]
Europe1 = Europe[:]
Oceania1 = Oceania[:]
Africa1 = Africa[:]
European_Union1 = European_Union[:]

count = 0
limit = 4

menu = """
==================================== Menu =====================================
Select one of the following:
    A) Display the exports to Europe for the period 1998 to 2009
    B) The average & the three lowest export values for selected area over a
       selected 6-year span
    C) Display the years and the export values for a selected area if the
       changes in export values are at least 4% over the previous year
    D) Line Plots of America, Asia vs Year 
       Bar Chart of Europe, European Union vs Year
    Q) Quit
===============================================================================
"""

menu1 = """
-------Select an Area------
1) America
2) Asia
3) Europe
4) Oceania
5) Africa
6) European Union
---------------------------
"""

menu2 ="""
----Select a 6-Year Span----
1) 1998 to 2003
2) 2004 to 2009
----------------------------
"""

menu4 = """
--------------------------
Do you wish to try again?
1) Yes
2) No
--------------------------
"""
menu5 = """
------------------------------------
Do you want to go back to the Menu?
1) Yes
2) No
------------------------------------
"""

menu6 = """
------------------------------------------------
Do you want to save the following plots to file?
1) Save line Plot to file only
2) Save Bar Chart to file only
3) Save both plots to file
4) Don't save plots to file
------------------------------------------------
"""


