# 1 Crie uma lista chamada Numeros com os itens [11, 12, 15, 19, 32, 44, 76, 99]
print("exe 1")

numeros = [11,12,15,19,32,44,76,99]

# 2 Modifique os itens da lista. Aqueles que forem maiores que 50, multiplique por 2.
#Aqueles que forem menores que 50, multiplique por 7.
print("exe 2")

for conta in numeros:
    print(conta)
    if conta > 50:
        print('Maiores que 50, mutiplicar * 2 -> ',conta*2)
    else:
        print('Menores que 50, mutiplicar * 7 -> ',conta*7)  

# 3 Identifique o último elemento da lista e imprima-o na frase “O número XX é o
#último elemento da lista”. 
print("exe 3")

print('Ultimo da lista é ',numeros[len(numeros)-1])

print(numeros[-1]) # ultimo elemnto

print(numeros[0]) # primeiro elemento

# 4 e 5 Crie uma nova lista com o segundo, terceiro e quarto elementos da lista Numeros.
#altere o sexto elemento da lista, substituindo-o por 100.
print("exe 4 e 5")

l = ['0',1,2,3,'4','5 xxxxxxxxx']
l[5] = 100
# *l elimina []
print(l)
# ---------------- outra forma 

# 4 
lis1 = ['0',1,2,3,'4','5']
elemento = (lis1[1:4])
print(elemento)

# 5 
lis1[5] = 100
print(lis1)



# 6 Leia o arquivo mailbox.txt e crie uma lista chamada Palavras com todas as
#palavras do arquivo.
print('exe 6 ')
#filee = open ('mailbox_123.txt','w')  criar - w 
#filee.close

arq_listas = open('mailbox_123.txt', 'r')
palavras = arq_listas.read().split(',\n') # palavras []lista       nao precisa \n 
arq_listas.close()

#print(palavras) lista[]

# 7 Conte o número de palavras que há na lista Palavras.
print('exe 7 ')
#import collections
#s = 'hhhhjjjj'            outra forma d contar --- obs
#c = collections.Counter(s)
#print(c.most_common())

arq1_listas = open('mailbox_123.txt', 'r')
palavras1 = arq1_listas.read()

#t = palavras1.count("")       1  - print(len(palavras1)) certo - contar  
 
#print('Total d palavras,',t)     

arq1_listas.close()

# 8 - Elimine da lista palavras todos os itens que possuem a palavra “java”.
print('exe 8 ')

for produt in palavras1:
    #print(produt)
    if produt =='java':               #    palvras1.remove('java')
       palavras1.remove(produt)

# print(palavras1)

#9 Crie uma nova lista com os primeiros 20 itens da lista Palavras, ordenados em
#ordem alfabética.
print('exe 9')

novalista = []

for i in range(20):
    novalista.append(palavras1[i])

novalista.sort()    

#10 Crie uma nova lista com os itens da lista Palavras que são um endereço de e-mail.
print('exe 10')

list_email = []

for p in palavras1:
    if p.count('@') > 0:
        list_email.append(p)

print(list_email)  


#11 Escreva um programa pedindo para o usuário digitar 5 números, armazene cada
#número digitado pelo usuário em uma lista, imprima o maior e o menor número.
print('exe 11')

try:
    n = []
    for i in range(5):
        n.append(int(input("Número: ")))
        if(n == ''):
            break
    
    print('Lista ',n) 
    print('Maior:',max(n))
    print('Menor:',min(n)) 

except:
    print('Erro !')      



     











   


      
      
     