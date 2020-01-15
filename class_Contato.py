class Contato:# obs tem (contatos):
    def __init__(self,nome,telefone,apelido,online):
        self.nome = nome
        self.telefone = telefone
        self.apelido = apelido
        self.online = online

    @property
    def nome(self): return self.__nome
    @nome.setter
    def nome(self,novonome): self.__nome = novonome
    @property
    def telefone(self): return self.__telefone
    @telefone.setter
    def telefone(self,novotelefone): self.__telefone = novotelefone
    @property
    def apelido(self): return self.__apelido
    @apelido.setter
    def apelido(self,novoapelido): self.__apelido = novoapelido 
    @property # obs! online e status 
    def online(self): return self.__online
    @online.setter
    def online(self,novoonline): self.__online = novoonline      
    @property
    def status(self): return self.__status
    @status.setter
    def status(self,novostatus): self.__status = novostatus       
    # obs !
    def mudar_status(self,novo_Status): 
        pass