# exe 1 herança

class Automovel_123: 
    #modelo          # atributo de classe assecivel em qualquer lugar 
    #ano 
    #marca
    
    def __init__(self,marca,modelo,ano):
        self.marca = marca  # atributos d obejto assecivel so dentro da instancia 
        self.ano = ano
        self.modelo = modelo  
     
    def dirigir(self):
        print('Metodo - dirigir')
    def lavar(self):
        print('Metodo - lavar')
    def ligar(self):
        print('Metodo - ligar')  

class Off__road(Automovel_123):  

    def __init__(self,modelo,ano,marca,assecorios,comprimento): 
        Automovel_123.__init__(self,modelo,ano,marca)
        self.assecorios = assecorios
        self.comprimento = comprimento 

    def desatola(self):
        print("Metodo - desatolar")
    def escalar(self):
        print('Metodo - escalar')
    def reboca(self):
        print("Metodo - rebocar")  

class Corrida(Automovel_123):

    def __init__(self,modelo,ano,marca,turbo,nitro,spolier): 
        Automovel_123.__init__(self,modelo,ano,marca)
        self.turbo = turbo
        self.nitro = nitro
        self.spolier = spolier

    def correr(self):
        print("Metodo - correr")
    def derrapar(self):
        print('Metodo - derrapar')


camaro = Corrida('camaro',2018,'chefrolet',True,10,False)
camaro.correr()
camaro.lavar()
camaro.derrapar()







