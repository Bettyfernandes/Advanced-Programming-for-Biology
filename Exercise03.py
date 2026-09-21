#-----------------------------------------------
#             INCUBATION SUITABLE 
#-----------------------------------------------

#INPUTS

temperature=float(input("Temperature(C): "))
humidity=float(input("Humidity(%): "))

# Condictions 
if (30 <= temperature <= 40) and (humidity >=40):
    print("suitable") 
else: 
    print("not suitable")

