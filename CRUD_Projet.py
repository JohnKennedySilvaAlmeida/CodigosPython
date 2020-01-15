from tkinter import *
from tkinter.ttk import *

'''Janela = Tk()
Label(Janela, text=" John Kennedy ").pack()
Janela.mainloop()'''


window = Tk()#criando tk 

window.title('CRUD Tkinter') #titulo 
window.geometry('800x600+100+100') # altura,largura,direito,esquerdo            geometry = geometria 

#L 1,2,3,4.....
l1 = Label(master=window, text='Nome') #label setar : valores e textos 
l2 = Label(master=window, text='Endereço')
l3 = Label(master=window, text='Cep') # master = mestre 
l4 = Label(master=window, text='Telefone')

l1.place(x=10, y=10) #absoluta              lugar = place 
l2.place(relx=0.9, rely=0.9) #relativa

l3.pack()
l4.pack(before=l3) # antes = before

l1.grid(row=1 ,column=0) # linha e Coluna -> 1
l2.grid(row=2 ,column=1)
l3.grid(row=3 ,column=2) # grid = grade 
l4.grid(row=4)

# usar *pack  OR  *grid - obs  para linhar e centralizar campos !!!!

l1.grid(row=1, column=0, sticky=w) # linha e Coluna -> 2
l2.grid(row=2, column=0, sticky=w)
l3.grid(row=3, column=0, sticky=w)
l4.grid(row=4, column=0, sticky=w) # sticky = Pegajoso


l1.config(font=('John',40)) # configuração e fonte
l2.config(background='green') # FUNDO
l3.config(relief=RIDGE)# Alívio , BORDA , CONTORNO 
l4.config(foreground='blue') # PRIMEIRO

# E1 
e1 = Entry(master=window, width=30) # Entrada = Entry     largura =  width    master = mestre 
e1.grid(row=1, column=2)# grade/linha/coluna

e1.focus() # foco

e1.config(state=DISABLED) # configurção   /  Estado = state   /  DISABLED = desativado 

# B1
b1 = Button(window, text='Salvar', COMMAND=clicar) #botão / texto / comando 
b1.grid(row=1, column=2)

b1.config(state=ACTIVE) # estado  /  ativo 

def clicar():# função Clicar 
    l1.config(text='Clicado!!')
    l2.config(texto=e1.get()) # get = obter 

#obs!!
marcado = BooleanVar()
marcado.set(True)# definir / verdade 

ch = Checkbutton(window,text='Correto', var=marcado)# texto /  var = foi 
ch.grid(row=1, column=4, padx=10)#grade / linha / coluna / padx 

# obs !
opcao = IntVar()
opcao = 1

r1 = Radiobutton(window, text='python', value=1, variable = opcao)#texto / valor / variavel 
r2 = Radiobutton(window, text='java', value=2, variable = opcao)
r3 = Radiobutton(window, text='pascal', value=3, variable = opcao)

r1.grid(column=5,row = 1)# grade/ coluna / linha 
r2.grid(column=6,row = 1)
r3.grid(column=7,row = 1)

# C1
c1 = Combobox(master=window) # mestre 

c1.grid(row=6, sticky=W) # W / grade / linha / pegajoso 

c1['values'] = ('banana','laranja','goiaba','arroz')

c1.current(3) # atual 

c1.get() # obter 

# obs !! 
var1 = IntVar()

ss1 = Spinbox(window, from_= 0, to=100, width=5, textvariable=var1)# Spinbox = campo incremental 
ss1.grid(row=7)#grade/ linha 
var1.set(10)#definir 

var2 = IntVar()

s2 = Spinbox(window, values = (2,4,6,8,11) , width=5, textvariable=var2)#width = largura 
s2.grid(row = 7 , column = 2)
var2.set(5)





window.mainloop() # end - fim app 

