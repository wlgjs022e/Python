def sol():
    a = input()
    top = a
    cnt = 0

    while True:

        if len(top) == 1:
            top = "0" + top

        answer = str(int(top[0]) + int(top[1]))
        top = top[-1] + answer[-1]
        cnt += 1
        if int(top) == int(a):
            break
    print(cnt)


sol()