def solve():


    a = int(input())
    cnt = 0

    for i in range(1,a+1):

        num_list = list(map(int, str(i)))

        if i < 100:
            cnt += 1
        elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            cnt += 1
            num_list.clear()

    print(cnt)
solve()