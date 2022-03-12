def solve():

    a = int(input())
    cnt = 0
    num_list = list(map(int, input()))
    for i in range(len(num_list)):
        cnt += num_list[i]

    print(cnt)
solve()