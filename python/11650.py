import sys

def solve():

    a = int(sys.stdin.readline())
    answer = []
    cnt = 0

    for i in range(a):
        b = list(map(int,sys.stdin.readline().split()))
        answer.append(b)

    answer.sort()
    for i in answer:

        print(i[0],i[1])
solve()