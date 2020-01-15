class Usuario():  #obs tem (contato,conversa):
    
    #def __init__(self,nome,telefone,apelido,online,imagem): pass
    
    # obs ?
    def __init__(self,Imagem):
        self.Imagem = Imagem

    @property
    def Imagem(self): return self.__Imagem
    @Imagem.setter
    def Imagem(self,NovaImagem): self.__Imagem = NovaImagem   
