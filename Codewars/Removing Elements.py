# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

# None of the arrays will be empty, so you don't have to worry about that!
from unittest import TestCase as test


my_list = [False, False, True, True]

def remove_every_other(my_list):
    final_list = []
    for index in range(len(my_list)):
        if index % 2 == 0:
            final_list.append(my_list[index])
    return final_list


print(remove_every_other(my_list))

# test.assertEquals(remove_every_other(first=['Hello', 'Goodbye', 'Hello Again']), second=['Hello', 'Hello Again'])
# test.assertEquals(remove_every_other(first=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), second=[1, 3, 5, 7, 9])
# test.assertEquals(remove_every_other(first=[[1, 2]]), second=[[1, 2]])
# test.assertEquals(remove_every_other(first=[['Goodbye'], {'Great': 'Job'}]), second=[['Goodbye']])
