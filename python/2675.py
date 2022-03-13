def solve():

    a = int(input())
    answer = ""
    for i in range(a):
        num = list(map(str,input().split()))
        le = len(num[1])
        for j in range(le):
            temp = num[1][j]*int(num[0])
            answer += temp
            temp = ""
        print(answer)
        answer = ""

solve()