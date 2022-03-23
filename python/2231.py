def solve():

    a = int(input())

    for i in range(1,a+1):
        result = 0
        b = list(map(int,str(i)))
        result = i + sum(b)

        if result == a:
            print(i)
            break
        if i == a:
            print(0)
solve()