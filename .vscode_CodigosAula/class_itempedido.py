

class ItemPedido:  # import ?

    def __init__(self,codigo,descricao,quantidade,preco):
        self.codigo=codigo
        self.descricao=descricao
        self.quantidade=quantidade
        self.preco=preco

    @property
    def codigo(self): return self.__credito

    @codigo.setter
    def codigo(self,novocodigo):  #obs if novocodigo?
        if type(novocodigo) is int:
            self.__credito = novocodigo
        else:
            raise Exception('O codigo deve ser do tipo inteiro!!')    

    @property
    def descricao(self): return self.__descricao

    @descricao.setter
    def descricao(self,novadescricao): self.__descricao = novadescricao

    @property
    def quantidade(self): return self.__quantidade

    @quantidade.setter
    def quantidade(self,novaquantidade): self.__quantidade = novaquantidade

    @property
    def preco(self): return self.__preco

    @preco.setter
    def preco(self,novopreco): self.__preco = novopreco