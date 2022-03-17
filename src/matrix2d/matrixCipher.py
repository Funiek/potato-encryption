#!/usr/bin/python3

def encrypt(message: str, key: str):
    k_array = getArrayKey(key)
    message = message.replace(" ", '')
    n = len(k_array)
    m = (len(message) * 2 - 1) // n

    ret = []

    for y in k_array:
        index = 1
        while index + y - 2 < len(message):
            ret.append(message[index + y - 2])
            index += len(k_array)
        ret.append(" ")
    return ''.join(ret[:-1])


def decrypt(message: str, key: str):
    print(key)
    message = message.replace(" ", '')
    n = len(key)
    m = (len(message) * 2 - 1) // n
    k_array = getArrayKey(key)

    result = [''] * len(message)
    i = 0
    for y in k_array:
        index = 1
        while index + y - 2 < len(message):
            result[index + y - 2] = message[i]
            index += len(k_array)
            i += 1

    return ''.join(result)


def getArrayKey(key: str):
    arr = list(range(1, int(len(key)) + 1))
    arr = list(zip(key, arr))
    arr.sort()
    arr = [i[1] for i in arr]
    return arr


if __name__ == "__main__":
    import sys

    print(decrypt(encrypt("HERE IS A SECRET MESSAGE ENCIPHERED BY TRANSPOSITION", "CONVENIENCE"), "CONVENIENCE"))
