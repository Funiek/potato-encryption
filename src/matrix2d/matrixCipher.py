#!/usr/bin/python3

"""
Metoda do enkrypcji
"""
def encrypt(message: str, key: str):
    # Pobranie tablicy przestawień
    k_array = getArrayKey(key)
    # Usunięcie znaków białych
    message = message.replace(" ", '')
    ret = []
    # Iteracja po macierzy przestawień
    for y in k_array:
        index = 1
        # Iteracja po tekście jawnym przesuwając się o długość klucza
        while index + y - 2 < len(message):
            # dodanie znaku do wyniku
            ret.append(message[index + y - 2])
            index += len(k_array)
        # Oddzielenie sekcji spacjami
        ret.append(" ")
    # Przygotowanie końcowego wyniku
    return ''.join(ret[:-1])


"""
Metoda do dekrypcji
"""
def decrypt(message: str, key: str):
    # Usunięcie znaków białych
    message = message.replace(" ", '')
    # Pobranie tablicy przestawień
    k_array = getArrayKey(key)

    result = [''] * len(message)
    i = 0
    # Iteracja po tablicy przestawień
    for y in k_array:
        index = 1
        # Iteracja po szyfrogramie iterując się po znakach oddalonych od siebie o długość klucza
        while index + y - 2 < len(message):
            # Przypisanie wyniku
            result[index + y - 2] = message[i]
            # Zwiększenie indeksów
            index += len(k_array)
            i += 1
    # Przygotowanie finalnej wersji wyniku
    return ''.join(result)

"""
Opracowanie tablicy na podstawie klucza, która będzie wzorem przestawień znaków.
"""
def getArrayKey(key: str):
    # Przygotowanie na podstawie znaków listy tupli zawierających litere i indeks
    arr = list(zip(key, list(range(1, int(len(key)) + 1))))
    # Posortowanie ciągu po znaku
    arr.sort()
    # Usunięcie znaku pozostawiając nr przestawień
    arr = [i[1] for i in arr]
    return arr


if __name__ == "__main__":
    import sys
    print(decrypt(encrypt("HERE IS A SECRET MESSAGE ENCIPHERED BY TRANSPOSITION", "CONVENIENCE"), "CONVENIENCE"))
