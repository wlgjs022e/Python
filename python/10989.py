import sys



def solve():


    a = int(input())
    answer = [0] * 10001

    for i in range(a):
        b = int(sys.stdin.readline())
        answer[b] = answer[b] + 1

    for i in range(10001):
        if answer[i] != 0:
            for j in range(answer[i]):
                print(i)


solve()