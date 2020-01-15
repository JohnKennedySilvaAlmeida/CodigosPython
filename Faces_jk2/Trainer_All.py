#2 passo 

import os                                               #  OS for path
import cv2                                              #  OpenCV library
import numpy as np                                      #  Numpy library
from PIL import Image                                   #  Image library


EigenFace = cv2.face.EigenFaceRecognizer_create(15)      # criando EIGEN FACE RECOGNISER
FisherFace = cv2.face.FisherFaceRecognizer_create(2)     # Criando FISHER FACE RECOGNISER
LBPHFace = cv2.face.LBPHFaceRecognizer_create(1, 1, 7,7) # Criando LBPH FACE RECOGNISER

path ='C:\\Users\\Jk_cu\\OneDrive\\Documentos\\dataSet'   #caminho para as fotos

def getImageWithID (path): # funcão p/ pegar fotos e nomes e Ids
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    FaceList = []
    IDs = []
    for imagePath in imagePaths:
        faceImage = Image.open(imagePath).convert('L')  # Abra a imagem e converta para cinza
        faceImage = faceImage.resize((110,110))         # redimensione a imagem para que o reconhecedor EIGEN possa ser treinado
        faceNP = np.array(faceImage, 'uint8')           #converter a imagem em matriz Numpy
        ID = int(os.path.split(imagePath)[-1].split('.')[1])    # Retrave o ID do array
        FaceList.append(faceNP)                         # Anexar a Matriz Numpy à lista
        IDs.append(ID)                                  # Anexar o ID à lista de IDs
        #cv2.imshow('Conjunto de Treinamento', faceNP)              # Mostrar as imagens na lista
        ###cv2.imshow('Conjunto de Treinamento',ID)
        cv2.waitKey(1)
    
    return np.array(IDs), FaceList                      # Os IDs são convertidos em um array Numpy

IDs, FaceList = getImageWithID(path)

# ------------------------------------ TRADING O RECONHECEDOR ----------------------------------------
print('.....TREINAMENTO.....');

EigenFace.train(FaceList, IDs)                          # O promotor é treinado usando as imagens
print('1 - EIGEN FACE RECOGNISER COMPLETO.')
T1 = ('C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Recogniser\\trainingDataEigan.xml')
EigenFace.save(T1)
print('ARQUIVOS SALVOS.')

FisherFace.train(FaceList, IDs)
print('2 - FISHER FACE RECOGNISER COMPLETO.')
T2 = ('C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Recogniser\\trainingDataFisher.xml') #CAMINHO DO ARQUIVOS
FisherFace.save(T2)
print('XML DO FISHER FACE SALVOS.')

LBPHFace.train(FaceList, IDs)
print('3 - LBPH FACE RECOGNISER COMPLETO.')
T3 = ('C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Recogniser\\trainingDataLBPH.xml')
LBPHFace.save(T3)
print ('TODOS ARQUIVOS XML SALVOS.')

cv2.destroyAllWindows()