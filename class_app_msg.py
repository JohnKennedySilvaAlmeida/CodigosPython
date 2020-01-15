from datetime import date

class Messagem:# obs tem (conversa):
    def __init__(self,texto,data,imagem,audio,video):
        self.texto = texto
        self.data = date.today()
        self.imagem = imagem
        self.audio = audio
        self.video = video

    @property
    def texto(self): return self.__texto
    @texto.setter
    def texto(self,novotexto): self.__texto = novotexto
    @property
    def imagem(self): return self.__imagem
    @imagem.setter
    def imagem(self,novaimagem): self.__imagem = novaimagem
    @property
    def audio(self): return self.__audio
    @audio.setter
    def audio(self,novoaudio): self.__audio = novoaudio
    @property
    def video(self): return self.__video
    @video.setter
    def video(self,novovideo): self.__video = novovideo
    @property
    def data(self): return self.__data
    @data.setter
    def data(self,novadata): self.__data = novadata    


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
        if novo_Status == True:
            print('On')
        else:
            print('OFF')    

class Contatos:# obs tem (conversa):
    def __init__(self,contato): # obs -  contato?
        self.lista_contatos = []        #obs - self.contato ?
        self.contato = contato

    @property
    def contato(self): return self.contato
    @contato.setter
    def contato(self,novocontato): self.contato = novocontato
    @property
    def lista_contatos(self): return self.lista_contatos
    @lista_contatos.setter
    def lista_contatos(self,novalista): self.lista_contatos = novalista

    def adicionar(self,nome,telefone,apelido,online): 
        add = Contato(nome,telefone,apelido,online)
        if hasattr(self,'_Contato__lista_contatos'):
            self.lista_contatos = []
        self.lista_contatos.append(add)    
    
    def remover(self,contato): # obs contato
        remover_item = ''
        for add in self.lista_contatos:
            if add.contato == contato:   #add. nome      obs!
                remover_item = add
                break
        self.lista_contatos.remove(remover_item)          
    
    def consultar(self,nome): # obs!   
        for add in self.lista_contatos:
            if add.nome == nome:
                print('ok')
            else:
                print('Não encontrado')    


                 
class Usuario(Contato):  #obs tem (contato,conversa):
    
    #def __init__(self,nome,telefone,apelido,online,imagem): pass
    # obs ?

    def __init__(self, imagem, nome, telefone, apelido, online):
        Contato.__init__(nome, telefone, apelido, online)
        self.imagem = imagem

    @property
    def imagem(self):
        return self.imagem

    @imagem.setter
    def imagem(self, novaImagem):
        self.__imagem = novaImagem

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


