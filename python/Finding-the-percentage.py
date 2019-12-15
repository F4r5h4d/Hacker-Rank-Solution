if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    s = 0.0
    ll = student_marks[query_name]
    for i in ll:
        s += i
    print(format(s / len(ll), '.2f'))

