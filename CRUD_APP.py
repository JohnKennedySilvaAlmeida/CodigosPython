from tkinter import *
from tkinter.ttk import *
#import tkinter as tk
from tkinter import messagebox
#import tkinter.colorchooser #obs
import sqlite3
#from CRUD_Cep import *
from pycep_correios import *
#import tkinter


app = Tk()# inicio tela 
app.title("Jk.System") # titulo  jk 
app.geometry('1000x600+100+100') # geometria
app.configure(background='black')# cor

mprincipal = Menu(app) # menu principal 

#1
mitem = Menu(mprincipal, tearoff=0)
mitem.add_command(label="Importar")
mitem.add_command(label="Exportar")# Rotulo 
mitem.add_command(label="Sair")
#2
msobre = Menu(mprincipal, tearoff=0)
msobre.add_command(label="Help") # Rotulo 
msobre.add_command(label="Versão")
#3
mprincipal.add_cascade(label="Arquivo", menu=mitem) # menu 
mprincipal.add_cascade(label="Sobre", menu=msobre)#  |   arquivo |  Sobre    | = EX

#cadastro de clientes - Logo
titulopincipal = Label(app, text='Cadastro De Clientes')
titulopincipal.place(x=247,y=1) # Titulo da tela de clientes 
titulopincipal.config(font=('Bernard MT Condensed',19)) 
titulopincipal.config(background="Light Blue")
#SNAC 2018 CRUD
titufinal = Label(app, text='Senac - 2018 ')
titufinal.place(x=297,y=400) 
titufinal.config(font=('Bernard MT Condensed',19)) 
titufinal.config(background="Light Blue")
#creditos 
titufinal = Label(app, text='CRUD - Waldemar Roberti ')
titufinal.place(x=240,y=460) 
titufinal.config(font=('Bernard MT Condensed',19)) 
titufinal.config(background="Light Blue")
#Turma ADS
ads = Label(app, text='ADS - 2 Semestre ')
ads.place(x=280,y=520) 
ads.config(font=('Bernard MT Condensed',19)) 
ads.config(background="Light Blue")
# OBS
obs = Label(app, text=' OBS !')
obs.place(x=715,y=180.5) 
obs.config(font=('Bernard MT Condensed',12)) 
obs.config(background="Light Blue")

#4 codigo
lblcodigo  = Label(app, text="Código", background='black') #texto  com  cor --- OBS!!!
lblcodigo.place(x=20, y=40) # lugar     x   y 
lblcodigo.config(font=('Arial Black',9))# fonte do Codigo 
lblcodigo.config(foreground="Light Blue")# cor do codigo 
entcodigo = Entry(app, width=50)# Entrada  /  largura 
entcodigo.place(x=20, y=60)
#5 nome 
lblnome  = Label(app, text="Nome", background='black')
lblnome.place(x=20, y=90)
lblnome.config(font=('Arial Black',9))# fonte do nome 
lblnome.config(foreground="Light Blue")# cor do nome
entnome = Entry(app, width=50) # Entrada
entnome.place(x=20, y=110)
#6 CPF
lblcpf  = Label(app, text="CPF", background='black')
lblcpf.place(x=20, y=140)
lblcpf.config(font=('Arial Black',9))# fonte
lblcpf.config(foreground="Light Blue")# cor 
entcpf = Entry(app, width=50)  # entrada 
entcpf.place(x=20, y=160)
#7 telefone 
lbltelefone  = Label(app, text="Telefone", background='black')
lbltelefone.place(x=20, y=190)
lbltelefone.config(font=('Arial Black',9))# fonte 
lbltelefone.config(foreground="Light Blue")# cor 
enttelefone = Entry(app, width=50) #entrada 
enttelefone.place(x=20, y=210)
#8 email 
lblemail  = Label(app, text="Email", background='black')
lblemail.place(x=20, y=240)
lblemail.config(font=('Arial Black',9))# fonte
lblemail.config(foreground="Light Blue")# cor
entemail = Entry(app, width=50) # entrada 
entemail.place(x=20, y=260) # place = lugar 
#9 estado Civil 
lblestadocivil  = Label(app, text="Estado Civil", background='black')
lblestadocivil.place(x=20, y=290)
lblestadocivil.config(font=('Arial Black',9))# fonte 
lblestadocivil.config(foreground="Light Blue")# cor 
cmbestadocivil = Combobox(app, width=47)
cmbestadocivil['values'] = ['Casado','Solteiro','Amasiado','Viúvo','Separado'] # lista 
cmbestadocivil.place(x=20, y=310)
#10 CEP 
lblcep  = Label(app, text="Cep", background='black')
lblcep.place(x=400, y=40)
lblcep.config(font=('Arial Black',9))# fonte 
lblcep.config(foreground="Light Blue")# cor 
entcep = Entry(app, width=38,font=('Arial Black',9,'bold')) # entrada -> e opçãos!!!    obs !!!!!
entcep.place(x=400, y=60)

#11 rua 
lblrua  = Label(app, text="Rua", background='black')
lblrua.place(x=400, y=90)
lblrua.config(font=('Arial Black',9))# fonte 
lblrua.config(foreground="Light Blue")# cor 
entrua = Entry(app, width=50) # entrada 
entrua.place(x=400, y=110)
#entrua.config(state=DISABLED)
# 12 numero 
lblnumero  = Label(app, text="Numero", background='black')
lblnumero.place(x=720, y=90)
lblnumero.config(font=('Arial Black',9))# fonte  
lblnumero.config(foreground="Light Blue")# cor  
entnumero = Entry(app, width=10) # entrada 
entnumero.place(x=720, y=110)
# 13 complemento 
lblcomplemento  = Label(app, text="Complemento", background='black')
lblcomplemento.place(x=400, y=140)
lblcomplemento.config(font=('Arial Black',9))# fonte 
lblcomplemento.config(foreground="Light Blue")# cor
entcomplemento = Entry(app, width=50) # entrada 
entcomplemento.place(x=400, y=160)
#entcopmplemento.config(state=DISABLED)  #desabilitar funcão 
# 14 bairro 
lblbairro  = Label(app, text="Bairro", background='black')
lblbairro.place(x=400, y=190)
lblbairro.config(font=('Arial Black',9))# fonte 
lblbairro.config(foreground="Light Blue")# cor 
entbairro = Entry(app, width=50) # entrada 
entbairro.place(x=400, y=210)
#entbairro.config(state=DISABLED)
# 15 cidade 
lblcidade  = Label(app, text="Cidade", background='black')
lblcidade.place(x=400, y=240)
lblcidade.config(font=('Arial Black',9))# fonte 
lblcidade.config(foreground="Light Blue")# cor  
entcidade = Entry(app, width=50) # entrada 
entcidade.place(x=400, y=260)
#entcidade.config(state=DISABLED)
# 16 estado 
lblestado  = Label(app, text="Estado", background='black')
lblestado.place(x=400, y=240)
lblestado.config(font=('Arial Black',9))# fonte 
lblestado.config(foreground="Light Blue")# cor 
entestado = Entry(app, width=10) # entrada 
entestado.place(x=400, y=260) # lugar x y 
#entestado.config(state=DISABLED) # configurção para desabilitar 

# Funções para botoes 
def inserir(): 
    insertCliente = '''INSERT INTO clientes (NOME,CPF,NUMERO,COMPELMENTO,EMAIL,ESTADO_CIVIL)
         VALUES (?,?,?,?,?,?,?,?);'''

    parametros = (entnome.get(),
      entcpf.get(),
      enttelefone.get(),
      entcep.get(),
      entnumero.get(),
      entcomplemento.get(),
      entemail.get(),
      cmbestadocivil['values'][cmbestadocivil.current()])

    insertEndereco = '''  INSERT INTO Endereco(CEP,RUA,BAIRRO,CIDADE,ESTADO) 
                  VALUES (?,?,?,?,?);'''
    parametrosEndereco =( 
        entcep.get(),
        entrua.get(),
        entbairro.get(),
        entcidade.get(),
        entestado.get())

    conexao = sqlite3.connect('clientes.db') # DB - conexão 
    cursor = conexao.cursor()
    conexao.execute(insertCliente,parametros) # paramentro 1
    conexao.execute(insertEndereco,parametrosEndereco) # parametro 2
    conexao.commit()
    conexao.close() # fechar bd 

    limparTela() #Função 

def consultar():
    consulta = Toplevel(app)
    consulta.title('Consultas') 
    consulta.geometry('400x400')

    lblcodigo  = Label(consulta, text="Código", background='black') #texto  com  cor --- OBS!!!
    lblcodigo.place(x=20, y=40) # lugar     x   y 
    lblcodigo.config(font=('Arial Black',9))# fonte do Codigo 
    lblcodigo.config(foreground="blue")# cor do codigo 
    entcodigo = Entry(consulta, width=50)# Entrada  /  largura 
    entcodigo.place(x=20, y=60)
    #5 nome 
    lblnome  = Label(consulta, text="Nome")
    lblnome.place(x=20, y=90)
    lblnome.config(font=('Arial Black',9))# fonte do nome 
    lblnome.config(foreground="blue")# cor do nome
    entnome = Entry(consulta, width=50) # Entrada
    entnome.place(x=20, y=110)
    #6 CPF
    lblcpf  = Label(consulta, text="CPF")
    lblcpf.place(x=20, y=140)
    lblcpf.config(font=('Arial Black',9))# fonte
    lblcpf.config(foreground="blue")# cor 
    entcpf = Entry(consulta, width=50)  # entrada 
    entcpf.place(x=20, y=160)
    #7 telefone 
    lbltelefone  = Label(consulta, text="Telefone")
    lbltelefone.place(x=20, y=190)
    lbltelefone.config(font=('Arial Black',9))# fonte 
    lbltelefone.config(foreground="blue")# cor 
    enttelefone = Entry(consulta, width=50) #entrada 
    enttelefone.place(x=20, y=210)
    #8 email 
    lblemail  = Label(consulta, text="Email")
    lblemail.place(x=20, y=240)
    lblemail.config(font=('Arial Black',9))# fonte
    lblemail.config(foreground="blue")# cor
    entemail = Entry(consulta, width=50) # entrada 
    entemail.place(x=20, y=260) # place = lugar 
    #9 estado Civil 
    lblestadocivil  = Label(consulta, text="Estado Civil")
    lblestadocivil.place(x=20, y=290)
    lblestadocivil.config(font=('Arial Black',9))# fonte 
    lblestadocivil.config(foreground="blue")# cor 
    cmbestadocivil = Combobox(consulta, width=47)
    cmbestadocivil['values'] = ['Casado','Solteiro','Amasiado','Viúvo','Separado'] # lista 
    cmbestadocivil.place(x=20, y=310)
    #10 CEP 
    lblcep  = Label(consulta, text="Cep")
    lblcep.place(x=400, y=40)
    lblcep.config(font=('Arial Black',9))# fonte 
    lblcep.config(foreground="blue")# cor 
    entcep = Entry(consulta, width=38,font=('Arial Black',9,'bold')) # entrada - e opçãos!!!    obs !!!!!
    entcep.place(x=400, y=60)

    #11 rua 
    lblrua  = Label(consulta, text="Rua")
    lblrua.place(x=400, y=90)
    lblrua.config(font=('Arial Black',9))# fonte 
    lblrua.config(foreground="blue")# cor 
    entrua = Entry(consulta, width=50) # entrada 
    entrua.place(x=400, y=110)
    #entrua.config(state=DISABLED)
    # 12 numero 
    lblnumero  = Label(consulta, text="Numero")
    lblnumero.place(x=720, y=90)
    lblnumero.config(font=('Arial Black',9))# fonte  
    lblnumero.config(foreground="blue")# cor  
    entnumero = Entry(consulta, width=10) # entrada 
    entnumero.place(x=720, y=110)
    # 13 complemento 
    lblcomplemento  = Label(consulta, text="Complemento")
    lblcomplemento.place(x=400, y=140)
    lblcomplemento.config(font=('Arial Black',9))# fonte 
    lblcomplemento.config(foreground="blue")# cor
    entcomplemento = Entry(consulta, width=50) # entrada 
    entcomplemento.place(x=400, y=160)
    #entcopmplemento.config(state=DISABLED)  #desabilitar funcão 
    # 14 bairro 
    lblbairro  = Label(consulta, text="Bairro")
    lblbairro.place(x=400, y=190)
    lblbairro.config(font=('Arial Black',9))# fonte 
    lblbairro.config(foreground="blue")# cor 
    entbairro = Entry(consulta, width=50) # entrada 
    entbairro.place(x=400, y=210)
    #entbairro.config(state=DISABLED)
    # 15 cidade 
    lblcidade  = Label(consulta, text="Cidade")
    lblcidade.place(x=400, y=240)
    lblcidade.config(font=('Arial Black',9))# fonte 
    lblcidade.config(foreground="blue")# cor  
    entcidade = Entry(consulta, width=50) # entrada 
    entcidade.place(x=400, y=260)
    #entcidade.config(state=DISABLED)
    # 16 estado 
    lblestado  = Label(consulta, text="Estado")
    lblestado.place(x=400, y=240)
    lblestado.config(font=('Arial Black',9))# fonte 
    lblestado.config(foreground="blue")# cor 
    entestado = Entry(consulta, width=10) # entrada 
    entestado.place(x=400, y=260)
    
    def query():
        select = '''SELECGT NOME,CLIENTES.CEP,
          CPF,
          TELEFONE,
          NUMERO,
          COMPLEMENTO,
          EMAIL,
          ESTADO_CIVIL,
          RUA,CIDADE,ESTADO
            FROM CLIENTES,ENDERECOS
            WHERE CLIENTES.CEP = ENDERECOS.CEP
        '''

        if entnome.get()!='':
            select += f" AND NOME = '{entnome.get()}'"

        if entcodigo.get() !='':
            select += f" AND CODIGO = {entcodigo.get()}"   

        conexao = sqlite3.connect('clientes.db') # DB - conexão 
        cursor = conexao.cursor()
        conexao.execute(select) # paramentro 1
        resultado = cursor.fetchone()
        consulta.destroy()

      #  entnome.delete(0,END)
       # entnome.insert(resultado('NOME'))       # !!! obs !!!

        btnConsulta = Button(consulta,text='Consultar',command=query)
        btnConsulta.place(x=20,y=350)

    btnConsulta = Button(consulta,text='Consultar',command=consultar)
    btnConsulta.place(x=20,y=350)



def alterar(): pass 
def deletar(): pass  

def limparTela():
    mudarStatus(True)
    entbairro.delete(0,END)
    entcidade.delete(0,END)
    entestado.delete(0,END)
    entrua.delete(0,END)
    entcep.delete(0,END) 
    entcodigo.delete(0,END)
    entnome.delete(0,END)
    entcpf.delete(0,END)
    entcomplemento.delete(0,END)
    enttelefone.delete(0,END)
    cmbestadocivil.set('')
    mudarStatus(False)

def mudarStatus(habilitar):
    if habilitar == True: #verdade 
        novoEstado= NORMAL #novo estado de habilitar 
    else:
        novoEstado = DISABLED # desabilitar - estado 
    entcidade.config(state=novoEstado)
    entestado.config(state=novoEstado)
    entbairro.config(state=novoEstado)
    entrua.config(state=novoEstado)
    entcodigo.config(state=novoEstado)

def consultarCep(cep): 
    result = dict()
    try:
        mudarStatus(True) # verdade 
        result = consultar_cep(entcep.get()) # cep - função 
        entbairro.delete(0,END)
        entbairro.insert(0,result['bairro']) # bairro 
        entcidade.delete(0,END)
        entcidade.insert(0,result['cidade']) #cidade 
        entestado.delete(0,END)
        entestado.insert(0,result['uf']) # estado 
        entrua.delete(0,END)
        entrua.insert(0,result['end']) # rua 
        mudarStatus(False) # Falso
    except:
        messagebox.showerror('Error consulta Cep ... Ou Cep Inválido')
    
      
#insirindo imagem no app  !!!! obs ----------------------

foto_photo = PhotoImage(file='PY2.png')
#foto_photo.width()#largura

label_foto = Label(app,image = foto_photo)
label_foto.place(x=540,y=350)

# -------------------------------------- teste obs!!!


#botão 1
btninserir = Button(app,text='Salvar',command=inserir)
btninserir.place(x=400, y=310)
#botão 2
btnConsulta = Button(app,text='Consultar',command=consultar)
btnConsulta.place(x=475,y=310)
#botão 3 
btnAlterar = Button(app, text='Alterar',command=alterar)
btnAlterar.place(x=550,y=310)
#botão 4
btnDeletar = Button(app, text='Excluir',command=deletar)
btnDeletar.place(x=625,y=310)
# botão 5
btncep = Button(app, text='Validar',command=consultarCep) # botão -> cep - validar 
btncep.place(x=720,y=58) # posição 
# botão 6
btnlimpatela = Button(app, text='Limpar_Tela',command=limparTela) 
btnlimpatela.place(x=760,y=180) #obs !!!!!!!!!!!!




app.config(menu=mprincipal) # APP configuração /menu-Principal 

app.mainloop() #fim app 