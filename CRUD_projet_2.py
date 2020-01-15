from tkinter import *
from tkinter.ttk import *

def clicar():
    l1.config(text="Clicado!")
    l2.config(text=e1.get())
    messagebox.showinfo('Mensagem', 'Agora vai!')
    messagebox.showerror('Erro!', 'Algo errado!')
    messagebox.showwarning('Atenção!', 'Muita atenção"')
    res = messagebox.askyesno('Pergunta', "Formatar?") # Utilizadas 

window = Tk()
window.title("CRUD Tkinker test")
window.geometry('800x600+200+200')

l1 = Label(master=window, text="Nome")
l1.grid(row=1, column=1, sticky=W)
l1.config(font=("Arial", 40))

l2 = Label(master=window, text="Endereco")
l2.grid(row=2, column=1, sticky=E)
l2.config(background="green")

l3 = Label(master=window, text="CEP")
l3.grid(row=1, column=2, sticky=W)
l3.config(relief=RIDGE)

l4 = Label(master=window, text="Telefone")
l4.grid(row=2, column=2, sticky=SE)
l4.config(foreground="blue")

e1 = Entry(master=window, width=30)
e1.grid(row=3, column=2)
e1.focus()
e1.config()

b1 = Button(window, text='salvar', command=clicar)
b1.grid(row=1, column=2)
b1.config(state=ACTIVE) #exemplo

marcado = BooleanVar()
marcado.set(True)

ch = Checkbutton(window, text="Correto", var=marcado)
ch.grid(row=1, column=4, padx=10)


opcao = IntVar()
opção = 1
r1 = Radiobutton(window,text='Python', value=1, 	variable=opcao)
r2 = Radiobutton(window,text='Java', value=2, 	variable=opcao)
r3 = Radiobutton(window,text='Ruby', value=3, 	variable=opcao)

r1.grid(column=5, row=1)
r2.grid(column=6, row=1)
r3.grid(column=7, row=1)

c1 = Combobox(master=window)
c1.grid(row=6, sticky=W)
c1['values'] = ('banana','laranja','melancia')
c1.current(2)

var1 = IntVar()
s1 = Spinbox(window, from_=0, to=100, width=5, 	textvariable=var1)
s1.grid(row=7)
var1.set(10)

var2 = StringVar()
s2 = Spinbox(window, values=("sim", "não"), width=5, 	textvariable=var2)
s2.grid(row=7, column=2)
var2.get()

from tkinter import messagebox


window.mainloop()