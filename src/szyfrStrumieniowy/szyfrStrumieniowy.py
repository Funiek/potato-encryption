#!/usr/bin/python3

import repackage

repackage.up()

from strumieniowyCiagLosowy.streamRandom import *

import binascii


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)


def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


def bin_to_letters(str: str):
    ret = ''
    li = list(str.split(' '))

    for i in li:
        ret += text_from_bits(i)

    return ret


def encrypt(message: str, init_array: list, polynomial: list):

    message = ' '.join(format(ord(x), 'b') for x in message)
    return encrypt_decrypt(message, init_array, polynomial)


def decrypt(message: str, init_array: list, polynomial: list):
    return encrypt_decrypt(message, init_array, polynomial)


def encrypt_decrypt(message: str, init_array: list, polynomial: list):
    ret = ''

    for i in message:
        if i != ' ':
            random_stream, init_array = generate_stream(1, init_array, polynomial)
            
            Ci = xor(int(i), random_stream[-1])
            ret += str(Ci)
        else:
            ret += ' '

    ret_word = bin_to_letters(ret)

    return ret, ret_word


if __name__ == '__main__':
    temp = [0, 1, 0, 1, 1, 1, 0]
    poly = [5,6]
    # value #lfsr_array #flaga-1encrypt-0decrypt
    encrypted_msg, encrypted_msg_word = encrypt("Hello", temp, poly)
    print('encrypted_msg: ', encrypted_msg, 'word: ', encrypted_msg_word)
    decrypted_msg, decrypted_msg_word = decrypt(encrypted_msg, temp, poly)
    print('decrypted_msg: ', decrypted_msg, ' word: ', decrypted_msg_word)
