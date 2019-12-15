def merge_the_tools(string, k):
    result = [string.upper()[i:i + k] for i in range(0, len(string), k)]
    temp_list = []
    # [temp_list.append(x) for x in string if x not in temp_list]
    for i in result:
        sum = ''
        for j in i:
            if j not in sum:
                sum += j
        temp_list.append(sum)
    result = temp_list
    for i in result:
        print(i)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
