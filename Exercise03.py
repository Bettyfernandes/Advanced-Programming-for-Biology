#-------------------------------
#    HOW MANY DAYS IN A YEAR? 
#-------------------------------

while True:   #porque usamos o while? 
    year = int(input(" How many days in a year? Type 0 to stop executing the program." "\n"))   #não esquecer o int
    if year == 0: 
        break 
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):    #nao existe !%? #não esquecer do == 0
        print(366)
    else: 
        print(365)




