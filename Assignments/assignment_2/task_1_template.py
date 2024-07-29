## Task 1a #########################################
def alphabet_to_digit(c: str) -> int | None:
    # Case Insensitive
    # 1 = A/a, 2 = B/b, 3 = C/c, ..., 26 = Z/z
    return (
        ord(c) - ord("a") + 1
        if "a" <= c <= "z"
        else ord(c) - ord("A") + 1 if "A" <= c <= "Z" else None
    )


# testing the code for Task 1a
def test_1a():
    print(alphabet_to_digit("a"))
    print(alphabet_to_digit("A"))
    print(alphabet_to_digit("Z"))


## Task 1b #########################################
def convert_prefix(prefix: str) -> list[int | None]:
    last_digit = prefix[-1]
    second_last_digit = prefix[-2] if len(prefix) > 1 else None
    return [
        alphabet_to_digit(second_last_digit) if second_last_digit is not None else 0,
        alphabet_to_digit(last_digit) if last_digit is not None else 0,
    ]


# testing the code for Task 1b
def test_1b():
    print(convert_prefix("E"))
    print(convert_prefix("SH"))
    print(convert_prefix("SBS"))


## Task 1c #########################################
def convert_num_series(num_series: str) -> list[int]:
    def pad(s, width):
        # Check if the string already meets the required width
        if len(s) >= width:
            return s
        # Calculate the number of zeros needed
        zeros_needed = width - len(s)
        # Pad the string with zeros on the left
        return "0" * zeros_needed + s

    padded_string = pad(num_series, 4)
    return [int(i) for i in padded_string]


# testing the code for Task 1c
def test_1c():
    print(convert_num_series("1"))
    print(convert_num_series("10"))
    print(convert_num_series("402"))
    print(convert_num_series("2222"))


## Task 1d #########################################
def multiply_and_add(series):
    multiplier = [9, 4, 5, 4, 3, 2]
    for i in range(len(series)):
        series[i] = series[i] * multiplier[i]
    return sum(series)


# testing the code for Task 1d
def test_1d():
    print(multiply_and_add([2, 19, 0, 0, 1, 0]))
    print(multiply_and_add([0, 5, 2, 2, 2, 2]))
    print(multiply_and_add([1, 1, 1, 1, 1, 1]))


## Task 1e #########################################
def remainder_to_checksum_letter(remainder):
    lut = [
        "A",
        "Z",
        "Y",
        "X",
        "U",
        "T",
        "S",
        "R",
        "P",
        "M",
        "L",
        "K",
        "J",
        "H",
        "G",
        "E",
        "D",
        "C",
        "B",
    ]
    return lut[remainder]


# testing the code for Task 1e
def test_1e():
    print(remainder_to_checksum_letter(0))
    print(remainder_to_checksum_letter(5))
    print(remainder_to_checksum_letter(18))


## Task 1f #########################################
def checksum_calculator(plate):
    def list_to_string(lst):
        s = ""
        for i in lst:
            s += str(i)
        return s

    # Find all alphabets in the plate
    alphabets = list_to_string([c for c in plate if c.isalpha()])
    # Find all numbers in the plate
    numbers = list_to_string([c for c in plate if c.isdigit()])
    # Convert the prefix to a list of integers
    prefix = convert_prefix(alphabets)
    # Convert the number series to a list of integers
    num_series = convert_num_series(numbers)
    # Multiply and add the numbers in the number series
    total = multiply_and_add(prefix + num_series)
    # Calculate the remainder
    remainder = total % 19
    # Get the checksum letter
    checksum_letter = remainder_to_checksum_letter(remainder)
    return checksum_letter


# testing the code for Task 1f
def test_1f():
    print(checksum_calculator("SBS10"))
    print(checksum_calculator("SBS3229"))
    print(checksum_calculator("EV8"))
