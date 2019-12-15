import math


n = int(input("Enter a number: "))

if n % 2 != 0:
    print("Weird")

elif n >= 2 and n <= 5:
        print("Not weird")

elif n >= 6 and n <= 20:
    print("Weird")
elif n > 20 and n <= 100:
    print("Not Weird")
else:
    print("Not Weird")