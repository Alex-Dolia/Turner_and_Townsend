def The_Collatz_Conjecture(n):
    #
    if not isinstance(n, int):
       raise ValueError("n is NOT INTEGER number")  
    #   
    if n <= 0:
       raise ValueError("n is ZERO or NEGATIVE number") 	
    #
    how_many_steps = 0
    while n > 1:
       if n % 2 == 0:
          n = n // 2
       else:   
          n = 3 * n + 1
       #
       how_many_steps += 1
       #
       # print("n: ",  n, ", how_many_steps: ", how_many_steps)
    #
    return how_many_steps 
