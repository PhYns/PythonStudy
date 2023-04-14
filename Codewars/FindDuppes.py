"""
  Count the number of Duplicates
  Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string.
  The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
  Example
  "abcde" -> 0 # no characters repeats more than once
  "aabbcde" -> 2 # 'a' and 'b'
  "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
  "indivisibility" -> 1 # 'i' occurs six times
  "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
  "aA11" -> 2 # 'a' and '1'
  "ABBA" -> 2 # 'A' and 'B' each occur twice
  
  Live interview - 5 min limit
"""

def duplicates(string = ""):
    string = string.capitalize()
    count_char = dict()
    for i in string:
        if i in count_char.keys():
            count_char[i] += 1
        else:
            count_char[i] = 1

    number_dup = 0

    for value in count_char.values():
        if value > 1:
            number_dup += 1

    return number_dup

print(duplicates("ABBA"))
