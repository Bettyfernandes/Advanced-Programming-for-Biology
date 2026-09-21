#-----------------------------------------------------------
#                 Serial dilution calculator
#-----------------------------------------------------------

# Inputs

C1 = float(input("Stock concentration (ng/ul): " ))
C2 = float(input("Desired concentration (ng/ul): " ))

V2 = float(input("Final volume (ul): " ))


V1 = (C2 * V2) / C1                    # Dilution equation

diluent= V2 - V1                       # Volume of diluent (water/buffer)


#Outputs

print(f"Stock volume:  {V1:.1f} uL")
print(f"Diluent volume: {diluent:.1f} uL")






