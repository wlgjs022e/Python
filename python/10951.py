def sol():
    answer = []
    while True:
        try:
            a,b = map(int,input().split())
            c = a+b
            answer.append(c)
        except:
            break

    for i in answer:
        print(i)
sol()