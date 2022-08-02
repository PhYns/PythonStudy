# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

# None of the arrays will be empty, so you don't have to worry about that!
from unittest import TestCase as test
my_list = ["Um","Dois","Tres"]

def remove_every_other(my_list):
     elementsToRemove = [my_list[i] for i in range(1, len(my_list), 2)]
     for element in elementsToRemove: my_list.remove(element)
     return(my_list)

remove_every_other(my_list)
print(my_list)

test.assertEquals(remove_every_other(first=['Hello', 'Goodbye', 'Hello Again']),second=['Hello', 'Hello Again'])
test.assertEquals(remove_every_other(first=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),second=[1, 3, 5, 7, 9])
test.assertEquals(remove_every_other(first=[[1, 2]]), second=[[1, 2]])
test.assertEquals(remove_every_other(first=[['Goodbye'], {'Great': 'Job'}]), second=[['Goodbye']])