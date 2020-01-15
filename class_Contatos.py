class Contatos:# obs tem (conversa):
    def __init__(self,lista_contatos):
        self.lista_contatos = []        #obs - self.contato ?

    @property
    def lista_contatos(self): return self.lista_contatos
    @lista_contatos.setter
    def lista_contatos(self,novalista): self.lista_contatos = novalista

    def adicionar(self,contato): pass
    def remover(self,contato): pass
    def consultar(self,nome): pass     
                 # ou numero