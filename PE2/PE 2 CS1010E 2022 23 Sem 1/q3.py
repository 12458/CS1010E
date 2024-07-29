def min_no_of_turns(L):
    # strategy: (1) sort the array, (2) find longest consecutive subsequence, (3) eliminate the subsequence from the array, (4) repeat until array is empty

    L_copy = list(L)
    L_copy.sort()
    turns = 0
    while L_copy:
        print(L_copy)
        # find the longest consecutive subsequence
        longest_subsequence = []
        current_subsequence = [L_copy[0]]
        for i in range(1, len(L_copy)):
            if L_copy[i] == L_copy[i - 1] + 1:
                current_subsequence.append(L_copy[i])
            else:
                if len(current_subsequence) > len(longest_subsequence):
                    longest_subsequence = current_subsequence
                current_subsequence = [L_copy[i]]
        if len(current_subsequence) > len(longest_subsequence):
            longest_subsequence = current_subsequence

        # remove the longest subsequence from the array
        print(f"longest_subsequence: {longest_subsequence}")
        for elem in longest_subsequence:
            L_copy.remove(elem)
        turns += 1
    return turns


# print(min_no_of_turns((1, 8, 3, 6, 5, 7, 2, 1)))
# print(min_no_of_turns((1, 8, 3, 6, 5, 7, 2, 1, 4)))
tup3 = (6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 6, 5, 16, 16)
print(min_no_of_turns(tup3))
