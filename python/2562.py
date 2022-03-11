def sol():
    answer = []
    cnt = 0
    while True:
        a = int(input())

        answer.append(a)
        b = max(answer)

        if len(answer) == 9:
            break

    for i in range(len(answer)):
        cnt += 1
        if b == answer[i]:
            break

    print(b)
    print(cnt)


sol()