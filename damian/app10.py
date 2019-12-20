import libreria
#calcular el volumen de cualquier prisma
import os

volumen=libreria.volumen_prisma(float(os.sys.argv[1]),float(os.sys.argv[2]))
print("El volumen es {}".format(volumen))