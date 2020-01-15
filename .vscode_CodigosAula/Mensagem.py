from datetime import date
class Mensagem:
    #imagem,audio,video
    def __init__(self,Texto,Data):
        self.Texto = Texto
        self.Data = date.today()

    @property
    def Texto(self):
        return self.__Texto

    @Texto.setter
    def Texto(self,novoTexto):
        self.__Texto=novoTexto

    @property
    def Data(self):
        return self.__Data

    @Data.setter
    def Data(self,novaData):
        self.__Data=novaData

    def mensagem(self):
        self.Texto


