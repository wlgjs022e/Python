def sol():

    a = int(input())
    for i in range(a):
        b = list(map(int,input().split()))
        c = sum(b[1:])/b[0] # 평균값
        cnt = 0
        for j in b[1:]:
            if j > c:
                cnt += 1
        d = (cnt/b[0])*100
        print(format(d,".3f"),end="%")
        print()
sol()