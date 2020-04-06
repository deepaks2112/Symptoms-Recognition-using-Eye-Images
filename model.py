import tensorflow as tf
from tensorflow import keras
from keras.models import model_from_json
import cv2
import numpy as np
import os

def predict(weights,image):
	img=cv2.imread(image)
	img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	img=cv2.resize(img,(256,256))
	img=np.array(img,np.float64)
	img/=255

	json_file=open(weights,'r')
	loaded_model_json=json_file.read()
	json_file.close()
	disease_clf=model_from_json(loaded_model_json)

	label_pred=disease_clf.predict(img.reshape(1,256,256,3))
	clas=['Healthy','Thyroid','Conjunctivitis','Jaundice']
	inv_clas={'Healthy':0,'Thyroid':1,'Conjunctivitis':2,'Jaundice':3}
	print('The predicted label is: '+clas[np.argmax(label_pred)])
	print('Confidence scores: ')
	label_pred_i=[[label_pred[0][i],i] for i in range(4)]
	label_pred_i.sort(reverse=True)
	for score,idx in label_pred_i:
		print(clas[idx]+': '+str(score))
	return