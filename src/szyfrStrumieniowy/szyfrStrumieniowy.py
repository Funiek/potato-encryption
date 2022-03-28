#!/usr/bin/python3
#import strumieniowyCiagLosowy.streamRandom as sr

import binascii


def generate_stream(l: int, init_array: list, polynomial: list):
    ret = []
    # polynomial.reverse()
    for i in range(l):
        print(f"i {i}")
        print(f"init_array {init_array}")
        ret.append(init_array[-1])
        new_bit = 0  # init_array[-1]  # możliwe wykorzystanie init_array[-2]
        print(f"  init_array[-1] {init_array[-1]}")
        for y in polynomial:
            print(f"    y {y}")
            print(f"    init_array[y] {init_array[y]}")
            print(f"    new_bit {new_bit}")
            print(
                f"    new_bit = xor(init_array[y], new_bit) {xor(init_array[y], new_bit)}")

            new_bit = xor(init_array[y], new_bit)
        print(
            f"  [new_bit, ] + init_array[:-1] {[new_bit, ] + init_array[:-1]}")

        init_array = [new_bit, ] + init_array[:-1]

    return ret


def xor(a, b):
    ret = 0
    if bool(a) != bool(b):
        ret = 1
    return ret

###############################################


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


def encrypt_decrypt(message: str, lfsr_array: list, do_encrypt=True):

    ret = ''
    ret_word = ''
    j = 0

    if(do_encrypt == True):

        # convert message to bin format
        message_bin = ' '.join(format(ord(x), 'b') for x in message)
        print('message_bin', message_bin)
        for i in message_bin:
            if(i != ' '):

                Ci = xor(int(i), lfsr_array[j])
                ret += str(Ci)
                j += 1
                if(j == len(lfsr_array)):
                    j = 0
            else:
                ret += str(' ')
    else:
        for i in message:
            if(i != ' '):
                Ci = xor(int(i), lfsr_array[j])
                ret += str(Ci)
                j += 1
                if(j == len(lfsr_array)):
                    j = 0
            else:
                ret += str(' ')

        ret_word = bin_to_letters(ret)

    return ret, ret_word



temp = [0, 1, 0, 1, 1, 1]
lfsr_array = generate_stream(8, temp, [1, 3])
#value #lfsr_array #flaga-1encrypt-0decrypt
encrypted_msg, encrypted_msg_word = encrypt_decrypt("Hello", lfsr_array, 1)
print('encrypted_msg: ', encrypted_msg)
decrypted_msg, decrypted_msg_word = encrypt_decrypt(encrypted_msg, lfsr_array, 0)
print('decrypted_msg: ', decrypted_msg, ' word: ', decrypted_msg_word)
