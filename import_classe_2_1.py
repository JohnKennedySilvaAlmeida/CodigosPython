#
from classe_exe_2_1 import Automovel, Cambio, Embreagem, Pneu

import time

obj_cambio = Cambio(posicao=0)
obj_embreagem = Embreagem(pressionado=False)
pneus = list() # obj penus

#for i in range (5):
   # pneus.append(Pneu(30,True))    vai antes d -> objeto_carro

print('===== Automovel ======')
print('Calibrando Pneus [O]')
time.sleep(3)

obj_carro = Automovel(obj_cambio,obj_embreagem,pneus) # instancia (...)

for i in range(5):
    for Pneu in obj_carro.pneus:
        Pneu.Calibrar(NovaPressao=30)
        pneus.append(Pneu(30, True))
    if i >= 1:
        print('Calibrando... ')
        time.sleep(3)
        print(f'Pneu {i} Calibrado')
        time.sleep(2)

for Pneu in pneus:
    Pneu.balancear()
print('...Ligando o Carro...')
time.sleep(4)

obj_carro.ligar() #executando  o metodo ligar
time.sleep(2)

for i in range(6):
    if i >= 1:
        obj_carro.aumentarMarcha() #metodo aumentarmarcha
        if i == 0:
            print('Carro em Ponto Morto')  
        print(f'{i}º Marcha [+] ')    
        time.sleep(3)

print('Reduzindo marcha <>')

time.sleep(2)
print(f'Esta na ultima marcha {i}')

for i in range(6):
    obj_carro.reduzirMarcha()
    time.sleep(2)

obj_carro.rodar(55)
obj_carro.rodar(33)
obj_carro.consultarkmRodado()

#obj_carro.salvar("C:\\Users\\Jk_cu\\OneDrive\\Área de Trabalho\\teste.txt")

print('-'*30)
print('!!! Carro parado !!!')




