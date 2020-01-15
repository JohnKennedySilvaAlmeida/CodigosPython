import cv2
import os
import numpy as np


eigenface = cv2.face.EigenFaceRecognizer_create()
fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()

caminho_Fotos_Tiradas ='C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Fotos_Faces_Py' #caminho fotos tiradas 

def getImagemComId():# funcao para varer pasta com imagens e pegar id para treinamento 
	caminhos = [os.path.join(caminho_Fotos_Tiradas, f) for f in os.listdir(caminho_Fotos_Tiradas)]
	#caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]

	faces 	= []
	ids 	= []

	for caminhoImagem in caminhos:
		imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY ) 
			#Divide uma string em strings (split) type Array
		id = int(os.path.split(caminhoImagem)[-1].split('.')[1]) #obs!
			#print(id)

		ids.append(id) 
		faces.append(imagemFace) 

	return np.array(ids), faces

ids, faces = getImagemComId()

print("...Treinando...");

eigenface.train(faces, ids)
eigenface.write('C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Classifica_Faces_PY\\classificadorEigen.yml')
                        #caminhos classificadores - treinamento
fisherface.train(faces, ids)
fisherface.write('C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Classifica_Faces_PY\\classificadorFisher.yml')

lbph.train(faces, ids)
lbph.write('C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Classifica_Faces_PY\\classificadorLBPH.yml')

print("! Treinamento Realizado com Sucesso !")