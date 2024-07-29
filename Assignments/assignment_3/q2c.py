def assign(letters, numbers_left, mapping, puzzle):
    if not letters:         # base case 1: possibly found a solution
        return check(puzzle, mapping)
    if not numbers_left:    # base case 2: an error
        return False
    curr_letter = letters[0]
    
    for i in range(len(numbers_left)):
        # assign a number in numbers_left to the current letter
        # update it to a new map
        # need to keep the old map for use in the following iteration
        map_copy = mapping.copy()
        map_copy[curr_letter] = numbers_left[i]
        
        # Recursive call with updated parameters
        res = assign(letters[1:], numbers_left[:i] + numbers_left[i+1:], map_copy, puzzle)
        if res:
            return res
        # If res is False, the loop will continue to the next iteration
    
    # Going through all available numbers, fail to find a good mapping
    return False
