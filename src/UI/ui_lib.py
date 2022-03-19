import os
import tkinter as tk
from tkinter import BOTTOM, CENTER, LEFT, N, NW, RIGHT, TOP, Canvas, filedialog, Text



def init_window(w:int,h:int):
    def perform_fence():
        INPUT_DATA = input.get("1.0", "end-1c")
        KEY_DATA = key.get("1.0", "end-1c")
    
    def perform_matrix_transformations():
        INPUT_DATA = input.get("1.0", "end-1c")
        KEY_DATA = key.get("1.0", "end-1c")
    
    def perform_matrix_cipher():
        INPUT_DATA = input.get("1.0", "end-1c")
        KEY_DATA = key.get("1.0", "end-1c")
    
    def call_back():
        popup_window()
    
    def popup_window():
        window = tk.Toplevel()

        label = tk.Label(window, text="Output")
        label.pack(fill='x', padx=50, pady=5)

        label = tk.Label(window, text="1234")
        label.pack(fill='x', padx=50, pady=5)

        button_close = tk.Button(window, text="Close", command=window.destroy)
        button_close.pack(fill='x')

    root = tk.Tk()
    root.title("Potato Encryption")
    root.geometry(str(w)+"x"+str(h))
    
    canvas = tk.Canvas(root, width=w, height=h, bg="#f9e8e9")
    canvas.pack()
    
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    
    buttons_frame = tk.Frame(frame, bg="#ffffff")
    buttons_frame.pack(side = TOP,pady=(10,0))
    
    fence_button = tk.Button(buttons_frame, text="Rail Fence", command=call_back)
    fence_button.pack(
        side = LEFT,
        ipadx=5,
        ipady=5,
        padx=(10,10),
        pady=(0,10)
    )
    
    matrix_trans_button = tk.Button(buttons_frame, text="Matrix Transformation", command=call_back)
    matrix_trans_button.pack(
        side = LEFT,
        ipadx=5,
        ipady=5,
        padx=(10,10),
        pady=(0,10)
    )
    
    matrix_cipher_button = tk.Button(buttons_frame, text="Matrix Cipher", command=call_back)
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
    submit_button = tk.Button(actions_frame, text="Encrypt", command=lambda:take_input())
    submit_button.pack(
        side = RIGHT,
        ipadx=5,
        ipady=5,
        padx=(10,10),
        pady=(0,10),
        expand=True
    )
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