
def solve():


    a = input()

    num = ["c=","c-","dz=","d-","lj","nj","s=","z="]

    for i in num:
        if i in a:
            a = a.replace(i,"*")
    print(len(a))
solve()