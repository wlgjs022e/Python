def sol():

    answer = []
    for i in range(10):
        a = int(input())
        b = a%42
        answer.append(b)

    answer = set(answer)
    print(len(answer))
sol()