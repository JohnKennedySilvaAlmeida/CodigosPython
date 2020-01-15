# Best - Fit  
  
# Função para alocar memória para blocos
# conforme o algoritmo de melhor ajuste
def bestFit(blockSize, m, processSize, n): 
      
    # Armazena a identificação do bloco
    # alocado para um processo
    allocation = [-1] * n  
      
    #escolha cada processo e considere adequado
    # blocos de acordo com o tamanho do anúncio
    # atribuir a ele
    for i in range(n): 
          
       # Encontre o melhor bloco de ajuste para
        # Processo atual
        bestIdx = -1
        for j in range(m): 
            if blockSize[j] >= processSize[i]: 
                if bestIdx == -1:  
                    bestIdx = j  
                elif blockSize[bestIdx] > blockSize[j]:  
                    bestIdx = j 
    
        # Se pudéssemos encontrar um bloco para
        # Processo atual
        if bestIdx != -1: 
              
            # aloca o bloco j ao processo p [i]
            allocation[i] = bestIdx  
  
            # Reduza a memória disponível neste bloco. 
            blockSize[bestIdx] -= processSize[i] 
  
    #nº d processo \Tamanho do processo\ Nº do bloco.
    print("Nº        Tamanho      Nº do bloco.") 
    for i in range(n): 
        print(i + 1, "         ", processSize[i],  
                                end = "         ")  
        if allocation[i] != -1:  
            print(allocation[i] + 1)  
        else: 
            print("Não alocado") 

# Código do driver
if __name__ == '__main__':  
    blockSize = [100, 500, 200, 300, 600]  
    processSize = [212, 417, 112, 426]  
    m = len(blockSize)  
    n = len(processSize)  
  
    bestFit(blockSize, m, processSize, n) 