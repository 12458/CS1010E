def encode_I(s1, s2, m):
    # iterative version
    lower_case = s1.lower()
    result = ""
    for idx, letter in enumerate(lower_case):
        # convert letter to alphabet index
        index = ord(letter) - ord("a")
        # shift index by m * s2[idx] and wrap around
        new_index = (index + m * int(s2[idx])) % 26
        # convert new index to alphabet letter
        new_letter = chr(new_index + ord("a"))
        result += new_letter
    return result


# print(encode_I("spyxfamily", "2222222222", 1))  # urazhcokna
# print(encode_I("krmxhaeaba", "9170109981", -2))  # spyxfamily


def encode_R(s1, s2, m, idx=0):
    # Base case: if we've processed all characters, return an empty string
    if idx == len(s1):
        return ""

    # Process the current character
    letter = s1[idx].lower()
    index = ord(letter) - ord("a")
    new_index = (index + m * int(s2[idx])) % 26
    new_letter = chr(new_index + ord("a"))

    # Recursive call for the rest of the string
    return new_letter + encode_R(s1, s2, m, idx + 1)


# print(encode_R("spyxfamily", "2222222222", 1))  # urazhcokna
# print(encode_R("krmxhaeaba", "9170109981", -2))  # spyxfamily


def encode_U(s1, s2, m):
    # one-liner
    return "".join(
        [
            chr((ord(s1[i].lower()) - ord("a") + m * int(s2[i])) % 26 + ord("a"))
            for i in range(len(s1))
        ]
    )


# print(encode_R("spyxfamily", "2222222222", 1))  # urazhcokna
# print(encode_R("krmxhaeaba", "9170109981", -2))  # spyxfamily
