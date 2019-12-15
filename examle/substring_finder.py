from itertools import combinations


def sub_string_finder(string):
    substring_of = [string.upper()[i:j] for i, j in combinations(range(len(string) + 1), r=2)]
    return substring_of


s = input("Enter a string: ")
print(f"Number of substring: {len(sub_string_finder(s))}")
print(sub_string_finder(s))
