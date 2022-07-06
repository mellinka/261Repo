# Name: Karl Mellinger
# OSU Email: mellinka@oregonstate.edu
# Course:       CS261 - Data Structures
# Assignment: 1
# Due Date: 4/18/2022
# Description: 10 Methods that need to be implemented using the static_array class.


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------
# min_max takes a StaticArray arr, loops through arr, setting a new value to min or max depending on if it was less than or greater than
# the previous, respectively. It returns a Tuple of min, max.
def min_max(arr: StaticArray) -> tuple:
    min = arr.get(0)
    max = arr.get(0)
    for i in range(1,arr.length()):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    return min, max

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------
# fizz_buzz takes a StaticArray arr, and returns a new StaticArray of the same size with numbers divisible by 3 (but not 5) replaced with fizz, numbers
# divisible by 5 (but not 3) with buzz, and numbers divisible by 3 and 5 with fizzbuzz, and numbers not divisible by either are unchanged.
def fizz_buzz(arr: StaticArray) -> StaticArray:
    returnArray = StaticArray(arr.length())
    for i in range(arr.length()):
        if arr[i] % 3 == 0 and arr[i] % 5 != 0:
            returnArray.set(i, 'fizz')
        elif arr[i] % 5 == 0 and arr[i] % 3 != 0:
            returnArray.set(i, 'buzz')
        elif arr[i] % 5 == 0 and arr[i] % 3 == 0:
            returnArray.set(i, 'fizzbuzz')
        else:
            returnArray.set(i, arr[i])
    return returnArray

# ------------------- PROBLEM 3 - REVERSE -----------------------------------
# reverse takes a StaticArray arr and reverses the order of the elements using tuple assignment. It does not return anything.
def reverse(arr: StaticArray) -> None:
    for i in range(arr.length()//2):
        arr[i], arr[arr.length()-1-i] = arr[arr.length()-1-i], arr[i]

    

# ------------------- PROBLEM 4 - ROTATE ------------------------------------
# rorate takes a StaticArray arr and an int steps and returns a new StaticArray with the elements of arr shifted by steps.
def rotate(arr: StaticArray, steps: int) -> StaticArray:
    returnArray = StaticArray(arr.length())
    for i in range(arr.length()):
        if i + steps >= 0 and i + steps < arr.length():
            returnArray[i+steps] = arr[i]
        elif i + steps < 0:
            returnArray[((steps+i)%arr.length())] = arr[i]
        elif i + steps >= arr.length():
            returnArray[((i+steps)%arr.length())] = arr[i]
    return returnArray

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------
# sa_range takes two ints, start and end, and returns a new StaticArray with all of the consecutive integers between start and end.
def sa_range(start: int, end: int) -> StaticArray:
    returnArray = StaticArray(abs(end-start)+1)
    if end >= start:
        for int in range(start, end+1):
            returnArray[abs(int-start)] = int
    else:
        for int in range(start, end-1, -1):
            returnArray[abs(int-start)] = int
    return returnArray

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------
# is_sorted takes a StaticArray arr and returns 1 if arr is sorted in ascending order, -1 if arr is sorted in descending order, or 0 in any other case.
def is_sorted(arr: StaticArray) -> int:
    tally = 0
    for i in range(arr.length()-1):
        if arr[i] < arr[i+1]:
            tally += 1
        elif arr[i] > arr[i+1]:
            tally -= 1
    if abs(tally) == arr.length()-1 and tally >= 0:
        return 1
    elif abs(tally) == arr.length()-1 and tally < 0:
        return -1
    else:
        return 0

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------
# find_mode takes a StaticArray arr and returns a tuple of the most common element of arr combined with the number of occurences. 
def find_mode(arr: StaticArray) -> tuple:
    mode = arr[0], 1
    count = 1
    for i in range(arr.length()-1):
        if arr[i] == arr[i+1]:
            count += 1
            if i == arr.length()-2:
                if count > mode[1]:
                    mode = arr[i], count
        elif arr[i] != arr[i+1]:
            if count > mode[1]:
                mode = arr[i], count
            count = 1
    return mode


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------
# remove_duplicates takes a StaticArray arr and returns a new StaticArray that has all nonrepeating elements of arr.
def remove_duplicates(arr: StaticArray) -> StaticArray:
    sizeOfReturnArray = arr.length()
    for i in range(arr.length()-1):
        if arr[i] == arr[i+1]:
            sizeOfReturnArray -= 1
    returnArray = StaticArray(sizeOfReturnArray)
    count = 0
    for i in range(arr.length()-1):
        if arr[i] != arr[i+1]:
            returnArray[count] = arr[i]
            count += 1
    # Adding last element of arr to returnArray because this element never gets indexed as arr[i] so it does not go through the != comparison.
    returnArray[sizeOfReturnArray-1] = arr[arr.length()-1]
    return returnArray

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------
# count_sort takes a StaticArray arr and returns a new StaticArray with the same elements as arr, but in non-ascending order.
def count_sort(arr: StaticArray) -> StaticArray:
    minimum_maximum = min_max(arr)
    rangeOfarr = minimum_maximum[1] - minimum_maximum[0]
    countingArray = StaticArray(rangeOfarr+1)
    #Inputting counts into countingArray.
    for i in range(arr.length()):
            if countingArray[arr[i] - minimum_maximum[0]] == None:
                countingArray[arr[i] - minimum_maximum[0]] = 1
            else:
                countingArray[arr[i] - minimum_maximum[0]] += 1
    returnArray = StaticArray(arr.length())
    #Looping through the countingArray backwards, using j as the number of times an integer appears to add that integer j times to the returnArray.
    k = 0
    for i in range(countingArray.length()-1, -1, -1):
        j = countingArray[i]
        if j != None:
            while j > 0:
                returnArray[k] = i + minimum_maximum[0]
                k += 1
                j -= 1
    return returnArray

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------
# sorted_squares takes a StaticArray arr and returns a new StaticArray with the squares of each element of arr sorted in non-descending order.
def sorted_squares(arr: StaticArray) -> StaticArray:
    returnArray = StaticArray(arr.length())
    i = 0
    j = arr.length() - 1
    k = arr.length() - 1
    while i <= j:
        if abs(arr[i]) >= abs(arr[j]):
            returnArray[k] = (arr[i])**2
            k -= 1
            i += 1
        elif abs(arr[i]) < abs(arr[j]):
            returnArray[k] = (arr[j])**2
            k -= 1
            j -= 1
    
    return returnArray


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    print(f"Min: {result[0]: 3}, Max: {result[1]: 3}")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    print(f"Min: {result[0]}, Max: {result[1]}")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        print(f"Min: {result[0]: 3}, Max: {result[1]}")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        mode, frequency = find_mode(arr)
        print(f"{arr}\nMode: {mode}, Frequency: {frequency}\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
