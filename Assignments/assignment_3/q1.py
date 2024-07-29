def num_of_ways(n):
    # Base case 1: When n = 1, there are 2 ways (F or H)
    if n == 1:
        return 2
    
    # Base case 2: When n = 2, there are 3 ways (FH, HF, HH)
    if n == 2:
        return 3
    
    # Recursive case:
    # If the first meal is H, we can have any combination for the rest (n-1) meals
    ways_with_h_first = num_of_ways(n - 1)
    
    # If the first meal is F, we must have H as the second meal,
    # and then any combination for the rest (n-2) meals
    ways_with_f_first = num_of_ways(n - 2)
    
    # Total ways is the sum of both cases
    return ways_with_h_first + ways_with_f_first