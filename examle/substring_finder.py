def sub_string_finder(string):
    substring_of = [string.upper()[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]
    return substring_of


s = input("Enter a string: ")
print(f"Number of substring: {len(sub_string_finder(s))}")
print(sub_string_finder(s))