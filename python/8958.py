def sol():


    a = int(input())

    answer = []
    cnt = 0
    temp = 0
    for i in range(a):
        b = input()
        for j in range(len(b)):
            if b[j] == 'O':
                cnt += 1
                temp += cnt
            elif b[j] == 'X':
                cnt = 0

        answer.append(temp)
        temp = 0
        cnt = 0
    for i in answer:
        print(i)

sol()