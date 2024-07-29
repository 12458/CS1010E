## Task 3a #######################################
def sum1(lst) -> None:
    # You can use the following statements
    #
    #     print("{}#".format(var1))
    #     print("{},{}#".format(var1,var2))
    #     print("{}[{},{}]#".format(var1,var2,var3))
    #
    # to print out values of var1 and var2 in the
    # format required by the task
    cum_sum = 0
    for i in range(len(lst)):
        cum_sum += lst[i]
        print(f"{lst[i]},{cum_sum}#")


# test cases
sum1([1, 2, 3])
print()
sum1([1])
print()
sum1([-1])
print()
sum1([-1, 2, -3])
print()
sum1([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print()


## Task 3b #######################################
def sum2(lst):
    cur_max_sum = -9e9
    cum_sum = 0
    for i in range(len(lst)):
        cum_sum += lst[i]
        print(f"{lst[i]},{cum_sum}#")
        if cum_sum > cur_max_sum:
            cur_max_sum = cum_sum
    print(f"{cur_max_sum}#")


# test cases
print("Task 3b")
sum2([-2, 1, -3, 4, -1, 2, 1, -5])
print()
sum2([-1, 2, -3])
print()
sum2([-1])
print()
sum2([1, 2, 3])
print()


## Task 3c #######################################
def sum3(lst):
    cur_max_sum = -9e9
    cum_sum = 0
    for i in range(len(lst)):
        if cum_sum < 0:
            cum_sum = 0
        cum_sum += lst[i]
        print(f"{lst[i]},{cum_sum}#")
        if cum_sum > cur_max_sum:
            cur_max_sum = cum_sum
    print(f"{cur_max_sum}#")


# test cases
print("Task 3c")
sum3([1])
print()
sum3([-1])
print()
sum3([1, 1])
print()
sum3([1, -1])
print()
sum3([-1, 1])
print()
sum3([-1, -1])
print()
sum3([1, 1, -1])
print()
sum3([1, -1, 1])
print()
sum3([-1, 1, -1])
print()
sum3([1, -1, 2])
print()
sum3([-1, 2, -3, 4])
print()
sum3([1, 1, -2, 2])
print()
sum3([2, -1, 1])
print()
sum3([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print()


## Task 3d #######################################
def sum4(arr):
    max_sum = -9e9
    current_sum = 0
    start = 0
    end = 0
    temp_start = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        print(f"{arr[i]},{current_sum}#")

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
        elif current_sum == max_sum:
            if i < end or (i == end and i - temp_start + 1 < min_length):
                start = temp_start
                end = i
                min_length = i - temp_start + 1

        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1
        elif current_sum == 0:
            temp_start = i + 1

    print(f"{max_sum}[{start+1},{end+1}]#")


# test cases
print("Task 3d")
sum4([1])
print()
sum4([-1])
print()
sum4([1, 1])
print()
sum4([1, -1])
print()
sum4([-1, 1])
print()
sum4([-1, -1])
print()
sum4([1, 1, -1])
print()
sum4([1, -1, 1])
print()
sum4([-1, 1, -1])
print()
sum4([1, -1, 2])
print()
sum4([-1, 2, -3, 4])
print()
sum4([1, 1, -2, 2])
print()
sum4([2, -1, 1])
print()
sum4([1, -1, 2, -2, 2])
print()
sum4([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print()
sum4([1, -1, 2, -2, 2, 0])
print()
