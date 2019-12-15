#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.


def solve(s):
    sen = s.split(sep=" ")
    print(sen)
    result = ''
    for i in sen:
        if re.findall(r'\d', i):
            result += i + " "
        elif i == " ":
            result += i
        else:
            result += i.title() + " "
    result = result[:-1]
    return result

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PAT'], 'w')
#
#     s = input()
#
#     result = solve(s)
#
#     fptr.write(result + '\n')
#
#     fptr.close()

s = input()


print(solve(s))

