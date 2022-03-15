import os
import tkinter as tk
from tkinter import LEFT, N, NW, TOP, Canvas, filedialog, Text

def call_back():
   print("callback")

def init_window(w:int,h:int):
    
    root = tk.Tk()
    root.title("Potato Encryption")
    
    canvas = tk.Canvas(root, width=w, height=h, bg="#f9e8e9")
    canvas.pack()
    
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    
    fence_button = tk.Button(frame, text="Rail Fence", command=call_back)
    fence_button.pack(
        anchor = NW,
        side = LEFT,
        ipadx=5,
        ipady=5,
        padx=(10,10),
        pady=(10,10),
        expand=True
    )
    
    matrix_trans_button = tk.Button(frame, text="Matrix Transformation", command=call_back)
    matrix_trans_button.pack(
        anchor = NW,
        side = LEFT,
        ipadx=5,
        ipady=5,
        padx=(10,10),
        pady=(10,10),
        expand=True
    )
    
    submit_button = tk.Button(frame, text="Encrypt", command=call_back)
    submit_button.pack(
        anchor=tk.SE,
        ipadx=5,
        ipady=5,
        padx=(10,10),
        pady=(0,10),
        expand=True
    )
    
    
    
    root.mainloop()