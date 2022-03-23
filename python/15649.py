import itertools

def solve():

    n,m = map(int,input().split())
    answer = []
    result = []
    for i in range(1,n+1):
        answer.append(i)

    result = (list(itertools.permutations(answer,m)))

    result.sort()

    for i in result:
        k = list(i)
        for j in k:
            print(j,end=" ")
        print()

solve()