
def solve():

    a,b = map(int,input().split())
    c = list(map(int,input().split()))
    c.sort()
    temp = []

    for i in range(a):
        for j in range(i+1,a):
            for k in range(j+1,a):
                if c[i] + c[j] + c[k] > b:
                    continue
                else:
                    temp.append(c[i] + c[j] + c[k])
                # 0 1 2   0 1 3 0 1 4

    print(max(temp))


solve()