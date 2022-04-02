from fnmatch import fnmatch


def find_nth_occurrence(substring, string, occurrence=1):
    if type(substring) is not str or type(string) is not str or type(occurrence) is not int:
        return print("Wrong input")
    first = string.find(substring)
    while first >= 0 and occurrence > 1:
        first = string.find(substring, first + 1)
        occurrence -= 1
    return first


def solve(a, b):
    if type(a) is not str or type(b) is not str:
        return print("Wrong input")
    return fnmatch(b, a)


def is_palindrome(s):
    if type(s) is not str:
        return print("Wrong input")
    return s.lower() == s[::-1].lower()
