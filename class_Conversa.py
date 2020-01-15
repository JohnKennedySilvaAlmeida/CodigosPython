class Conversa: #obs tem (usuario contatos mensagem ...):
    def __init__(self,usuario,participante,inicio,fim):
        self.usuario = usuario
        self.participante = participante
        self.inicio = inicio #datime
        self.fim = fim #datime   

    @property
    def usuario(self): return self.__usuario
    @usuario.setter
    def usuario(self,novusuario): self.__usuario = novusuario
    @property
    def participante(self): return self.__participante
    @participante.setter
    def participante(self,novoparticipante): self.__participante= novoparticipante 
    @property
    def inicio(self): return self.__inicio
    @inicio.setter
    def inicio(self,novoinicio): self.__inicio = novoinicio
    @property
    def fim(self): return self.__fim
    @fim.setter
    def fim(self,novofim): self.__fim = novofim
    # obs ? 
    def conversa(self,Usuario): pass
    def enviar_mensagem(self,Messagem): pass
    def receber_mensagem(self): pass
    def add_participante(self,Contato): pass
    def remover_participante(self,nome): pass            