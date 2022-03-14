def solve():
    a = input()
    num = ['0','1','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
    # 3~ 10 초 소요
    answer = []
    cnt1 =0
    for i in range(len(a)):
        for j in num:
            if a[i] in j:
                cnt = num.index(j)
                answer.append(cnt)
    for i in answer:
        cnt1 += (i+1)

    print(cnt1)
solve()