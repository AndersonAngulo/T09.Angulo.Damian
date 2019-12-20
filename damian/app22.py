import os
import libreria
#programa para calcular la altura maxima de un cuerpo cuando su movmiento es oarabolico
#
#input
velocidad_inicial=int(os.sys.argv[1])
gravedad=float(os.sys.argv[1])

#processing
altura_maxima=libreria.altura_maxima(velocidad_inicial,gravedad)

#output
print("la altura maxima alcanzada es de:", altura_maxima)
