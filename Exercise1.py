#-------------------------------------------------------
#         DNA to Rna, one base at a time 
#-------------------------------------------------------


#Convert a single DNA base to its RNA equivalent.
def dna_to_rna(base:str) -> str: 
    if base == "T": 
        return "U"
    else: 
        return base 

#Read one base from the user and print its RNA equivalent.
def main() -> None: 
    base = input ()
    print (dna_to_rna(base))

if __name__ == "__main__": 
    main()

    