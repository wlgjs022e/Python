def sol():



    a,b = map(int,input().split())

    c = list(map(int,input().split()))



    for j in c:
        if j < b:
            print(j,end=" ")


sol()