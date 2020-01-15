import pycep_correios

class Endereco:
   
    def __init__(self,cep,numero):
        self.carregar(cep)
        self.setNumero(numero)
       
    def setRua(self,rua): self.__rua = rua

    def getRua(self): return self.__rua

    def setNumero(self,numero): self.__numero = numero

    def getNumero(self): return self.__numero

    def setCep(self,cep): self.__cep = cep

    def getCep(self): return self.__cep

    def setCidade(self,cidade): self.__cidade = cidade

    def getCidade(self): return self.__cidade

    def setEstado(self,estado): self.__estado = estado

    def getEstado(self): return self.__estado

    def enderecoo(self):
        pass

    def carregar(self,cep):
        endereco = pycep_correios.consultar_cep(cep)
        self.setCidade(endereco['cidade'])
        self.setEstado(endereco['uf'])
        self.setRua(endereco['end'])
        self.setCep(cep)
        #print(endereco)   endereco 1 



      





         









