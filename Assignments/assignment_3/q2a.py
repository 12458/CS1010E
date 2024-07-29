def check(puzzle, mapping):
    def word_to_num(word):
        # Convert a word to its numeric value based on the mapping
        return int(''.join(str(mapping[letter]) for letter in word))
    
    # Check if the first letter of any word maps to 0
    for word in puzzle:
        if mapping[word[0]] == 0:
            return False
    
    # Convert all words to numbers
    numbers = [word_to_num(word) for word in puzzle[:-1]]
    result = word_to_num(puzzle[-1])
    
    # Check if the sum of the numbers equals the result
    if sum(numbers) == result:
        return mapping
    else:
        return False