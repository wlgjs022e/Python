


def solve():

    a = int(input())
    cnt = 0
    temp = []
    answer = []


    for i in range(a):
        c = list(map(int,input().split()))
        temp.append(c)


    for i in range(a):
        cnt = 1
        for j in range(a):
            if temp[i][0] < temp[j][0] and temp[i][1] < temp[j][1]:
                cnt += 1
        answer.append(cnt)
    for i in answer:
        print(i,end=" ")



solve()