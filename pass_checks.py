#!/usr/bin/ python3

"""This is a simple script that passes PEP8 checks"""


def find_outlier(integers):
    """This function iterates through the given list of numbers,
       finds the odd and even numbers and returns the only different number
       eg in [0, 2, 4, 5] returns 5 [1,3,5,7,10] returns 10 """
    even, odd = [], []
    for number in integers:
        if number % 2 == 0:
            even.append(number)
        elif number % 2 != 0:
            odd.append(number)
    # since the list can only have one odd or even number the new lists will \
    # always have one with less numbers than the other.
    if len(even) < len(odd):
        return even[0:]
    elif len(even) == len(odd):
        return integers  # you can add the two lists,
        # sort them then return the sorted list
    else:
        return odd[0:]


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  # this will the same list since
print(find_outlier(nums))
