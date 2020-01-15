# Recursividade 

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum
print(listsum([1,3,5,7,9]))
# 1 ---------------------------------------
def listsum1(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum1(numList[1:])
print(listsum1([1,3,5,7,9]))
# 2 -----------------------------------------------------
def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]
print(toStr(1453,16))
# 3 _---------------------------------------------------
def fibonacci(indice):
    if indice == 1 or indice == 2:
        return 1
    return fibonacci(indice - 1) + fibonacci(indice - 2)
print(fibonacci(5))   
# 4 --------------------------------------------------------------
def fat(n):
    resultado = 1
    while n > 0:
        resultado = resultado * n
        n = n - 1
    return resultado
print("Fatorial de 3:", fat(3)) 
# 5 -----------------------------------------------------------------
def Fibonacc(n):
    if n <= 1:
        return n
    else:
        return Fibonacc(n-1) + Fibonacc(n-2)
print('Fibonacc = ' + str(Fibonacc(9)) )
# 6 -------------------------------------------------------------
def Fatoriall(n):
    if n == 1:
        return 1
    else:
        return n * Fatoriall(n-1) 
print(Fatoriall(int(input("Digite o fatorial:"))))     
# 7 -------------------------------------------------------------

def string(palavra,n):
    if n < 50:
        print(string(palavra,n + 1))
    return palavra 

#print(string('John',0))
a = str(input("Digite seu nome:"))

print(string(a,0))
         