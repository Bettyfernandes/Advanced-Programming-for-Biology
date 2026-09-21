#-------------------------------
#         SUM OF DIGITS 
#-------------------------------  

def sum_of_digits(n: int) -> int: 
    total = 0 
    while n > 0 : 
        total += n % 10       #ej 1234 % 10 = 4    (resto da divisão; 123,4)
        n //= 10              # Atualiza o n retirando-lhe o 4 (1234:10=123) e assim sucessivamente, até ficar sem numeros.
    return total 
