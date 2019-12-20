import os
import libreria
#programa para calcular la densidad de un cuerpo
#
#input
masa=int(os.sys.argv[1])
volumen=int(os.sys.argv[2])
#processing
densidad=libreria.densidad(masa,volumen)

#output
print("la densidad del cuerpo es:", densidad)