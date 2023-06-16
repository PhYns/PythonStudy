"""
Find the missing letter
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in
the array.

You will always get a valid array. And it will be always exactly one letter be missing. The length of the array will
always be at least 2. The array will always contain letters in only one case.

Examples:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)
"""


def find_missing_letter(chars: list):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    # Detect and treat the case
    if chars[0].islower():
        alphabet = [letter.lower() for letter in alphabet]

    # Find the letter position
    position = alphabet.index(chars[0])

    # Compare the two string sequences
    missing_letter: list = []
    for letter in chars:
        if letter != alphabet[position]:
            missing_letter.append(alphabet[position])
            while letter != alphabet[position]:
                position += 1
        position += 1
    return missing_letter


print(find_missing_letter(['a','b','c','d','f']))
