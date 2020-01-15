from Contato import Contato
class Usuario(Contato):

    def __init__(self,Nome,Apelido,Telefone,Online):
        super().__init__(Nome,Apelido,Telefone,Online)
        #self.Imagem=Imagem
        
    @property
    def Nome(self):
        return self.__Nome

    @Nome.setter
    def Nome(self,novoNome):
        self.__Nome=novoNome

    @property
    def Apelido(self):
        return self.__Apelido

    @Apelido.setter
    def Apelido(self,novosApelido):
        self.__Apelido=novosApelido

    @property
    def Telefone(self):
        return self.__Telefone

    @Telefone.setter
    def Telefone(self,novoTelefone):
        self.__Telefone=novoTelefone

    @property
    def Online(self):
        return self.__Online

    @Online.setter
    def Online(self,novoOnline):
        self.__Online=novoOnline

    #Imagem/pesquisar
    def Usuario(self,Nome,Apelido,Telefone,Online):
        pass