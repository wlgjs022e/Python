import sys

def solve():

    a = int(sys.stdin.readline())
    answer = []
    temp = []
    cnt = 0

    for i in range(a):
        x,y = map(int,sys.stdin.readline().split())
        answer.append([y,x])

    answer.sort()

    for i in answer:
        print(i[1],i[0])
solve()