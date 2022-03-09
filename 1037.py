


def sol():
    T = int(input())
    answer = []

    data = list(map(int,input().split()))
    answer.append(data)

    answer = sum(answer,[])
    l = max(answer)
    u = min(answer)
    number = (l*u)
    print(number)

sol()