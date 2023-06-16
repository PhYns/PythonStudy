# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

from unittest.case import TestCase


def accum(s):
    mumble_result: str = ""
    for index in range(len(s)):
        actual_letter: str = ""
        actual_letter += s[index].capitalize()
        if index > 0:
            for n in range(index):
                actual_letter += s[index].lower()
        mumble_result += actual_letter
        if index <= (len(s) - 2):
            mumble_result += "-"
    return mumble_result
