import matplotlib.pyplot as plt
import tkinter as tk

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from pandas import DataFrame

#import sqlite3
#conexao = sqlite3.connect("contagem_carboidratos\\banco_de_dados\\clientes.db")

app = Tk()
def only_number(value):
    if value.isdigit():
        return True
    elif value is "":
        return True
    else:
        return False
#cria a tela principal
app.title("Contagem de carboidratos")
app.geometry('1000x600+100+100')
#command para forçar o usuario a digitar apenas numeros
reg = app.register(only_number)
#barra de menus-parte superior
mprincipal = Menu(app)
#sobre
msobre = Menu(mprincipal, tearoff=0)
msobre.add_command(label="Help")
msobre.add_command(label="Versão")
#cascata
mprincipal.add_cascade(label="sobre",menu=msobre)

#calcula e armazena os carboidratos
def calcular_carboidrato():
    def calcular():
        #banco
        #cmbalimento
        #query para puxar o alimento 
        #if(cmbdia_refeicao=="Café da manhã")
            #insulina = (carbo/7) + correcao
        #elif(cmbdia_refeicao=="Almoço")
            #insulina = (carbo/7) + correcao
        #else:
            #insulina = (carbo/7) + correcao
        #messagebox.showinfo(f"Mensagem","Aplicar {insulina:.2f} unidades de insulina!!")
        pass
    def sair():
        btnsair.destroy()
        win.destroy()
    def combo_input():
        #c = conexao.cursor()
        #result = []
        #c = conexao.execute('select * from clientes natural join enderecos;')
        #rows = c.fetchall()
        #for row in rows:
        #    result.append(row)
        #return result
        return "feijão"
    win = Toplevel()
    win.title("Calcular carboidrato")
    win.geometry('1000x600+100+100')

    #combo alimentos
    lblalimento = Label(win, text="Alimentos")
    lblalimento.place(x=0,y=80)
    cmbalimento = Combobox(win, width=80)
    cmbalimento['values'] = combo_input()
    cmbalimento.place(x=25,y=100)
    #combo refeicao
    lblrefeição = Label(win, text="Atividade pós refeição")
    lblrefeição.place(x=0,y=130)
    cmbrefeição = Combobox(win, width=80)
    cmbrefeição['values'] = ('Leve','Moderada','Intensa')
    cmbrefeição.place(x=25,y=150)
    #combo dia_refeicao
    lbldia_refeicao = Label(win, text="Atividade pós refeição")
    lbldia_refeicao.place(x=0,y=180)
    cmbdia_refeicao = Combobox(win, width=80)
    cmbdia_refeicao['values'] = ('Café da manhã','Almoço',' Lanche/Janta')
    cmbdia_refeicao.place(x=25,y=200)

    #-----------buttons------------#
    #btn_sair
    btnsair = Button(win, text='Voltar', command=sair)
    btnsair.place(x=700,y=310)
    #btn_calcular
    btncalcular = Button(win, text='Calcular', command=calcular)
    btncalcular.place(x=950,y=310) 
#cria e mostra os dados por tempo
'''def consultar_dados():
    def sair():
        btnsair.destroy()
        win.destroy()
    
    def geraPdf():
        pass

    class Grafico:
        def __init__(self,master):
            self.master=master
            master.title("Dashboard")
            Data1 = {'Time': ['US','CA','GER','UK','FR'],
            'GDP_Per_Capita': [45000,42000,52000,49000,47000]}

            df1 = DataFrame(Data1, columns= ['Country', 'GDP_Per_Capita'])
            df1 = df1[['Country', 'GDP_Per_Capita']].groupby('Country').sum()
 
            figure1 = plt.Figure(figsize=(6,5), dpi=100)
            ax1 = figure1.add_subplot(111)
            bar1 = FigureCanvasTkAgg(figure1, master)
            bar1.show()
            df1.plot(kind='bar', legend=True, ax=ax1)
            bar1.get_tk_widget().pack(side="top", fill="both",expand=True)
            ax1.set_title('Valor da glicemia')
            


    #cria a segunda tela
    win = Toplevel()
    gui=Grafico(win)
    win.title("Gerar relatório")
    win.geometry('1000x600+100+100')

    #-----------buttons------------#
    #btn_sair
    btnsair = Button(win, text='Voltar', command=sair)
    btnsair.place(x=400,y=500)
    #btn_inserir
    btninserir = Button(win, text='Inserir', command=geraPdf())
    btninserir.place(x=600,y=500) 

    #names = ['group_a', 'group_b', 'group_c']
    #values = [1, 10, 100]

    #plt.figure(figsize=(9, 3))
    #plt.subplot(131)
    #plt.bar(names, values)

    #plt.figure(figsize=(9, 3))

    #plt.subplot(131)
    #plt.bar(names, values)
    #plt.show()
'''

#cria e insere os dados no banco de dados
def cadastrar_alimentos():
    #deleta a tabela filha
    def sair():
        btnsair.destroy()
        win.destroy()
    #insere os dados no banco de dados
    def inserir():
        try:  
            #conexao.execute(f"INSERT INTO clientes (codigo,nome,cpf,telefone,cep,numero,complemento,email,estado_civil) VALUES(NULL,'{entnome.get()}','{entcpf.get()}','{enttelefone.get()}', '{entcep.get()}', '{entnumero.get()}','{entcomplemento.get()}','{entemail.get()}','{cmbcivil.get()}');")
            #conexao.execute(f"INSERT INTO enderecos (cep,rua,bairro,cidade,estado) VALUES('{entcep.get()}','{entrua.get()}','{entbairro.get()}','{entcidade.get()}','{entestado.get()}');")
            #conexao.commit()
            #limpar()
            messagebox.showinfo("Mensagem","Alimento adicionado com sucesso!!")
        except:
            messagebox.showinfo("Mensagem","Não foi possível cadastrar um novo alimento!!")
    #cria a segunda tela
    win = Toplevel()
    win.title("Cadastro de alimentos")
    win.geometry('1000x600+100+100')
    #--------------labels-------------#
    #label carboidratos
    lblcarboidrato = Label(win, text="Carboidrato")
    lblcarboidrato.place(x=300,y=90)
    entcarboidrato = Entry(win, width=50)
    entcarboidrato.place(x=375,y=110)
    #label nome
    lblnome = Label(win, text="Nome")
    lblnome.place(x=300,y=140)
    entnome = Entry(win, width=50)
    entnome.place(x=375,y=160)
    #label porção
    lblporcao = Label(win, text="Porçao")
    lblporcao.place(x=300,y=190)
    entporcao = Entry(win, width=50)
    entporcao.place(x=375,y=210)
    entporcao.config(validate="key",validatecommand=(reg,'%P'))
    #label proteinas
    lblproteinas = Label(win, text="Proteínas")
    lblproteinas.place(x=300,y=240)
    entproteinas = Entry(win, width=50)
    entproteinas.place(x=375,y=260)
    entproteinas.config(validate="key",validatecommand=(reg,'%P'))
    #label gorduras totais
    lblgorduras_totais = Label(win, text="Gorduras totais")
    lblgorduras_totais.place(x=300,y=290)
    entgorduras_totais = Entry(win, width=50)
    entgorduras_totais.place(x=375,y=310)
    #label gorduras saturaradas
    lblgorduras_saturadas = Label(win, text="Gorduras Saturadas")
    lblgorduras_saturadas.place(x=300,y=340)
    entgorduras_saturadas = Entry(win, width=50)
    entgorduras_saturadas.place(x=375,y=360)
    #label gorduras_trans
    lblgorduras_trans = Label(win, text="Gorduras trans")
    lblgorduras_trans.place(x=300,y=390)
    entgorduras_trans = Entry(win, width=50)
    entgorduras_trans.place(x=375,y=410)
    entgorduras_trans.config(validate="key",validatecommand=(reg,'%P'))
    #label fibra_alimentar
    lblfibra_alimentar = Label(win, text="Fibra alimentar")
    lblfibra_alimentar.place(x=300,y=440)
    entfibra_alimentar = Entry(win, width=50)
    entfibra_alimentar.place(x=375,y=460)
    entfibra_alimentar.config(validate="key",validatecommand=(reg,'%P'))

    #-----------buttons------------#
    #btn_sair
    btnsair = Button(win, text='Voltar', command=sair)
    btnsair.place(x=400,y=500)
    #btn_inserir
    btninserir = Button(win, text='Inserir', command=inserir)
    btninserir.place(x=600,y=500) 

#botoes de redirecionamento
btninserir = Button(app, text='Calcular carboidrato',width=50, command=calcular_carboidrato)
btninserir.place(x=325, y=100)

btnConsulta = Button(app, text='Gerar relatório',width=50)
btnConsulta.place(x=325, y=200)

btnAlterar = Button(app, text='Cadastrar alimento',width=50, command=cadastrar_alimentos)
btnAlterar.place(x=325,y=300)


#configurar parte sobre
app.config(menu=mprincipal)
app.mainloop()