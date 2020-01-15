try:
    print('Olar Mundo')
    print(3*'jk\n')

    a = int(input('A - Digite um numero:'))
    b = int(input('B - Digite um numero:'))
    

    if (a > b):
        print('B menor que A')
    else: 
        print('B maior que A')  

    res = a * b
    res1 = a / b
    res2 = a - b

    print('Result,',res)
    print('Result,',res1)
    print('Result,',res2)

except:
    print('Não sei o que houve!!! ??')
finally:
    print('Topp')   



    