


def sol():

     a = int(input())
     b = int(input())
     c = int(input())
     d = str(a*b*c)

     answer = []
     cnt = 0


     for i in range(len(d)):
         if d[i] == '0':
             cnt += 1

     answer.append(cnt)
     cnt = 0

     for i in range(len(d)):
         if d[i] == '1':
             cnt += 1

     answer.append(cnt)
     cnt = 0

     for i in range(len(d)):
         if d[i] == '2':
             cnt += 1

     answer.append(cnt)
     cnt = 0

     for i in range(len(d)):
         if d[i] == '3':
             cnt += 1

     answer.append(cnt)
     cnt = 0

     for i in range(len(d)):
         if d[i] == '4':
             cnt += 1

     answer.append(cnt)
     cnt = 0

     for i in range(len(d)):
         if d[i] == '5':
             cnt += 1

     answer.append(cnt)
     cnt = 0

     for i in range(len(d)):
         if d[i] == '6':
             cnt += 1

     answer.append(cnt)
     cnt = 0

     for i in range(len(d)):
         if d[i] == '7':
             cnt += 1

     answer.append(cnt)
     cnt = 0

     for i in range(len(d)):
         if d[i] == '8':
             cnt += 1

     answer.append(cnt)
     cnt = 0

     for i in range(len(d)):
         if d[i] == '9':
             cnt += 1

     answer.append(cnt)
     cnt = 0


     for i in answer:
         print(i)
     # print(answer)
sol()