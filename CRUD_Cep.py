'''from pycep_correios import *
from tkinter import messagebox

def consultarCep(cep):
    result = dict()
    try:
        result = consultar_cep(cep)
    except:
        messagebox.showerror('Error consulta Cep ... Ou Cep Inválido')
    
    return result   '''

import tkinter as tk
root = tk.Tk()

imagem = tk.PhotoImage(file="PY2.png")
w = tk.Label(root, image=imagem)
w.imagem = imagem
w.pack()

root.mainloop()
