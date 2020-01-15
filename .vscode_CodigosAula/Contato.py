class Contato:

    def __init__(self,Nome,Apelido,Telefone,Online):
        self.Nome = Nome
        self.Apelido = Apelido
        self.Telefone = Telefone
        self.Online = Online
        
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
    def Apelido(self,novoApelido):
        self.__Apelido=novoApelido

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

    def contato(self,Nome,Apelido,Telefone,Online):
       pass
        
        
