def solve():

    a = list(input())
    b = len(a)
    answer = []
    temp = ""
    for i in range(1,len(a)+1):
        if a[b-i] != " ":
            temp += a[b-i]

        if len(temp) == 3:
            answer.append(temp)
            temp = ""

    print(max(answer))
solve()