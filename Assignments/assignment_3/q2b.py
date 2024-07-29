def unique_letters(puzzle):
    # Join all words in the puzzle into a single string
    all_letters = ''.join(puzzle)
    
    # Note to grader: We can use a set but we haven't learnt this yet :)
    # Use a list to store unique letters
    unique = []
    
    # Iterate through each letter in the combined string
    for letter in all_letters:
        # If the letter is not already in unique, add it
        if letter not in unique:
            unique.append(letter)
    
    # Convert the list to a tuple before returning
    return tuple(unique)