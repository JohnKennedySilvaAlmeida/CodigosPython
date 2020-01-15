#Função necessaria p/ passo 1,2,3

import cv2 #Video Capture Library 
import math # Image Rotation Library
import time #Time count Library
import os # Files Library

now_time = time.clock() # Rélogio de ponto

#caminhos arquivos | Haarcascade  
face = cv2.CascadeClassifier('C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Haar\\haarcascade_frontalcatface.xml')
glass_cas = cv2.CascadeClassifier('C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Haar\\haarcascade_eye_tree_eyeglasses.xml')

#caminho nomes de Usuarios cadastrados 
names_TXT =('C:\\Users\\Jk_cu\\OneDrive\\Documentos\\NOMES_CAPTURA.txt')

WHITE = [255, 255, 255]  #BRANCO


def FileRead(): #Arquivo lido
    Info = open(names_TXT, "r")                      # Abrir o arquivo de texto no modo de leitura
    NAME = []                                        # A tupla para armazenar nomes
    while (True):                     # Leia todas as linhas no arquivo e armazene-as em duas tuplas
        Line = Info.readline()
        if Line == '':
            break                   #[0] ou 1
        NAME.append(Line.split(",")[1].rstrip())  # - OBS!!!
       
    return NAME                                     # Devolva as duas tuplas
        
Names = FileRead()                                 # Execute a função acima para obter o ID e nomes Tuple

#     ------------------- FUNÇÃO PARA ENCONTRAR O NOME  -----------------------------------------------------------

# Verificação do último ID em Names.txt - last_string
def file_is_empty(path):
    return os.stat(path).st_size==0

with open(names_TXT) as f:
    lines = f.readlines()
    if file_is_empty(names_TXT):
        last_string = 1
    else:
        last_row = lines[-1]
        string_last = last_row  
        for s in string_last.split(): 
            if s.isdigit():
                last_string = int(s)     # quantidade de pessoas cadastradas 
                print("A base possui: " + str(last_string) + " " + "pessoas." )

def ID2Name(ID, conf):          #OBS !!
        # id >= 1
    if ID >= 1 and ID <= last_string: # add - nome e id  
        NameString = ("Nome:" + Names[ID-1] + " |Confidence: " + (str(round(conf))) )   # Encontre o nome usando o índice do ID
    else:                         # id - 1  ou  id ou id + 1
        NameString = ("Rosto não Reconhecido !")                          #Encontre o nome usando o índice do ID

    return NameString

#     ------------------- ESTA FUNÇÃO LER O ARQUIVO E ADICIONAR O NOME AO FIM DO ARQUIVO  -----------------

def AddName():   # adicionar nomes + ID
    Name = input('Digite seu nome:')
    #notificarUsuario = input("Email:")#aqui********************************
    Info = open(names_TXT, "r+")      # OBS !!! Msm apagando Txt aposicao fica e causa erro Index ***
    ID = ((sum(1 for line in Info))+1)
    Info.write(str(ID) + " " + "," + " " + Name + "\n")
    print ("Nome armazenado em:" + str(ID))
    Info.close()
    return ID

#     ------------------- DESENHE A CAIXA EM TORNO DO ROSTO, ID E CONFIANÇA ou CONFIDENCE  -------------------------------------


def DispID(x, y, w, h, NAME, Image):

    #  --------------------------------- A POSIÇÃO DA CAIXA DE IDENTIFICAÇÃO  ---------------------------------------------

    Name_y_pos = y - 10
    Name_X_pos = x + w/2 - (len(NAME)*7/2)

    if Name_X_pos < 0:
        Name_X_pos = 0
    elif (Name_X_pos +10 + (len(NAME) * 7) > Image.shape[1]):
          Name_X_pos= Name_X_pos - (Name_X_pos +10 + (len(NAME) * 7) - (Image.shape[1]))
    if Name_y_pos < 0:
        Name_y_pos = Name_y_pos = y + h + 10
          
 #  ------------------------------------   O DESENHO DA CAIXA E ID  --------------------------------------
    
    draw_box(Image, x, y, w, h)
    
    #cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), (0,0,0), -2)              
    cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), (0,0,0), -2)
    cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), WHITE, 1) # Desenhe um retângulo preto sobre o rosto
    cv2.putText(Image, NAME, (int(Name_X_pos), int(Name_y_pos - 10)), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)                         # Imprimir o nome do ID


def draw_box(Image, x, y, w, h):
    cv2.line(Image, (x, y), (x + (int(w/5)) ,y), WHITE, 2)
    cv2.line(Image, (x+((int(w/5)*4)), y), (x+w, y), WHITE, 2)
    cv2.line(Image, (x, y), (x, y+(int(h/5))), WHITE, 2)
    cv2.line(Image, (x+w, y), (x+w, y+int((h/5))), WHITE, 2)
    cv2.line(Image, (x, (y+int((h/5*4)))), (x, y+h), WHITE, 2)
    cv2.line(Image, (x, (y+h)), (x + int((w/5)) ,y+h), WHITE, 2)
    cv2.line(Image, (x+(int((w/5)*4)), y+h), (x + w, y + h), WHITE, 2)
    cv2.line(Image, (x+w, (y+int((h/5*4)))), (x+w, y+h), WHITE, 2)


# ---------------    SEGUNDA CAIXA DE IDENTIFICAÇÃO     ----------------------
def DispID2(x, y, w, h, NAME, Image):

#  --------------------------------- A POSIÇÃO DA CAIXA DE IDENTIFICAÇÃO -------------------------------------------------        

    Name_y_pos = y - 40
    Name_X_pos = x + w/2 - (len(NAME)*7/2)

    if Name_X_pos < 0:
        Name_X_pos = 0
    elif (Name_X_pos +10 + (len(NAME) * 7) > Image.shape[1]):
          Name_X_pos= Name_X_pos - (Name_X_pos +10 + (len(NAME) * 7) - (Image.shape[1]))
    if Name_y_pos < 0:
        Name_y_pos = Name_y_pos = y + h + 10
          
 #  ------------------------------------    O DESENHO DA CAIXA E ID  --------------------------------------
    cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), (0,0,0), -2)
    cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), WHITE, 1)  # Desenhe um retângulo preto sobre o rosto
    cv2.putText(Image, NAME, (int(Name_X_pos), int(Name_y_pos - 10)), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)                         # Imprimir o nome do ID


# ---------------     TERCEIRA CAIXA DE IDENTIFICAÇÃO     ----------------------
def DispID3(x, y, w, h, NAME, Image):

#  --------------------------------- A POSIÇÃO DA CAIXA DE IDENTIFICAÇÃO -------------------------------------------------        

    Name_y_pos = y - 70
    Name_X_pos = x + w/2 - (len(NAME)*7/2)

    if Name_X_pos < 0:
        Name_X_pos = 0
    elif (Name_X_pos +10 + (len(NAME) * 7) > Image.shape[1]):
          Name_X_pos= Name_X_pos - (Name_X_pos +10 + (len(NAME) * 7) - (Image.shape[1]))
    if Name_y_pos < 0:
        Name_y_pos = Name_y_pos = y + h + 10
          
 #  ------------------------------------    O DESENHO DA CAIXA E ID   --------------------------------------
    cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), (0,0,0), -2)
    cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), WHITE, 1)# Desenhe um retângulo preto sobre o rosto
    cv2.putText(Image, NAME, (int(Name_X_pos), int(Name_y_pos - 10)), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)                         # Imprimir o nome do ID


def DrawBox(Image, x, y, w, h):
    cv2.rectangle(Image, (x, y), (x + w, y + h), (255, 255, 255), 1)     # Desenhe um retângulo em volta do rosto

# ----------------------------- ESTA FUNÇÃO TOMA ESPECIAL CASCATA, FACE CASCATA E UMA IMAGEM
# ------------------------- ELE RETORNA UM ROSTO CROPIDO E SE POSSIBILIDADE RETA A INCLINAÇÃO DA CABEÇA


def DetectEyes(Image):
    Theta = 0
    rows, cols = Image.shape
    glass = glass_cas.detectMultiScale(Image)                                               # Isso ditects os olhos
    for (sx, sy, sw, sh) in glass:
        if glass.shape[0] == 2:                                                             # A imagem deve ter 2 olhos
            if glass[1][0] > glass[0][0]:
                DY = ((glass[1][1] + glass[1][3] / 2) - (glass[0][1] + glass[0][3] / 2))    # Diferença de altura entre o vidro
                DX = ((glass[1][0] + glass[1][2] / 2) - glass[0][0] + (glass[0][2] / 2))    # Diferença de largura entre o vidro
            else:
                DY = (-(glass[1][1] + glass[1][3] / 2) + (glass[0][1] + glass[0][3] / 2))   # Diferença de altura entre o vidro
                DX = (-(glass[1][0] + glass[1][2] / 2) + glass[0][0] + (glass[0][2] / 2))   # Diferença de largura entre o vidro

            if (DX != 0.0) and (DY != 0.0):                                                 # Certifique-se de que a mudança aconteça apenas se houver um ângulo
                Theta = math.degrees(math.atan(round(float(DY) / float(DX), 2)))            # Encontre o ângulo
                print ("Calculando " + str(Theta))
                #print ("Theta  " + str(Theta))

                M = cv2.getRotationMatrix2D((cols / 2, rows / 2), Theta, 1)                 # Encontre a matriz de rotação
                Image = cv2.warpAffine(Image, M, (cols, rows))
                # cv2.imshow('ROTATED', Image)                                              # DESAPARECIMENTO SE VOCÊ QUER VER O

                Face2 = face.detectMultiScale(Image, 1.3, 5)                                # Isso detecta um rosto na imagem
                for (FaceX, FaceY, FaceWidth, FaceHeight) in Face2:
                    CroppedFace = Image[FaceY: FaceY + FaceHeight, FaceX: FaceX + FaceWidth]
                    return CroppedFace

def tell_time_passed():
    print ('TEMPO PASSOU ' + str(round(((time.clock() - now_time)/60), 2)) + ' MINS')
