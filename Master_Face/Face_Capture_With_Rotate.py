#ISTO É USADO PARA CAPTURAR LOJA AS FOTOS PARA TREINAR OS SISTEMAS DE RECONHECIMENTO DE FACE 
# ADIÇÕES ESPECIAIS SÃO FEITAS PARA SALVAR IMAGENS SOMENTE COM ILUMINAÇÃO CORRECTA
# E CABEÇAS INCLINADAS CORRECAS 


import cv2                  # Importing the opencv
import numpy as np          # Import Numarical Python
import NameFind             # Import NameFind function           OBS! funçao 

WHITE = [255, 255, 255]

#   importe as cascatas de Haar para a detecção de faces
face_cascade = cv2.CascadeClassifier('C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Haar_Faces_PY\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Haar_Faces_PY\\haarcascade_eye.xml')  #obs caminho 

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_test.xml') # Classifier "frontal-face" Haar Cascade
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree.xml') # Classifier "eye" Haar Cascade

caminho_Fotos_Tiradas ='C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Fotos_Faces_Py\\User.'	

ID = NameFind.AddName() #funcao 

Count = 0
cap = cv2.VideoCapture(0)                                                                           # Camera object

while Count < 50:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                                    # Converta a câmera para grayScale
    if np.average(gray) > 10:                                                                      # Testando o brilho da imagem
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)                                         # Detecte os rostos e guarde as posições
        for (x, y, w, h) in faces:                                                                  # Molduras LOCAL X, Y LARGURA, ALTURA
            FaceImage = gray[y - int(h / 2): y + int(h * 1.5), x - int(x / 2): x + int(w * 1.5)]    # O rosto é isolado e cortado
            Img = (NameFind.DetectEyes(FaceImage))#aqui funcao 
            cv2.putText(gray, "FACE DETECTED", (x+int((w/2)), y-5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)
            if Img is not None:
                frame = Img                                                                         # Mostrar os rostos detectados
            else:
                frame = gray[y: y+h, x: x+w]
            cv2.imwrite(caminho_Fotos_Tiradas + str(ID) + "." + str(Count) + ".jpg", frame)
            cv2.waitKey(300)
            cv2.imshow("CAPTURED PHOTO", frame)                                                     # mostra a imagem capturada
            Count = Count + 1
    cv2.imshow('Face Recognition System Capture Faces', gray)                                       # Mostre o vídeo
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print ('FACE CAPTURE FOR THE SUBJECT IS COMPLETE')
cap.release()
cv2.destroyAllWindows()
