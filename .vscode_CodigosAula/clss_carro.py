class Automovel:
    
    # construtor - serve pra criar uma instância da classe
    def __init__(self, marcha, embreagem, pneus, nome):
        self.setMarcha(marcha)
        self.setEmbreagem(embreagem)
        self.setPneus(pneus)
        self.setNome(nome)
        self.setKmRodado(0)        

    def setNome(self, novoNome): 
        self.__nome = novoNome

    def getNome(self): return self.__nome
    def setMarcha(self, novaMarcha): self.__marcha = novaMarcha
    def getMarcha(self): return self.__marcha
    def setEmbreagem(self, novaEmbreagem): self.__embreagem = novaEmbreagem
    def getEmbreagem(self): return self.__embreagem
    def setPneus(self, novosPneus): self.__pneus = novosPneus
    def getPneus(self): return self.__pneus
    def setKmRodado(self, novoKmRodado): 
      # Verificar se o atributo não existe no objeto (na primeira vez que for chamado, ele ainda não existe)
      if hasattr(self, '_Automovel__kmRodado') == False:
        self.__kmRodado = self.carregar("python\\meucarrosalvo.txt") # se não existe, carregar do arquivo

      self.__kmRodado += novoKmRodado # agora ele existe, incrementar com o valor recebido no parametro do metodo


    def getKmRodado(self): 
        print("O automovel já rodou {} kilômetros".format(self.__kmRodado))
        return self.__kmRodado

    def ligar(self):
        posicao = self.getMarcha().getPosicao()
        if posicao > 0:
            self.getEmbreagem().setPressionado(True)
        print("O carro está ligado")
    
    def aumentarMarcha(self):
        posicao = self.getMarcha().getPosicao()
        if posicao < 5:
            self.getEmbreagem().setPressionado(True)
            novaMarcha = posicao + 1
            self.getMarcha().setPosicao(novaMarcha)
            print("Aumentamos a marcha")

    def reduzirMarcha(self):
        if self.getMarcha().getPosicao() > -1: 
            self.getEmbreagem().setPressionado(True)
            self.getMarcha().setPosicao(self.getMarcha().getPosicao() - 1)
        
        print("O carro está na marcha {}".format(self.getMarcha().getPosicao()))
        
    def salvar(self, caminho):
        try:
          arquivo = open(caminho, 'w')
          arquivo.write(str(self.getKmRodado()))
          arquivo.close()
        except:
          print(f'O caminho {caminho} não foi encontrado')
        print("Arquivo salvo")

    def carregar(self, caminho):
        try:
          arquivo = open(caminho)
        except:
          return 0
        return int(arquivo.read())


class Cambio:

    def __init__(self, posicao):
        self.setPosicao(posicao)
    
    def setPosicao(self, novaPosicao): self.__posicao = novaPosicao
    def getPosicao(self): return self.__posicao    

class Embreagem:

    def __init__(self, pressionado):
        self.setPressionado(pressionado)
    
    def setPressionado(self, novoPressionado): 
      self.__pressionado = novoPressionado
      print("Embreagem pressionada!")
    def getPressionado(self): return self.__pressionado

class Pneu:

    def __init__(self, pressao, balanceado):
        self.setPressao(pressao)
        self.setBalanceado(balanceado)
    
    def setPressao(self, novaPressao): 
      self.__pressao = novaPressao
      print("Pneu calibrado!")
    def getPressao(self): return self.__pressao
    def setBalanceado(self, balanceado): 
      self.__balanceado = balanceado
      print("Pneu balanceado!")
    def getBalanceado(self): return self.__balanceado


# ====================================== app =========================================

# jeito mais otimizado
#from classes import Automovel, Cambio, Embreagem, Pneu

__cambio = Cambio(0)
__embreagem = Embreagem(False)
__pneus = list()
for i in range(5):
    __pneus.append(Pneu(10, True))

meuCarro = Automovel(__cambio, __embreagem, __pneus, 'carrro do professor')

#calibrar os pneus
for pneu in meuCarro.getPneus():
    pneu.setPressao(30)

# ligar
meuCarro.ligar()

#subir marcha
for i in range(6):
    meuCarro.aumentarMarcha()

meuCarro.setKmRodado(20)
meuCarro.setKmRodado(50)
meuCarro.setKmRodado(140)
print(meuCarro.getKmRodado())

for i in range(8):
    meuCarro.reduzirMarcha()

for pneu in meuCarro.getPneus():
    pneu.setPressao(30)

meuCarro.salvar("python\\meucarrosalvo.txt")

print("Fim do programa")