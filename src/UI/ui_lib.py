from glob import glob
import os
import tkinter as tk
from tkinter import BOTTOM, CENTER, LEFT, N, NW, RIGHT, TOP, Canvas, filedialog, Text
import fence.fence_lib as fl
import matrix_transformations.matrix_transformations_lib as mt
import matrix2d.matrixCipher as mc

# Definiowanie typu enkrypcji do wybrania
encryption_type = None

# Funkcja inicjalizacji okienka aplikacji przyjmująca wysokość -> w i szerokość -> h
def init_window(w:int,h:int):
    # Funkcja w której wykonywany jest algorytm i wywoływane jest okno z wynikiem
    def perform_algorithm():
        # Przypisanie wejścia tekstu do enkrypcji do zmiennej
        INPUT_DATA = input.get("1.0", "end-1c")
        # Przypisanie klucza do zmiennej
        KEY_DATA = key.get("1.0", "end-1c")
        # Przygotowanie zmiennej na wynik
        res = ''

        # Jeżeli została wybrana wersja 'fence' to wykonaj algorytm ekrypcji Rail Fence
        if encryption_type == 'fence':
            res = fl.encrypt(INPUT_DATA, KEY_DATA)
        # Jeżeli została wybrana wersja 'matrix_transformations' to wykonaj algorytm ekrypcji Przestawienia Macierzowe z przykładu A
        elif encryption_type == 'matrix_transformations':
            res = mt.encrypt_decrypt(INPUT_DATA, KEY_DATA)
        # Jeżeli została wybrana wersja 'matrix_transformations' to wykonaj algorytm ekrypcji Przestawienia Macierzowe z przykładu B
        else:
            res = mc.encrypt(INPUT_DATA, KEY_DATA)
        # Pokaż okno z wynikiem
        popup_window(res)
    
    # Funkcja do wywołania okna typu popup z wynikiem enkrypcji
    def popup_window(result):
        # Funkcja wykonująca dekrypcję i zamieniająca tekst popupu na wynik dekrypcji
        def perform_decryption():
            # Przypisanie wejścia tekstu do enkrypcji do zmiennej
            INPUT_DATA = label.cget("text")
            # Przypisanie klucza do zmiennej
            KEY_DATA = key.get("1.0", "end-1c")
            # Jeżeli została wybrana wersja 'fence' to wykonaj algorytm dekrypcji Rail Fence
            if encryption_type == 'fence':
                res = fl.decrypt(INPUT_DATA, KEY_DATA)
            # Jeżeli została wybrana wersja 'matrix_transformations' to wykonaj algorytm dekrypcji Przestawienia Macierzowe z przykładu A
            elif encryption_type == 'matrix_transformations':
                res = mt.encrypt_decrypt(INPUT_DATA, KEY_DATA)
            # Jeżeli została wybrana wersja 'matrix_transformations' to wykonaj algorytm dekrypcji Przestawienia Macierzowe z przykładu B
            else:
                res = mc.decrypt(INPUT_DATA, KEY_DATA)
            # Podmiana tekstu zawierającego enkrypcję na dekrypcję
            label.config(text=str(res))

        # Deklaracja okna typu popup
        window = tk.Toplevel()

        # Deklaracja etykiety "Output"
        label = tk.Label(window, text="Output")
        # Konfiguracjia wyglądu etykiety
        # Odstępy horyzontalne:50 jednostek, odstępy wertykalne: 5 jednostek
        label.pack(fill='x', padx=50, pady=5)

        # Deklaracja etykiety wyniku enkrypcji
        label = tk.Label(window, text=str(result))
        # Konfiguracjia wyglądu etykiety
        # Odstępy horyzontalne:50 jednostek, odstępy wertykalne: 5 jednostek
        label.pack(fill='x', padx=50, pady=5)

        # Deklaracja przycisku o nazwie "Decrypt" wykonującej po kliknięciu funkcję dekryptującą
        decrypt_button = tk.Button(window, text="Decrypt", command=lambda:perform_decryption())
        decrypt_button.pack(fill='x')

        # Przycisk zamykający okno po kliknięciu
        close_button = tk.Button(window, text="Close", command=window.destroy)
        close_button.pack(fill='x')

    # Wybór algorytmu Rail Fence
    def switch_fence():
        # Sięgamy po zmienną globalną
        global encryption_type
        # Nadajemy encryption_type alias algorytmu w celu późniejszego wyboru do enkcrpcji i dekrypcji
        encryption_type='fence'
        # Odblokowanie przycisku do enkrypcji
        submit_button["state"] = "normal"

    # Wybór algorytmu Przestawienia Macierzowe z przykładu A
    def switch_matrix_transformations():
        # Sięgamy po zmienną globalną
        global encryption_type
        # Nadajemy encryption_type alias algorytmu w celu późniejszego wyboru do enkcrpcji i dekrypcji
        encryption_type='matrix_transformations'
        # Odblokowanie przycisku do enkrypcji
        submit_button["state"] = "normal"

    # Wybór algorytmu Przestawienia Macierzowe z przykładu B
    def switch_matrix_cipher():
        # Sięgamy po zmienną globalną
        global encryption_type
        # Nadajemy encryption_type alias algorytmu w celu późniejszego wyboru do enkcrpcji i dekrypcji
        encryption_type='matrix_cipher'
        # Odblokowanie przycisku do enkrypcji
        submit_button["state"] = "normal"

    # Deklaracja głównego okna aplikacji
    root = tk.Tk()
    # Nadanie tytułu okna
    root.title("Potato Encryption")
    # Nadanie wstępnych rozmiarów okna
    root.geometry(str(w)+"x"+str(h))
    
    # Ustalenie męskiego łososiowego tła naszej aplikacji
    canvas = tk.Canvas(root, width=w, height=h, bg="#f9e8e9")
    canvas.pack()
    
    # Deklaracja ramki na główną treść aplikacji
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    
    # Deklaracja ramki na przyciski do wyboru typu enkrypcji
    buttons_frame = tk.Frame(frame, bg="#ffffff")
    buttons_frame.pack(side = TOP,pady=(10,0))
    
    # Deklaracja przycisku wybierającego algorytm Rail Fence
    fence_button = tk.Button(buttons_frame, text="Rail Fence", command=switch_fence)
    fence_button.pack(
        side = LEFT,
        ipadx=5,
        ipady=5,
        padx=(10,10),
        pady=(0,10)
    )
    
    # Deklaracja przycisku wybierającego algorytm Przestawienia Macierzowe z przykładu A
    matrix_trans_button = tk.Button(buttons_frame, text="Matrix Transformation", command=switch_matrix_transformations)
    matrix_trans_button.pack(
        side = LEFT,
        ipadx=5,
        ipady=5,
        padx=(10,10),
        pady=(0,10)
    )
    
    # Deklaracja przycisku wybierającego algorytm Przestawienia Macierzowe z przykładu B
    matrix_cipher_button = tk.Button(buttons_frame, text="Matrix Cipher", command=switch_matrix_cipher)
    matrix_cipher_button.pack(
        side = LEFT,
        ipadx=5,
        ipady=5,
        padx=(10,10),
        pady=(0,10)
    )
    
    # Ramka na pola do wypełnienia
    content_frame = tk.Frame(frame, bg="#ffffff")
    content_frame.pack(
        side=TOP
        )
    # Deklaracja etykieta dla pola na tekst do enkrypcji
    input_label = tk.Label(content_frame, text = "Input")
    input_label.pack(
        side=TOP,
        ipadx=5,
        ipady=5,
        pady=(10,10)
        )
    # Pole na tekst do enkrypcji
    input = tk.Text(content_frame,  height = 1, width = 32)
    input.pack(side=TOP)
    # Deklaracja etykieta dla pola na klucz do enkrypcji
    key_label = tk.Label(content_frame, text = "Key (x-y-z...)")
    key_label.pack(
        side=TOP,
        ipadx=5,
        ipady=5,
        pady=(10,10)
        )
    # Pole na klucz do enkrypcji
    key = tk.Text(content_frame, height = 1, width = 16)
    key.pack(side=TOP)
    
    # Ramka na przyciski zaczynający enkrypcję i wyjście z programu
    actions_frame = tk.Frame(frame, bg="#ffffff")
    actions_frame.pack(side=BOTTOM, anchor= tk.SE,pady=(0,10))
    
    # Deklaracja przycisku zaczynający algorytm enkrypcji
    submit_button = tk.Button(actions_frame, text="Encrypt", command=lambda:perform_algorithm())
    submit_button.pack(
        side = RIGHT,
        ipadx=5,
        ipady=5,
        padx=(10,10),
        pady=(0,10),
        expand=True
    )
    # Zablokowanie do kliknięcia przycisku do enkrypcji
    submit_button["state"] = "disabled"
    
    # Deklaracja przycisku wyjścia z programu
    exit_button = tk.Button(actions_frame, text="Exit", command=root.destroy)
    exit_button.pack(
        side = RIGHT,
        ipadx=5,
        ipady=5,
        padx=(10,10),
        pady=(0,10),
        expand=True
    )
    # Pętla do działania aplikacji okienkowej
    root.mainloop()