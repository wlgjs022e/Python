def solve():

    a = int(input())
    temp = a
    cnt = 1
    num1 = 0
    num2 = 1
    while(True):

        if a == 0:
            print(0)
            break
        elif a == 1:
            print(1)
            break

        num1 += num2
        cnt += 1
        if (cnt == temp and cnt % 2 == 0):
            print(num1)  
            break

        num2 += num1
        cnt += 1
        if (cnt == temp and cnt % 2 != 0):
            print(num2)
            break

solve()