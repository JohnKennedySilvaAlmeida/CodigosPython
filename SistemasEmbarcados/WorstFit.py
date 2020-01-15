#worst fit 
 
def worstFit(blockSize, m, processSize, n): 
      
    # Armazena a identificação do bloco
    # alocado para um processo
      
    # Inicialmente nenhum bloco é atribuído
    # para qualquer processo

    allocation = [-1] * n 
      
    # escolha cada processo e encontre os blocos adequados
    # de acordo com o tamanho que o anúncio atribui a ele
    for i in range(n): 
          
       # Encontre o melhor bloco de ajuste para
        # Processo atual
        wstIdx = -1
        for j in range(m): 
            if blockSize[j] >= processSize[i]: 
                if wstIdx == -1:  
                    wstIdx = j  
                elif blockSize[wstIdx] < blockSize[j]:  
                    wstIdx = j 
      
        # Se pudéssemos encontrar um bloco para
        # Processo atual
        if wstIdx != -1: 
              
            # aloca o bloco j ao processo p [i]
            allocation[i] = wstIdx  
  
            # Reduza a memória disponível neste bloco.
            blockSize[wstIdx] -= processSize[i] 

    # Nº do processo Tamanho do processo Nº do bloco.
    print("Nº       Tamanho    Nº do bloco.") 

    for i in range(n): 
        print(i + 1, "         ",  
              processSize[i], end = "     ")  
        if allocation[i] != -1: 
            print(allocation[i] + 1)  
        else: 
            print("Não alocado") 

# Codigo
if __name__ == '__main__': 
    blockSize = [100, 500, 200, 300, 600]  
    processSize = [212, 417, 112, 426]  
    m = len(blockSize)  
    n = len(processSize)  
  
    worstFit(blockSize, m, processSize, n)             