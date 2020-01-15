from Usuario import Usuario
from Contato import Contato
from Mensagem import Mensagem
from datetime import datetime

class Conversa:
    def __init__(self,usuario,inicio,fim):
        self.usuario = usuario
        self.participantes = []
        self.inicio = datetime.now()
        self.fim = datetime.now() 

    @property
    def usuario(self): 
        return self.__usuario

    @usuario.setter
    def usuario(self,novousuario): 
        self.__usuario = novousuario

    @property
    def participantes(self): 
        return self.__participantes

    @participantes.setter
    def participantes(self,novoparticipantes): 
        self.__participantes= novoparticipantes 

    @property
    def inicio(self): 
        return self.__inicio

    @inicio.setter
    def inicio(self,novoinicio): 
        self.__inicio = novoinicio

    @property
    def fim(self): 
        return self.__fim

    @fim.setter
    def fim(self,novofim): 
        self.__fim = novofim

    #participante tbm envia msg mudar o construtor para o X participante enviar
    def Conversa(self,Usuario): 
        print(f'{self.usuario} entrou no chat') 
        for i in self.__participantes:
            print(f'{i.Nome} entrou no chat')
        if Usuario == self.usuario:
            print(f' digite uma mensagem') 
        else:
            for i in self.__participantes:
                if i.Nome == Usuario:
                    self.usuario = Usuario  
        
    def enviarMensagem(self,mensagem):
        print('mensagem enviada com sucesso!!')
        self.inicio = self.inicio.strftime("%X")
        Mensagem.mensagem(mensagem)

    def receberMensagem(self): 
        print("mensagem recebida com sucesso!!")
        self.fim = self.fim.strftime("%X")

    def adicionarParticipante(self,participante):
        #participante retorna None caso o usuario está offline
        if participante.Online == False: 
            print('usuario indisponivel')
        elif participante == None:
            print('usuario não encontrado')
        else:
            self.__participantes.append(participante)
            print("participante adicionado")

    def removerParticipante(self,Nome): 
        if not Nome == None:
            itemParaDeletar = ""
            for i in self.__participantes:
                if i.Nome == Nome.Nome:
                    itemParaDeletar = i
                    break

            self.__participantes.remove(itemParaDeletar) 
        else:
            print("Usuario não encontrado")
    
    def gravarConversa(self,caminho,texto,data):
        with open(caminho,'w') as arq:
            arq.write(f'{self.usuario} disse: {texto}  -envio da mensagem {self.inicio} -recepcao da mensagem {self.fim} dia:{data.strftime("%d")}')
        self.inicio=datetime.now()
        self.fim=datetime.now() 

