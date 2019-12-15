def sub_string_finder(string):
    given_string = string.upper()
    substring_of = []
    length = len(given_string)
    # find all substring and put it in substring array
    for i in range(length):
        for j in range(i + 1, length + 1):
            substring_of.append(given_string[i:j])
    return substring_of


s = input("Enter a string: ")
print(f"Number of substring: {len(sub_string_finder(s))}")
print(sub_string_finder(s))