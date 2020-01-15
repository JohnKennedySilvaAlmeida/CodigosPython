class Automovel: #classe Herança 

    def __init__(self,ano,marca,modelo): #carro
        print(f'Meu carro é um {modelo} da marca {marca} e ano {ano}          [carros]')
        self.ano = ano 
        self.marca = marca
        self.modelo = modelo

    def dirigir(self):  #dirigir
        print("Metodo - Dirigir")
    def ligar(self):   #ligar
        print('Metodo - ligar')
    def lavar(self):  # lavar 
        print('Metodo - lavar')    
  
cars = Automovel('2018','Toyota','Hilux')
cars.dirigir()
cars.ligar()
cars.lavar()   

class Off_Road(Automovel):

    def __init__(self,assecorios,comprimento): #off road / carros
        print(f'Acessorios:{assecorios} e tem o tamnho {comprimento}       [Off-road]')
        self.assecorios = assecorios
        self.comprimento = comprimento 

    def desatola(self):
        print("Metodo - desatolar")
    def escalar(self):
        print('Metodo - escala')
    def reboca(self):
        print("Metodo - rebocar")  

cars1 = Off_Road('Peneus com cravos','1,05cm')
cars1.desatola()
cars1.escalar()
cars1.reboca()  

class Corrida(Automovel):

    def __init__(self,turbo,nitro,spolier): #corrida / carros
        print(f'Acessorios:turbo {turbo} ,nitro da marca {nitro} e spolier {spolier}       [Corrida]')
        self.turbo = turbo
        self.nitro = nitro
        self.spolier = spolier

    def correr(self):
        print("Metodo - correr")
    def derrapar(self):
        print('Metodo - derrapar')

cars2 = Corrida('2.5 kl','Nós','xxx')
cars2.correr()
cars2.derrapar()


print('_*'*30)  # obs teste!!  ----------------------------------------------

class Automovel_: #classe 
    
    modelo = 'camaro'
    marca = 'chefrolet'
    ano = 2018
    print(f'Meu carro é um {modelo} da marca {marca} e ano {ano}          [carros]')
      

    def dirigir(self):  #dirigir
        print("Metodo - Dirigir")
    def ligar(self):   #ligar
        print('Metodo - ligar')
    def lavar(self):  # lavar 
        print('Metodo - lavar')     

class Off_Road_(Automovel_):

    assecorios = 'rodas kmt'
    comprimento = 2.99
    print(f'Acessorios:{assecorios} e tem o tamnho {comprimento}       [Off-road]')
       

    def desatola(self):
        print("Metodo - desatolar")
    def escalar(self):
        print('Metodo - escala')
    def reboca(self):
        print("Metodo - rebocar")  

objeto_carro = Automovel_()
objeto_off_road = Off_Road_()
print()

print('classe off-road;',objeto_off_road.ano)
print('classe automovel:',objeto_carro.ano)
print('Obs?',objeto_carro.dirigir()) #?
print('Obs?',objeto_off_road.ligar()) #?


print('#'*30)
# exe - outra parte --------------------------------------------------

class Automovel_1: 
    
    def __init__(self,marcha,embreagem):
        self.marcha = marcha
        self.embreagem = embreagem
        print(f'tipo de cambio {marcha},tipo de embreagem {embreagem} ')
      

    def Aumentar_marca(self):  
        print("Metodo - Machar")
    def Ligar(self):   
        print('Metodo - ligar')
    def Redefinir_marcha(self):  
        print('Metodo - Trocar machar')     

class Embreagem(Automovel_1):

    def __init__(self,pressionada):   # ? bool
        self.pressionada = pressionada
        print(f'Embreagem:{pressionada}')
       

    def Pressionar(self):
        print("Metodo - pressionar")
    def Soltar(self):
        print('Metodo - soltar')
    def Verificar(self):
        print("Metodo - verificar")  

class Cambio(Automovel_1):

    def __init__(self,posicao):  # init ?
        self.posicao = posicao
        print(f'Posição d cambio: {posicao}')

    def Posicionar(self):
        print('Metodo - posicionar')

    def Verifica(self):
        print('Metodo - verifica')         

obj_automovel = Automovel_1('5 marchas','curta')
obj_cambio = Cambio('ponto morto')
obj_embreagem = Embreagem('leve')


print('¨¨'*25)

#outro exemplo ----------------------------------------------######################

class Automovel_123: 
    #modelo   # atributo de classe assecivel em qualquer lugar 
    #ano 
    #marca
    
    def __init__(self,marca,modelo,ano):
        self.marca = marca  # atributos d obejto assecivel so dentro da instancia 
        self.ano = ano
        self.modelo = modelo
        #print(f'Marca {marca},ano {ano},modelo {modelo} ')

#Automovel_123.modelo = 'Fusca'  #classe
#print(Automovel_123.modelo)       
      
#camaro = Automovel_123('camaro',2018,'chefrolet') #obejto
#print(camaro.modelo)
#print(Automovel_123.modelo)  

#camaro = Automovel_123('Fabricação 2018') #obejto
#print(camaro.ano)
#print(Automovel_123.ano)  
     
    def dirigir(self):
        print('Metodo - dirigir')
    def lavar(self):
        print('Metodo - lavar')
    def ligar(self):
        print('Metodo - ligar')  

class Off__road_(Automovel_123):  

    def __init__(self,assecorios,comprimento): 
        self.assecorios = assecorios
        self.comprimento = comprimento 

    def desatola(self):
        print("Metodo - desatolar")
    def escalar(self):
        print('Metodo - escalar')
    def reboca(self):
        print("Metodo - rebocar")  

class _Corrida_(Automovel_123):

    def __init__(self,turbo,nitro,spolier): 
        self.turbo = turbo
        self.nitro = nitro
        self.spolier = spolier

    def correr(self):
        print("Metodo - correr")
    def derrapar(self):
        print('Metodo - derrapar')

 






