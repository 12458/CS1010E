def min_no_of_turns(L):
    if not L:
        return 0

    # Sort the list to handle consecutive sequences
    sorted_L = sorted(L)

    # Use a dictionary to group consecutive sequences
    sequences = {}
    current_seq = []
    
    for num in sorted_L:
        if not current_seq or num == current_seq[-1] + 1:
            current_seq.append(num)
        else:
            seq_key = tuple(current_seq)
            sequences[seq_key] = len(current_seq)
            current_seq = [num]
    
    # Add the last sequence
    if current_seq:
        seq_key = tuple(current_seq)
        sequences[seq_key] = len(current_seq)

    # The number of turns is the number of sequences
    return len(sequences)


# print(min_no_of_turns((1, 8, 3, 6, 5, 7, 2, 1)))
# print(min_no_of_turns((1, 8, 3, 6, 5, 7, 2, 1, 4)))
tup3 = (6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 6, 5, 16, 16)
print(min_no_of_turns(tup3))
