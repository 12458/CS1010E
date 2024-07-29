def solve(puzzle):
    # Get unique letters from the puzzle
    letters = unique_letters(puzzle)
    
    # Create a tuple of available numbers (0 to 9)
    numbers = tuple(range(10))
    
    # Start with an empty mapping
    initial_mapping = {}
    
    # Use the assign function to find a valid mapping
    result = assign(letters, numbers, initial_mapping, puzzle)
    
    # Return the result (either a valid mapping or False)
    return result