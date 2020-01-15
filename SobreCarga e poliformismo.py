# METODO ->  overloud e sobre descrição - Herança e poliformismo 

'''
class veiculo:
    def ligar(self):
        print('Veiculo')

class carro(veiculo):
    
    def ligar(self):
        print('carro')

class moto(veiculo):  
   
    def ligar(self):
        print('moto')   
    def __str__(self):
        return 'Sou uma motocicleta - descrição'    


lista = []

c = carro()
c.ligar()
lista.append(c)

m = moto()
m.ligar()
lista.append(m)

for item in lista:
    item.ligar()
    print(item)                      # -> poliformismo
'''
# sobre escrição de metodo                  obs - import abc      !!!!
class Pessoas:
    def __init__(self,nome):
        self.nome = nome

    def ImprimeNome(self):
        print('Meu nome é' + self.nome)

class Doutor(Pessoas):
   # pass
    def ImprimeNome(self):
        print("DR." + self.nome)  

class General(Pessoas):
    #pass
    def ImprimeNome(self):
        print('General.'+ self.nome)  

class Soldado(Pessoas):
    pass

# app ----------------------------------

obj_doutor = Doutor('john') 
obj_doutor.ImprimeNome()

obj_general = General('kennedy')
obj_general.ImprimeNome()
