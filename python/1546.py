




def sol():

    a = int(input())
    b = list(map(int,input().split()))
    hige = max(b)
    kor = []

    for i in b:
        kor.append(i/hige*100)


    suu = sum(kor)/a
    print(suu)

sol()