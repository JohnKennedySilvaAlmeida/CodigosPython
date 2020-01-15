class Automovel:       # nao herança  -----    + publico    - privado  # estatico 
                          # agregação 
    def __init__(self,pneu,marcha,embreagem): #contrutor 
        self.marcha = marcha
        self.embreagem = embreagem #atributos 
        self.pneu = pneu

    def ligar(self): 
        posicao = self.marcha.verificarPosicao()
        if posicao > -1:
            self.embreagem.pressionar()
        print('O carro esta ligado')       

    def aumentarMarcha(self):  #metodoss
        posicao = self.marcha.verificarPosicao()
        if posicao < 5:
            self.embreagem.pressionar()
            nova_marcha = posicao + 1
            self.marcha.posicionar(nova_marcha) 
        print("Proxima marcha + ")    
         
    def reduzirMarcha(self):
        posicao = self.marcha.verificarPosicao()
        # if self.posicao > -1: self.posicao -= 1        # outra forma d fazer
                                   # obs - posição ????
        if posicao > -1:
            self.embreagem.pressionar()
            reduz_marcha = posicao - 1
            self.marcha.posicionar(reduz_marcha)
            if reduz_marcha == -1:
                print('Machar Ré')
            else:
                print(f'O carro esta na marcha {reduz_marcha}')    


class Embreagem:

    def __init__(self,pressionado):  
        self.pressionado = pressionado

    def pressionar(self):
        if not self.pressionado: self.pressionado = True
       
    def soltar(self):
        if self.pressionado: self.pressionado = False
       
    def estaPressionada(self):
        return self.pressionado
        
        
         
class Cambio:

    def __init__(self,posicao): 
        self.posicao = posicao

    def posicionar(self,nova_posicao):
        self.posicao = nova_posicao
        
    def verificarPosicao(self):
        return self.posicao
         

class Pneu:  

    def __init__(self, pressao,balanceado):
        self.pressao = pressao
        self.balanceado = balanceado

    def calibrar(self,nova_pressao):
        self.pressao = nova_pressao

    def estaBalanceado(self):
        return self.balanceado

    def balancear(self):
        self.balanceado = True        


# falta ?       melhorar 


from classe_exe2 import Automovel, Cambio, Embreagem, Pneu

obj_cambio = Cambio(posicao = 0) 
obj_embreagem = Embreagem(pressionado = False) 
pneus = list() #lista

for i in range(5):
    pneus.append(Pneu(30, True))

obj_automovel = Automovel(obj_cambio,obj_embreagem,pneus)

for Pneu in pneus: # obs -> obj_automovel
    Pneu.calibrar(nova_pressao = 30)

obj_automovel.ligar()  # obs 

for j in range(1,6):
    obj_automovel.aumentarMarcha()
    print(f'{j}º Marcha')

for y in range(8):
    obj_automovel.reduzirMarcha()

for Pneu in pneus:
    Pneu.balancear()

print('ACABOU')


