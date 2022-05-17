#Dibujar y escribir en una imagen, y segmentar en región de interés
#Sandra Daniela Resendiz Alvarado

import cv2
import numpy as np
from matplotlib import pyplot as plt #parte visual
from matplotlib import pylab 

imagen=cv2.imread("playa.jpg")
xa=300 #area de interes
xb=500
ya=200
yb=600
area = imagen[xa:xb,ya:yb]
gris = cv2.cvtColor(area, cv2.COLOR_BGR2GRAY) 
cambio = cv2.cvtColor(gris,cv2.COLOR_GRAY2BGR)
imagen[xa:xb,ya:yb] = cambio
fig = plt.figure(figsize=(10,7), constrained_layout=True)

imagen = cv2.circle(imagen,(2800,800), 200, (45,255,255), -1) #circulo

imagen = cv2.rectangle(imagen,(210,360),(300,500),(255,0,0),5) #rectangulo

font = cv2.FONT_HERSHEY_SIMPLEX #texto
cv2.putText(imagen,'DANIELA RESENDIZ ALVARADO 19110325',(40,90), font, 3,(255,255,255),2,cv2.LINE_AA)
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
plt.imshow(imagen)
plt.axis('off')
plt.title("Playa")
plt.show()
