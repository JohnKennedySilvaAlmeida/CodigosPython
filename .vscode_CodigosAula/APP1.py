from classe_End_correios import Endereco

try:
    
    while True:
        print()
        print('Cep [Correios]'.center(50))
        print()
        print('Menu'.center(50))
        print('(1) - Para Consultar'.center(50))
        print('(2) - Para Sair'.center(46))
        op = int(input('Opção:'))
        
        if op == 1: 
            c = input('Digite o CEP:')
            n = input('Digite o Numero:')
            Ed = Endereco(c,n)
            #Ed = Endereco('89259210','123')
            #print(Ed)#
        elif op == 2:
            print('Finalizado o Processo!'.center(50))   
            break 
        elif op != 1 or op != 2:
            print('Opção Invalida!'.center(50))    

        print('_____________ Resultado ________________')
        print('|Uf:',Ed.getEstado())
        print('|City:',Ed.getCidade())
        print('|Rua:',Ed.getRua())
        print('|Numero:',Ed.getNumero())
        print('|Cep:',Ed.getCep())
        print('-----------------------------------------')
        
except:
    print('...Erro! Cep ou Numeros Incorretos...'.center(100))    


# obs -----------------------------
'''import pycep_correios

endereco = pycep_correios.consultar_cep('37503130')

print(endereco['end'])
print(endereco['bairro'])
print(endereco['cidade'])
print(endereco['complemento'])
print(endereco['complemento2'])
print(endereco['uf'])
print(endereco['cep'])'''

# ---------------------------------------------- obs 


 