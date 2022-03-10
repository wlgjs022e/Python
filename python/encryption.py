import random


def myencrypt(data, key):
    data_en = []

    for i in range(len(data)):
        for j in range(len(key)):
            a = data[i] ^ key[j]
        data_en.append(a)
    return data_en


def mydecrypt(data_en, key):
    data_de = []

    for i in range(len(data_en)):
        for j in range(len(key)):
            a = data_en[i] ^ key[j]
        data_de.append(a)
    return data_de


def test1():
    # xor 암호
    data = [1, 3, 5, 7, 9, 5, 8, 9, 5, 3, 8, 1, 7, 6, 3, 8, 1, 3, 5, 1]
    key = [2, 7, 8, 9]

    data_en = myencrypt(data, key)
    data_de = mydecrypt(data_en, key)
    print("평문", data)
    print("암호문", data_en)
    print("복호화", data_de)


test1()