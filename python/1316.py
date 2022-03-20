
def solve():

    n = int(input())
    cnt = n


    for i in range(n):

        b = input()

        for j in range(0,len(b)-1):
            if b[j] == b[j+1]:
                pass
            elif b[j] in b[j+1:]:
                cnt =-1
                break

    print(cnt)
solve()
