# -------------------------- FORMADOR PARA TODOS OS ALGORITMOS NO RECONHECIMENTO DE ROSTO -------------------------------------------

import os                                               # importing the OS for path
import cv2                                              # importing the OpenCV library
import numpy as np                                      # importing Numpy library
from PIL import Image                                   # importing Image library

EigenFace = cv2.face.EigenFaceRecognizer_create(15)
FisherFace = cv2.face.FisherFaceRecognizer_create(2)
LBPHFace = cv2.face.LBPHFaceRecognizer_create(1,1 ,7,7)

#EigenFace = cv2.face_EigenFaceRecognizer(15)   obs..!
#EigenFace = cv2.face.EigenFaceRecognizer_create(15)          # criando EIGEN FACE RECOGNISER

#FisherFace = cv2.face_FisherFaceRecognizer(2)  obs... !
#FisherFace = cv2.face.FisherFaceRecognizer_create(2)         # criando FISHER FACE RECOGNISER

#LBPHFace = cv2.face_LBPHFaceRecognizer(1,1, 7,7) obs ... !
#LBPHFace = cv2.face.LBPHFaceRecognizer_create(1, 1, 7,7)      # Criando LBPH FACE RECOGNISER

path = 'C:/Users/Jk_cu/OneDrive/Área de Trabalho/J k/Programs python JK/Master_Face/dataSet'

def getImageWithID (path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    FaceList = []
    IDs = []
    for imagePath in imagePaths:
        faceImage = Image.open(imagePath).convert('L')  # Abra a imagem e converta para cinza
        faceImage = faceImage.resize((110,110))         # redimensione a imagem para que o reconhecedor EIGEN possa ser treinado
        faceNP = np.array(faceImage, 'uint8')           # converter a imagem em matriz Numpy
        ID = int(os.path.split(imagePath)[-1].split('.')[1])    # Retrave o ID do array
        FaceList.append(faceNP)                         # Anexar a Matriz Numpy à lista
        IDs.append(ID)                                  # Anexar o ID à lista de IDs
        cv2.imshow('Training Set', faceNP)              # Mostrar as imagens na lista
        cv2.waitKey(1)
    return np.array(IDs), FaceList                      # Os IDs são convertidos em um array Numpy
IDs, FaceList = getImageWithID(path)

# ------------------------------------ TRADING O RECONHECEDOR ----------------------------------------
print('TRAINING......')
EigenFace.train(FaceList, IDs)                          # O promotor é treinado usando as imagens
print('EIGEN FACE RECOGNISER COMPLETE...')
EigenFace.save('Recogniser/trainingDataEigan.xml')
print('FILE SAVED..')
FisherFace.train(FaceList, IDs)
print('FISHER FACE RECOGNISER COMPLETE...')
FisherFace.save('Recogniser/trainingDataFisher.xml')
print('Fisher Face XML saved... ')
LBPHFace.train(FaceList, IDs)
print('LBPH FACE RECOGNISER COMPLETE...')
LBPHFace.save('Recogniser/trainingDataLBPH.xml')
print ('ALL XML FILES SAVED...')

cv2.destroyAllWindows()