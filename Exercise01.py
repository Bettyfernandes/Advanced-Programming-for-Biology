#----------------------------------
#   SUM OF THE POSITIVE READINGS 
#---------------------------------- 

N = int(input( "How many values?: ")) 
total = 0 

#conditions
for i in range(N): 
    value = int(input())
    if value > 0: 
        total += value

print(f"Sum of the positive ones =  {total}")



