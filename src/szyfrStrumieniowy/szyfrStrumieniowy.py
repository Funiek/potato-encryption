#!/usr/bin/python3

import repackage

repackage.up()

from strumieniowyCiagLosowy.streamRandom import *

import binascii


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


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


def encrypt_decrypt(message: str, init_array: list, polynomial: list, do_encrypt=True):
    ret = ''
    ret_word = ''
    
    lfsr_length = 1
    random_stream, lfsr_array = generate_stream(lfsr_length, init_array, polynomial)

    if do_encrypt:

        # convert message to bin format
        message_bin = ' '.join(format(ord(x), 'b') for x in message)
        print('message_bin', message_bin)
        for i in message_bin:
            if i != ' ':

                Ci = xor(int(i), random_stream[lfsr_length - 1])
                ret += str(Ci)

                lfsr_length += 1
                random_stream, lfsr_array = generate_stream(lfsr_length, lfsr_array, polynomial)

            else:
                ret += str(' ')

        ret_word = bin_to_letters(ret)
    else:
        for i in message:
            if i != ' ':
                Ci = xor(int(i), random_stream[lfsr_length - 1])
                ret += str(Ci)


                lfsr_length += 1
                random_stream, lfsr_array = generate_stream(lfsr_length, lfsr_array, polynomial)

            else:
                ret += str(' ')

        ret_word = bin_to_letters(ret)

    return ret, ret_word


if __name__ == '__main__':
    temp = [0, 1, 0, 1, 1, 1]
    lfsr_array = generate_stream(8, temp, [1, 3])
    # value #lfsr_array #flaga-1encrypt-0decrypt
    encrypted_msg, encrypted_msg_word = encrypt_decrypt("Hello", temp, [1, 3], 1)
    print('encrypted_msg: ', encrypted_msg, 'word: ', encrypted_msg_word)
    decrypted_msg, decrypted_msg_word = encrypt_decrypt(encrypted_msg, temp, [1, 3], 0)
    print('decrypted_msg: ', decrypted_msg, ' word: ', decrypted_msg_word)
