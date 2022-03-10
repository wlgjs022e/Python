import hashlib


a = '217bc03fe579cdc78f072b675b7cb2a4ef9b6a6f' # 구하고 싶은 해시값

for i in range(10000000,99999999+1):
    pw = (str(i)+'salt_for_you')
    for j in range(500):
        pw = hashlib.sha1(pw.encode()).haxdigest()
    print('process' +str(i))

    if(pw==a):
        print('falg'+str(i)+'salt_for_you')
        break
