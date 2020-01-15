#Capturar faces e add nome e guarda em uma pasta ...

import cv2 
import numpy as np


#treinamento de detecção de (face e olho)
classificador = cv2.CascadeClassifier('C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Haar_Faces_PY\\haarcascade_frontalface_default.xml')
classificadorOlho = cv2.CascadeClassifier('C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Haar_Faces_PY\\haarcascade_eye.xml')  #obs caminho 

#caminho obs
caminho_Fotos_Tiradas ='C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Fotos_Faces_Py\\Pessoa,'	

camera = cv2.VideoCapture(0)

amostra = 1
numeroDeAmostras = 25  #fotos tiradas quantidade
id = input('Digite seu indentificador: ')# id usuario 
largura, altura = 220, 220

print("Capturanda as faces...")

def fontes_Escritas(): 
	#captura / formatos / cv2.putText
	f1 = cv2.FONT_HERSHEY_SIMPLEX
	f2 = cv2.FONT_HERSHEY_COMPLEX
	f3 = cv2.FONT_HERSHEY_COMPLEX_SMALL
	f4 = cv2.FONT_HERSHEY_DUPLEX
	f5 = cv2.FONT_HERSHEY_PLAIN
	f6 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
	f7 = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
	f8 = cv2.FONT_HERSHEY_TRIPLEX
	f9 = cv2.FONT_ITALIC

	return f9


#loop Principal 
while (True):
	
	conectado, imagem = camera.read()
		#Detectar face na imagem
	imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) 
		#Esacala da imagem e tamanho para detecção de face
	facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(150,150))
	
		#Marcando o rosto da imagem
	for (x, y, l, a) in facesDetectadas:
		 	#Escrevendo de baixo da face mensagem
		cv2.putText(imagem,'Capturando...',(x - 20,y + a + 63), fontes_Escritas(), 1,(255,0,0),3,cv2.LINE_AA)
			#Verificando a face
		cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
			#Verificando se face tem olhos
		regiao = imagem[y:y + a, x:x + l]
		
		regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)# olhos 
		olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)

			# verificando ser tem olhos 
		for (ox, oy, ol, oa) in olhosDetectados:
			cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)

			if cv2.waitKey(1) & 0xFF == ord('c' or 'C'): #(0)
				if np.average(imagemCinza) > 10:
					imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
						#cv2.imwrite(caminho_Fotos_Tiradas + str(amostra) +"."+ str(id) + '.jpg', imagemFace) #grava aqui
					cv2.imwrite(caminho_Fotos_Tiradas + str(id) + '.' + str(amostra) + '.jpg', imagemFace) #grava aqui
						#	'fotos'- caminho   !!     #cv2.imwrite - grava imagem 
					print("[foto " + str(amostra) + " capturada com sucesso]")
					amostra += 1

		#Mostra a imagem capturada
	cv2.imshow("Face", imagem)
		#Mostra a imagem em tempo 
	cv2.waitKey(1)
	if(amostra >= numeroDeAmostras + 1): break

print('-'*31)
print(" Fotos capturadas com sucesso ...")
	#Liberar a memoria 
camera.release()

cv2.destroyAllWindows()



	
	
