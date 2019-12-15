def merge_the_tools(string, k):
    n = len(string)
    string.s
    output = []
    j = 0
    for i in range(n // k):
        output.append(string[i:i + k])
    print(output)



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)