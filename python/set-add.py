n = int(input())
countries = []
unique = []
for i in range(n):
    countries.append(input())
for j in countries:
    if j not in unique:
        unique.append(j)
print(len(unique))

