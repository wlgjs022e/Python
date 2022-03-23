def solve():

    a = int(input())
    temp = a
    cnt = 0


    while(True):

        if temp % 5 == 0:
            cnt += (temp//5)

            break

        temp -= 3
        cnt += 1

        if temp < 0:
            cnt = -1
            break
    print(cnt)
solve()