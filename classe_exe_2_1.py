class Automovel:
    def __init__(self, marcha, embreagem, pneus):
        self.marcha = marcha
        self.embreagem = embreagem
        self.pneus = pneus
        self.kmRodado = 0  # var 

    def ligar(self):
        posicao = self.marcha.verificarPosicao()
        if posicao > 0:
            self.embreagem.pressionar()
        print('Carro Ligado - Ok')

    def aumentarMarcha(self):
        posicao = self.marcha.verificarPosicao()
        if posicao <= 5:
            self.embreagem.pressionar()
            NovaMarcha = posicao + 1
            self.marcha.posicionar(NovaMarcha)
  
    def reduzirMarcha(self):
        posicao = self.marcha.verificarPosicao()
        if posicao >= 1:
            self.embreagem.pressionar()
            ReduzMarcha = posicao - 1
            self.marcha.posicionar(ReduzMarcha)
            if ReduzMarcha >= 1:
                print(f'{ReduzMarcha}º Marcha [-]')
            else:
                print('Marcha em Posição [N]')

    def rodar(self,km):
        self.kmRodado += km         # kmrodado atributo 
        
    def consultarkmRodado(self):
        print(f'Rodado {self.kmRodado} km') # metodos obs #
        return self.kmRodado

    def salvar(self,caminho):
        arquivo = open(caminho,'w')  
        arquivo.write(str(self.kmRodado))   # 
        arquivo.close()  
        
    def carregar(self,caminho):
        arquivo = open(caminho)     # abri arquivo 
        self.kmRodado = arquivo.read()

class Embreagem:
    def __init__(self, pressionado): #Self é a instância
        self.pressionado = pressionado

    def pressionar(self):
        if not self.pressionado:
            self.pressionado = True
        print('Pressionando a Embreagem')
    def soltar(self):
        if self.pressionado:
            self.pressionado = False #?  p .. r 
        print('Embreagem solta')    

    def estarPressionada(self):
        return self.pressionado


class Cambio:
    def __init__(self, posicao):
        self.posicao = posicao

    def posicionar(self, NovaPosicao):
        self.posicao = NovaPosicao

    def verificarPosicao(self):
        return self.posicao

class Pneu:
    def __init__(self, pressao, balanceado):
        self.pressao = pressao
        self. balanceado = balanceado

    def calibrar(self,NovaPressao):
        self.pressao = NovaPressao

    def estaBalanceado(self):
        return self.balanceado

    def balancear(self):
        self.balanceado = True
