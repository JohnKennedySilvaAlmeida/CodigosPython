class pessoa:
    
    def __init__ (self, nome, idade,uf):
        print('Eu sou o {} e tenho anos {} e moro em {}'.format(nome,idade,uf))
        self.nome = nome
        self.idade = idade   #atributos 
        self.uf = uf
    
    def muda_idade(self,idade):
        self.idade = idade

    def conversa(self):
        print(f'Estou conversando com o {self.nome}')

john = pessoa('John',25,'Sc')  #contrutor 
kennedy = pessoa('Kennedy',26,'PR')

john.muda_idade(99)

john.conversa()
kennedy.conversa()

# ----------------------------------------------------------
print('-'*25)

class Pessoa1:

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


regis = Pessoa1('Regis')
print(regis)
fabio = Pessoa1('Fabio')
print(fabio)


#---------------------------------------------
print('-'*25)

class Carros:

    def __init__(self,ano,nome):
        self.ano = ano
        self.nome = nome

    def Retorna_ano(self):
        return self.ano 

    def Retorna_nome(self):
        return self.nome     

carro = Carros(2018,'Camaro')
print('Ano:',carro.Retorna_ano())
print('Nome:',carro.Retorna_nome())

#----------------------------------------------
print('-'*25)

class Pai:

    var = 'Calsse Pai -> teste'

class filhos(Pai):  #ligando as calss
    pass # classe vazia 

obj_pai = Pai()
obj_filhos = filhos()

#print ('Pai:',obj_pai.var)
print('Filhos:',obj_filhos.var)



