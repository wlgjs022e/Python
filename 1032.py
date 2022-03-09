l = int(input())

answer = []
answer1 = []


for i in range(l):
    a = input()
    answer.append(a)
    if len(answer) == 1 or len(answer) == 0 :
        continue
    else:
        for i in range(1,len(answer)):
            for j in range(len(answer[0])):
                if answer[i-1][j] != answer[i][j]:
                    answer1.append('?')
                else:
                    answer1.append(answer[i-1][j])
        answer.pop(0)
        answer1 = ''.join(answer1)
        answer.append(answer1)
        answer1 = list(answer1)
        answer1.clear()
        answer.pop(0)


answer = ''.join(answer)
print(answer)