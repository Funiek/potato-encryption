#!/usr/bin/python3
import sys

def encrypt_decrypt(value:str,key:str):
    # Rozdzielanie klucza po myślinkach do listy
    key_arr = key.split('-')
    
    # Ilość cyfr w kluczu jako liczba kolumn
    column_count = len(key_arr)
    
    # Ilość liter w tekście przez liczbę kolumn w uzyskaniu liczby wierszy ale zaokrąglając
    temp = int(len(value)/column_count)
    # Jeżeli nie ma reszty z dzielenia znaczy że nie ma pustych dzień w macierzy
    if(len(value)/column_count%1==0):
        rows_count = temp
    # Jeżeli jest reszta znaczy że dorzucamy dodatkowy wiersz
    else:
        rows_count = temp+1


    # Deklarujemy zmienną na infinite
    inf = float('inf')
    # Deklarujemy tablicę dwuwymiarową o wymiarach column_count x rows_count i wypełniamy ją inf
    arr = [[inf for x in range(column_count)] for y in range(rows_count)]
    
    # Zmienna do wskazywania na pierwszy wiersz
    row=0
    # Zmienna do wskazywania na pierwszą kolumnę
    col=0
    # Po kolei wybieramy z wejścia pojedynczo literki...
    for x in range(len(value)):
            #  ...i wkładamy je do macierzy 
        arr[row][col] = str(value[int(x)])
        
        # Zwiększamy zmienną wskazującą na aktualną kolumnę o jeden
        col = col + 1
        # Jeżeli liczba na wskazującym elemencie będzie miała taką samą wartość jak liczba kolumn
        if col == column_count:
            # Zerujemy wartość na elemencie wskazującym
            col = 0
            # Zwiększamy zmienną wskazującą na aktualny wiesz o jeden
            row = row + 1
    
    
    # Zmienna na wynik    
    res = ''
    
    # Po kolei idziemy po każdym wierszu...
    for data_row in arr:
        # Względem klucza...
        for order in key_arr:
            # Jeżeli litera jest różna niż inf
            if str(data_row[int(order)-1]) != 'inf':
                # Dodaj do zmiennej przechowującą wynik kolejną literkę wybraną z wiersza względem klucza
                res = res + str(data_row[int(order)-1])
            
    # Zwróć wynik
    return res
