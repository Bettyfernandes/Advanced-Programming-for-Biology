#----------------------------------------------
#          GC content quality check 
#----------------------------------------------

base_A: int = int(input("Count of A: " ))
base_C: int = int(input("Count of C: " ))
base_G: int = int(input("Count of G: " ))
base_T: int = int(input("Count of T: " ))


total: int = base_A + base_C + base_G + base_T
gc_percent: float = round (100*(base_C + base_G)/total, 1)

#print("GC content:" , gc_percent,"%") 
print(f"GC content: {gc_percent} %")
      
if 40.0 <= gc_percent <= 60.0: 
    print ("PASS") 
else: 
    print("FAIL")







