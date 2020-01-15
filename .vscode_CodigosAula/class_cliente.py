from classe_End_correios import Endereco
from class_CPF import cpf


class Cliente:# from endereco import Endereco    //  from CPFpast import CPF // 

    def __init__(self,cpf,nome,credito): #endereco
        self.cpf = cpf
        self.nome = nome
        self.credito = credito
        #self.endereco = endereco   #????
    
    @property
    def endereco(self): return self.__endereco  

    @endereco.setter                      # obs!!????
    def endereco(self,endereco): self.__endereco = endereco
                          #import d clss (Endereco)
    
    @property
    def credito(self): return self.__credito 

    @credito.setter 
    def credito(self,novocredito): self.__credito = novocredito
    
    @property
    def nome(self): return self.__nome  

    @nome.setter
    def nome(self,novonome): self.__nome = novonome
   
    @property
    def cpf(self): return self.__cpf 
   
    @cpf.setter
    def cpf(self,novocpf):
        if cpf.validar(novocpf):
            self.__cpf = novocpf
        else:
            print('... CPF INVALIDO! Tente novamente ...')    

       