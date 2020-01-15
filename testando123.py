from class_cliente import Cliente
from class_pedido import Pedido
from classe_End_correios import Endereco


# criar instancia d cliente 

while True: # loop principal
   
    print('=-'*15)
    print('Menu'.center(20))
    print('[C] para continuar !')
    print('[S] para sair !') # menu pricipal 
    print()
    op = input('Digite Opção:')
    print()

    if op =='c' or op =='C': # opçoes - if 
        print('-=-=-= Cadastro - Cliente -=-=-=')
        cpf = input('Digite seu CPF:')
        nome = input('Digite seu nome:')
        credito = input('Digite o credito:')
       
        meuCliente = Cliente(cpf,nome,credito)#1 objs *
        try: # tratando erros 
            print('-=-=-= Cadastro - Endereço -=-=-=')
            cep = input('Digite o Cep:')
            num = input('Digite o Numero:')

            meuCliente.endereco = Endereco(cep,num)#2 objs *
        except:
            print("...Cep ou Numeros Invalidos...".center(100))
        
        meuPedido = Pedido(meuCliente)#3 objs *

        while True: #  2 loop - cadastro
            try: #tratando erros 
                print('-=-=-= Cadastro - Produtos -=-=-=')
                cod = int(input('Código:'))
                prod = str(input('Produto:'))
                qnd = int(input('Quantidade:'))
                prec = float(input('Preço:'))
                meuPedido.adicionarItem(cod,prod,qnd,prec)#3.1 objs * 
                op1 = input('Deseja Contunuar [s] ou [n] :')
                print('-='*15)

                if op1 =='s' or op1 =='S': print('Continue...')
                elif op1 =='n' or op1 =='N': break
                else: print('Opção Invalida'.center(60))        

            except:
                print(''' .. Atenção .. Digite apenas!
                    Codigos -  Numeros Inteiro
                    Produtos - Nomes [Letras]
                    Quantidades - Numeros Inteiro
                    Preço - Numeros Reais [0.0]
                                                '''.center(100))
          
        while True: # 3 looop remover itens 
            try:
                print('-=-= Remover Itens -=-=')
                remuve_cod = int(input('Codigo do Produto:'))
                meuPedido.removerItem(remuve_cod) #4 objs *
                op2 = input('Deseja Continuar [s] ou [n] :')
                print('-='*15)

                if op2 =='s' or op2 =='S': print('Continue...')
                elif op2 =='n' or op2 =='N': break
                else: print('Opção Invalida'.center(60))  
            except:
                print('''Erro... 
                       *Codigo apenas numeros inteiros
                                  ou
                       *Esse codigo não existe mais   ''')        




    elif op =='s' or op =='S':
        print('.. Processo Finalizado ..'.center(100)) # op - if - sair 
        break
   
    elif op !='s' and op !='S' and op !='c' and op != 'C': print('!Opção Invalida!'.center(100)) 
        # op - diferente - if 











# ---------------------------------------------------- -------------------------------------------#

'''meuCliente.endereco = ('892555750',123)#2
cep = input('Cep:')
numero = input('Numero:')
meuCliente.endereco = Endereco(cep,numero)#2

meuPedido = Pedido(meuCliente)#3
meuPedido.adicionarItem(1 cod,'arroz',10,7.10)#3'''
# falta
#total = meuPeido.getTotal() #4
#print(total{:.2f})

#meuPedido.removerItem(1) # 1cod    #5

#meuPedido.imprimir()  #6



