from glob import glob
import os
import tkinter as tk
from tkinter import BOTTOM, CENTER, LEFT, N, NW, RIGHT, TOP, Canvas, filedialog, Text
import fence.fence_lib as fl
import matrix_transformations.matrix_transformations_lib as mt
import matrix2d.matrixCipher as mc

encryption_type = None

def init_window(w:int,h:int):
    def perform_algorithm():
        INPUT_DATA = input.get("1.0", "end-1c")
        KEY_DATA = key.get("1.0", "end-1c")
        res = ''

        if encryption_type == 'fence':
            res = fl.encrypt(INPUT_DATA, KEY_DATA)
        elif encryption_type == 'matrix_transformations':
            res = mt.encrypt_decrypt(INPUT_DATA, KEY_DATA)
        else:
            res = mc.encrypt(INPUT_DATA, KEY_DATA)
        popup_window(res)
    
    
    def popup_window(result):
        def perform_decryption():
            INPUT_DATA = label.cget("text")
            KEY_DATA = key.get("1.0", "end-1c")
            print(INPUT_DATA+KEY_DATA)
            if encryption_type == 'fence':
                res = fl.decrypt(INPUT_DATA, KEY_DATA)
            elif encryption_type == 'matrix_transformations':
                res = mt.encrypt_decrypt(INPUT_DATA, KEY_DATA)
            else:
                res = mc.decrypt(INPUT_DATA, KEY_DATA)

            label.config(text=str(res))

        window = tk.Toplevel()

        label = tk.Label(window, text="Output")
        label.pack(fill='x', padx=50, pady=5)

        label = tk.Label(window, text=str(result))
        label.pack(fill='x', padx=50, pady=5)

        decrypt_button = tk.Button(window, text="Decrypt", command=lambda:perform_decryption())
        decrypt_button.pack(fill='x')

        close_button = tk.Button(window, text="Close", command=window.destroy)
        close_button.pack(fill='x')


    def switch_fence():
        global encryption_type
        encryption_type='fence'
        submit_button["state"] = "normal"


    def switch_matrix_transformations():
        global encryption_type
        encryption_type='matrix_transformations'
        submit_button["state"] = "normal"


    def switch_matrix_cipher():
        global encryption_type
        encryption_type='matrix_cipher'
        submit_button["state"] = "normal"

    root = tk.Tk()
    root.title("Potato Encryption")
    root.geometry(str(w)+"x"+str(h))
    
    canvas = tk.Canvas(root, width=w, height=h, bg="#f9e8e9")
    canvas.pack()
    
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    
    buttons_frame = tk.Frame(frame, bg="#ffffff")
    buttons_frame.pack(side = TOP,pady=(10,0))
    
    fence_button = tk.Button(buttons_frame, text="Rail Fence", command=switch_fence)
    fence_button.pack(
        side = LEFT,
        ipadx=5,
        ipady=5,
        padx=(10,10),
        pady=(0,10)
    )
    
    matrix_trans_button = tk.Button(buttons_frame, text="Matrix Transformation", command=switch_matrix_transformations)
    matrix_trans_button.pack(
        side = LEFT,
        ipadx=5,
        ipady=5,
        padx=(10,10),
        pady=(0,10)
    )
    
    matrix_cipher_button = tk.Button(buttons_frame, text="Matrix Cipher", command=switch_matrix_cipher)
    matrix_cipher_button.pack(
        side = LEFT,
        ipadx=5,
        ipady=5,
        padx=(10,10),
        pady=(0,10)
    )
    
    content_frame = tk.Frame(frame, bg="#ffffff")
    content_frame.pack(
        side=TOP
        )
    input_label = tk.Label(content_frame, text = "Input")
    input_label.pack(
        side=TOP,
        ipadx=5,
        ipady=5,
        pady=(10,10)
        )
    input = tk.Text(content_frame,  height = 1, width = 32)
    input.pack(side=TOP)
    key_label = tk.Label(content_frame, text = "Key (x-y-z...)")
    key_label.pack(
        side=TOP,
        ipadx=5,
        ipady=5,
        pady=(10,10)
        )
    key = tk.Text(content_frame, height = 1, width = 16)
    key.pack(side=TOP)
    
    
    actions_frame = tk.Frame(frame, bg="#ffffff")
    actions_frame.pack(side=BOTTOM, anchor= tk.SE,pady=(0,10))
    submit_button = tk.Button(actions_frame, text="Encrypt", command=lambda:perform_algorithm())
    submit_button.pack(
        side = RIGHT,
        ipadx=5,
        ipady=5,
        padx=(10,10),
        pady=(0,10),
        expand=True
    )
    submit_button["state"] = "disabled"
    exit_button = tk.Button(actions_frame, text="Exit", command=root.destroy)
    exit_button.pack(
        side = RIGHT,
        ipadx=5,
        ipady=5,
        padx=(10,10),
        pady=(0,10),
        expand=True
    )
    
    root.mainloop()