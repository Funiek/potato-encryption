#!/usr/bin/python3
"""
Główna funckja do szyfrowania danych
"""
def encrypt(value: str, key: str):
    # Pobranie tablicy generowanej na podstawie klucza zawierającej
    #  w każdym polu kolejny indeks poziomu
    a = getHelperArray(value, key)

    ret = []
    # Iteracja po poziomach
    for ii in range(1, int(key) + 1):
        # iteracja po tekście jawnym
        for i, v in enumerate(value):
            # gdy poziom jest równy z wartością przypisaną w tablicy pomocniczej
            #  dodawany jest znak do szyfrogramu
            if a[i] == ii:
                ret.append(v)
    # zapisanie wyniku w postaci ciągu znaków z tablicy
    return ''.join(ret)


def decrypt(value: str, key: str):
    # Pobranie tablicy pomocniczej zawierającej indeksy poziomów dla liter
    #  tekstu szyfrowanego na podstawie klucza
    a = getHelperArray(value, key)
    # ustawienie początkowych wartości zmiennym
    message = [''] * len(a)
    bufor_pointer = 0

    # iteracja po wartościach poziomów szyfru na podstawie klucza
    for k in range(1, int(key) + 1):
        # Iteracja po literach szyfrogramu
        for i in range(0, len(value)):
            # jeżeli wartości poziomów się zgadzają zapisywana jest litera w wiadomosci
            if k == a[i]:
                message[i] = value[bufor_pointer]
                bufor_pointer += 1
    # przekształcenie wyniku do postaci końcowej
    return ''.join(message)


def getHelperArray(value: str, key: str):
    a = [0] * len(value)
    zwrot = -1
    for i, v in enumerate(value):
        if i == 0:
            a[i] = 1
            continue
        if zwrot == -1:
            a[i] = a[i - 1] + 1
        else:
            a[i] = a[i - 1] - 1
        if a[i] == int(key) or a[i] == 1:
            zwrot = (-1) * zwrot
    return a


if __name__ == "__main__":
    import sys

    print(decrypt(encrypt(sys.argv[1], sys.argv[2]), sys.argv[2]))
