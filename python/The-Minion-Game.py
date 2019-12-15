def minion_game(string):
    given_string = string.upper()
    vowels = ['A', 'E', 'I', 'O', 'U']

    kevin_score = 0
    stuart_score = 0

    for i in range(len(given_string)):
        if given_string[i] in vowels:
            kevin_score += (len(given_string) - i)
        else:
            stuart_score += (len(given_string) - i)

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)


