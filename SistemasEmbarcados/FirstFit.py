# First fit 
 
def firstFit(blockSize, m, processSize, n): 
      
    # Armazena o ID do bloco
    # bloco alocado para um processo 
    allocation = [-1] * n  
  
    #  Inicialmente nenhum bloco é atribuído a nenhum processo
  
    # escolha cada processo e encontre os blocos adequados
    # de acordo com o tamanho que o anúncio atribui a ele 
    for i in range(n): 
        for j in range(m): 
            if blockSize[j] >= processSize[i]: 
                  
                #  aloca o bloco j ao processo p [i]
                allocation[i] = j  
  
               # Reduza a memória disponível neste bloco.
                blockSize[j] -= processSize[i]  
  
                break

    #Nº do processo Tamanho do processo Nº do bloco.
    print(" Nº         Tamanho        Nº do bloco.") 

    for i in range(n): 
        print(" ", i + 1, "         ", processSize[i],  
                          "         ", end = " ")  
        if allocation[i] != -1:  
            print(allocation[i] + 1)  
        else: 
            print("Não alocado") 

#  codigo   
if __name__ == '__main__':  
    blockSize = [100, 500, 200, 300, 600]  
    processSize = [212, 417, 112, 426] 
    m = len(blockSize) 
    n = len(processSize) 
  
    firstFit(blockSize, m, processSize, n)             