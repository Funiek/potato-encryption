from glob import glob
import os
import tkinter as tk
from tkinter import BOTTOM, CENTER, LEFT, N, NW, RIGHT, TOP, Canvas, filedialog, Text
from tkinter import *
from tkinter.ttk import *
import fence.fence_lib as fl
import matrix_transformations.matrix_transformations_lib as mt
import matrix2d.matrixCipher as mc

# Funkcja inicjalizacji okienka aplikacji przyjmująca wysokość -> w i szerokość -> h
def init_window(w:int,h:int):
    # Funkcja w której wykonywany jest algorytm i wywoływane jest okno z wynikiem
    def perform_encryption():
        # Przypisanie wejścia tekstu do enkrypcji do zmiennej
        INPUT_DATA = input.get("1.0", "end-1c")
        # Przypisanie klucza do zmiennej
        KEY_DATA = key.get("1.0", "end-1c")
        # Przypisanie zaznaczonego wyniku z radiobuttonów do zmiennej
        RADIOBUTTON_HANDLER = v.get()
        # Przygotowanie zmiennej na wynik
        res = ''

        # Jeżeli została wybrana wersja 'fence' to wykonaj algorytm ekrypcji Rail Fence
        if RADIOBUTTON_HANDLER == 'fence':
            res = fl.encrypt(INPUT_DATA, KEY_DATA)
        # Jeżeli została wybrana wersja 'matrix_transformations' to wykonaj algorytm ekrypcji Przestawienia Macierzowe z przykładu A
        elif RADIOBUTTON_HANDLER == 'matrix_transformations':
            res = mt.encrypt(INPUT_DATA, KEY_DATA)
        # Jeżeli została wybrana wersja 'matrix_cipher' to wykonaj algorytm ekrypcji Przestawienia Macierzowe z przykładu B
        else:
            res = mc.encrypt(INPUT_DATA, KEY_DATA)
        # Pokaż okno z wynikiem
        output.config(text = str(res))
    
    # Funkcja w której wykonywany jest algorytm i wywoływane jest okno z wynikiem 
    def perform_decryption():
        # Przypisanie wejścia tekstu do enkrypcji do zmiennej
        INPUT_DATA = input.get("1.0", "end-1c")
        # Przypisanie klucza do zmiennej
        KEY_DATA = key.get("1.0", "end-1c")
        # Przypisanie zaznaczonego wyniku z radiobuttonów do zmiennej
        RADIOBUTTON_HANDLER = v.get()
        # Przygotowanie zmiennej na wynik
        res = ''

        # Jeżeli została wybrana wersja 'fence' to wykonaj algorytm ekrypcji Rail Fence
        if RADIOBUTTON_HANDLER == 'fence':
            res = fl.decrypt(INPUT_DATA, KEY_DATA)
        # Jeżeli została wybrana wersja 'matrix_transformations' to wykonaj algorytm ekrypcji Przestawienia Macierzowe z przykładu A
        elif RADIOBUTTON_HANDLER == 'matrix_transformations':
            res = mt.decrypt(INPUT_DATA, KEY_DATA)
        # Jeżeli została wybrana wersja 'matrix_cipher' to wykonaj algorytm ekrypcji Przestawienia Macierzowe z przykładu B
        else:
            res = mc.decrypt(INPUT_DATA, KEY_DATA)
        # Pokaż okno z wynikiem
        output.config(text = str(res))
        
    
    # Wybór algorytmu Rail Fence
    def enable_buttons():
        # Sięgamy po zmienną globalną
        global encryption_type
        # Nadajemy encryption_type alias algorytmu w celu późniejszego wyboru do enkcrpcji i dekrypcji
        encryption_type='fence'
        # Odblokowanie przycisku do enkrypcji
        encrypt_button["state"] = "normal"
        # Odblokowanie przycisku do dekrypcji
        decrypt_button["state"] = "normal"


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


    v = StringVar()

    radio_buttons = {
        "Rail Fence" : "fence",
        "Matrix Transformation" : "matrix_transformations",
        "Matrix Cipher" : "matrix_cipher",
        "Random" : "stream_cipher",
        "Stream Cipher" : "stream_cipher"
    }

    for (text, value) in radio_buttons.items():
        Radiobutton(buttons_frame, text = text, variable = v,
                    value = value, command = lambda : enable_buttons()).pack(
                    fill = X,
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
    input_label = tk.Label(content_frame, text = "Input", bg="#e6e6e6")
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
    key_label = tk.Label(content_frame, text = "Key", bg="#e6e6e6")
    key_label.pack(
        side=TOP,
        ipadx=5,
        ipady=5,
        pady=(10,10)
        )
    # Pole na klucz do enkrypcji
    key = tk.Text(content_frame, height = 1, width = 16)
    key.pack(side=TOP)

    # Deklaracja etykieta dla pola na tekst do enkrypcji
    output_label = tk.Label(content_frame, text = "Output", bg="#e6e6e6")
    output_label.pack(
        side=TOP,
        ipadx=5,
        ipady=5,
        pady=(10,10)
        )
    # Pole na tekst do enkrypcji
    output = tk.Label(content_frame,  height = 1, width = 32, bg="#e6e6e6")
    output.pack(side=TOP)
    
    # Ramka na przyciski zaczynający enkrypcję i wyjście z programu
    actions_frame = tk.Frame(frame, bg="#ffffff")
    actions_frame.pack(side=BOTTOM, anchor= tk.SE,pady=(0,10))
    
    # Deklaracja przycisku zaczynający algorytm enkrypcji
    encrypt_button = tk.Button(actions_frame, text="Encrypt", command=lambda:perform_encryption())
    encrypt_button.pack(
        side = RIGHT,
        ipadx=5,
        ipady=5,
        padx=(10,10),
        pady=(0,10),
        expand=True
    )
    # Zablokowanie do kliknięcia przycisku do enkrypcji
    encrypt_button["state"] = "disabled"
    
    # Deklaracja przycisku zaczynający algorytm enkrypcji
    decrypt_button = tk.Button(actions_frame, text="Decrypt", command=lambda:perform_decryption())
    decrypt_button.pack(
        side = RIGHT,
        ipadx=5,
        ipady=5,
        padx=(10,10),
        pady=(0,10),
        expand=True
    )
    # Zablokowanie do kliknięcia przycisku do enkrypcji
    decrypt_button["state"] = "disabled"
    
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