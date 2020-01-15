# 1 - while - looops =================================================================

n = s = 0

while n != 999:
    n = int(input('digite numeros;'))
    s += n
s-= 999

print('Soma total {}'.format(s))    

# outra forma

p = t = 0

while True:
    p = int(input('digite numeros;'))
    if p == 999:
        break
    t += p

print('Soma total {}'.format(t))    


# 2 - tuplas ================================================ sao inmutaveis ,, nao da pra mudar.... 
tupla = tuple()
tupla =('john','kennedy','sc','25','brasil')

print(tupla)
print(tupla[2])
print("ultima posição,",tupla[-1])
print("primeira posição,",tupla[0])
print(tupla[1:])
print(tupla[0:2])
print(tupla[:3])
print(tupla[-2:])

print(sorted(tupla))

#for i in tupla:
   # print("tuplas -> ",i)
#print('----------------')    

# for outra maneira *

#for cont in range(0, len(tupla)):
    #print(tupla[cont],'- Posição',cont) # ou cont
#print('-------------------------')

#outra forma * 

for y,i in enumerate(tupla):
    print("tuplas -> ",i,':Posição >',y)
print('----------------')    


tupla2 = (11,22,33)
tupla1 =(1,2,3)

mais = tupla1 + tupla2

print(mais) # junta
print(len(mais))#tamanho 
print(mais.count(2))# contar quantas x aparece o 2 n tupla
print(mais.index(22)) # localiza sua posição 

p = ('John',25,'p',65.23)
#del (p)      # excluir 

tuplas1 = tuple()

tuplas1 = tuple(1,2,3,4,5,'jk','sc','br')

tuplas1 = tuplas1 + ('copia',) # adicionar 

#print(tuplas)

t123 = tuple('john kennedy d silva d almeida')
print(t)


tuplas = tuple()

tuplas = (1,2,3,4,5,'jk','sc','br',1.33)
    

for y,i in enumerate(tuplas):
    print(f"Itens da tupla ->({i})                Posição > {y}")
print('--'*25)   

# obs..
contatos = dict()

#contatos = ["john","kennedy"] = 'Fonexxxxxxxxxxx' #
#contatos = ["silva","almeida"] = 'xxxxxxxxxxx'   

for nome,telefone in contatos.items():
    print("Nome {} {}, telefone {} ".format(nome[0],nome[1], telefone))

# 3 Lista ==============================================================================

listas = []
listas =['john','kennedy','sc','25','brasil']

listas[1] = 'Silva' # troca pela posição 
listas.append('Baiha') # adiciona 
listas.insert(0,'lulaaa') #adiciona pela posiçao que vc define 
del listas[1] #apaga tudo ou pela posição 
listas.pop(2) #apaga pela posição ou o ultimo ()
listas.remove('john') # remove pelo nome \ conteudo *
listas.sort() # organiza em sequencia 
listas.sort(reverse = True) # reverso da lista
len(listas) # tamanho da lista 
print(max(listas)) # maior valor da lista 
print(min(listas)) # menor valor ... list




if '25' in listas:
    listas.remove('25') # para remover da lista
else:
    print("Não achei !! na Lista.. ")


valor = list(range(4,11))   #

#print(valor) criando uma lista com range 


num = []
num.append(1)
num.append(5)
num.append(12)

for n in num:
    print(f'{n}...') # print uma forma 
    print(f'{n}***',end='') # outra forma   # 1

for cont  in range (0,5):
    num.append(int(input("Digite valores:")))   # 2

for i , n in enumerate(num):
    print(f'na posição {i} encontrei  o valor {n} ...',end='') #2.1
    print(f'na posição {i} encontrei  o valor {n} ...')



a = [1,2,3]
b = a 
b[1] = 333 #obs 

print(f'Lista A: {a}')
print(f'Lista A: {b}')   # ligaçao de lista 

# -- - - - - - - - -

a1 = [1,2,3]
b1 = a1[:] #copia todos os valores da lista pra b 
b1[1] = 333 #obs 

print(f'Lista A: {a1}')
print(f'Lista A: {b1}')   # ligaçao de lista 

#  outros programs =========================================================================== 1

import os
import sys

#Pega qual é o SO
so = sys.platform
so_clear = ''

# Defini o argumento para limpeza de tela de acordo com o SO
if (so == 'linux'):
    so_clear = 'clear'
elif (so[:3] == 'win'):
    so_clear = 'cls'

# Função lambda para limpeza de tela
if so_clear:
    limpar = lambda l: os.system(l)
else:
    limpar = lambda l: l

def main():
    """Inicializa o programa"""

    limpar(so_clear)
    print('Programa para administrar sua lista de filmes favoritos')
    print()

    while True:
        print()
        print('Escolha uma das opções abaixo\n')
        print('1 - Ver a lista')
        print('2 - Adicionar filmes na lista')
        print('3 - Excluir filmes da lista')
        print('0 - Sair\n')

        opcao = input('Entre com o número da opcao: ')
        print()

        if (opcao == '1'):
            ver()
        elif (opcao == '2'):
            adicionar()
        elif (opcao == '0'):
            sys.exit(0)
        else:
            print('Opcao inválida')
def existe():
    """Verifica se o arquivo filmes.txt existe"""
    if os.path.isfile('data/filmes.txt'):
        return 'data/filmes.txt'
    else:
        return ''

def ver():
    """Mostra na tela do terminal 20 itens por vez da lista de filmes"""

    arq = existe()
    if not arq:
        input("O arquivo filmes.txt ainda não foi "
              "criado, tecle enter para continuar")
        return

    limpar(so_clear)
    print("Lista de Filmes:")
    print("(tecle enter para continuar)\n")
    with open(arq, 'r') as arquivo:
        filmes = arquivo.readlines()
        x = 0

        for filme in filmes:
            # Aqui declaramos end como um carcter vazio pois os
            # itens no arquivo já possuem um caracter de nova linha
            print(filme, end='')
            if x > 20:
                x = 0
                input()
            x += 1

def adicionar():
    """Adiciona filmes ao arquivo"""
    filmes = []
    opcao = ''
    arq = existe()

    if not arq:
        opcao = 'w'

    limpar(so_clear)
    print("Entre com os filmes digite 0 para sair")
    while True:
        filme = input()
        if filme != '0':
            filmes.append(filme)
        else:
            break

    with open(arq, opcao) as arquivo:
        for filme in filmes:
            # insere um caracter de nova linha até o penultimo item
            arquivo.write("{0}{1}".format(filme, '\n'))

        return

main()

# ======================================================================== programs 2

def retangulo(lado_a, lado_b):
    """Calcula a área de um retângulo"""
    area = lado_a * lado_b
    return area

def triangulo(base, altura):
    """Calcula a área de um triângulo"""
    area = (base * altura) / 2
    return area

def circulo(raio):
    """Calcula a área de um círculo"""
    area = 3.14 * (raio ** 2)
    return area

opcao = -1
while opcao != 0:
    print('Escolha o objeto que deseja calcular a área')
    print()
    print('1 - Retângulo')
    print('2 - Triângulo')
    print('3 - Círculo')
    print('0 - Sair')
    print()
    opcao = int(input('Entre com o número da opção desejada: '))
    if (opcao == 1):
        lado_a = float(input('Entre com um lado do retângulo: '))
        lado_b = float(input('Entre com o outro lado do retângulo: '))
        area = retangulo(lado_a, lado_b)
        print('\nA área do retâgulo é: {0:.2f}'.format(area))
    elif (opcao == 2):
        base = float(input('Entre com a base do triângulo: '))
        altura = float(input('Entre com a altura do triângulo: '))
        area = triangulo(base, altura)
        print('\nA área do triângulo é: {0:.2f}'.format(area))
    elif (opcao == 3):
        raio = float(input('Entre com o raio do cículo: '))
        area = circulo(raio)
        print('\nA área do círculo é: {0:.2f}'.format(area))
    elif (opcao != 0):
        print('\n{0} não é uma opção valida'.format(opcao))

    print()
print('Volte a qualquer hora')


#===================================================== programs 3

a = 21
b = 2
c = 21


if a > b and a > c:
    print('A é maior que - B e C')
elif b > a and b > c:
    print('B é maior que - A e C')    
elif c > a and c > b:
    print('C é maior que - A e B')  
elif a == b and a > c:
    print('A e B são = e maiores que - C')    
elif a == b and a < c:
    print('A e B são = e menores que - C')       
elif a == c and a > b:
    print('A e C são = e maiores que - B')
elif a == c and a < b:
    print('A e C são = e menores que - B')
elif b == c and b > a:
    print('B e C são = e maiores que - A')
elif b == c and b < a:
    print('B e C são = e menores que - A') 
elif a == b and b == c:
    print('A B C são iguais.... ')        
    

# -----------------------------===== programs ===================================





    
       














