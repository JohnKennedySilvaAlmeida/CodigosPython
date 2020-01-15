# Class Prova 
#import datetime

class Conta:
    def __init__(self, agencia, numero):
        self.agencia = agencia
        self.numero = numero
        #self.abertura = date   obs !
       # self.saldo = float(saldo)
     
    @property
    def agencia(self): return self.agencia
    @agencia.setter
    def agencia(self, Novaagencia): self.agencia = Novaagencia

    @property
    def numero(self): return self.numero
    @numero.setter
    def numero(self, Novonumero): self.numero = Novonumero

    def depositar(self,valor): # obs 
        self.__valor = self.__valor+valor
        return self.__valor

    def transferir(self, destino, valor): #obs 
        self.__destino = destino
        self.__valor = float(valor)
    
    def sacar(self, valor): #obs 
        self.__valor = valor   

class Endereco:
    def __init__(self, rua, numero, bairro, cidade):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade

    @property
    def rua(self): return self.__rua
    @rua.setter
    def rua(self, Novarua): self.__rua = Novarua

    @property
    def numero(self): return self.__numero
    @numero.setter
    def numero(self, Novonumero): self.__numero = Novonumero

    @property
    def bairro(self): return self.__bairro
    @bairro.setter
    def bairro(self, Novobairro): self.__bairro = Novobairro

    @property
    def cidade(self): return self.__cidade
    @cidade.setter
    def cidade(self, Novacidade): self.__cidade = Novacidade

class Cliente:
    def __init__(self,nome,cpf,nascimento): 
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        #self.endereco(Endereco)      obs !
        #self.contaCorrente(Conta)    obs !

    @property
    def nome(self): return self.__nome  
    @nome.setter                     
    def nome(self,novoNome): self.__nome = novoNome

    @property
    def cpf(self): return self.__cpf                     
    @cpf.setter
    def cpf(self,novocpf): self.__cpf = novocpf  

    @property
    def nascimento(self): return self.__nascimento 
    @nascimento.setter                     
    def nascimento(self,novoNASC): self.__nascimento = novoNASC

    def IncluirEndereço(self):
        self.__endereco = Endereco # obs!
    def criarConta(self):
        self.__conta = Conta  # obs !

class ClienteEspecial(Cliente):
    def __init__(self, valorlimite):
        super().__init__()
        self.valorlimite = valorlimite(float)
        
    @property
    def valorlimite(self): return self.__valorlimite
    @valorlimite.setter
    def valorlimite(self, Novovalorlimite): self.__valorlimite = Novovalorlimite
    
    def IncluirCartaoCredito(self,limite): 
        self.numeroCartaoCredito = limite  # obs falta ????
        return self.__valorlimite

    def incrementarLimite(self,incremento): 
        self.__valorlimite += incremento # obs falta ????? 
        return  self.__valorlimite
               








    










    
    

