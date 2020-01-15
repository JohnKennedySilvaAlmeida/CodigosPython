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


