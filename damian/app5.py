import os
import libreria
#calcular el area de un un trapezio

#input
bM=int(os.sys.argv[1])
bN=int(os.sys.argv[2])
alt=int(os.sys.argv[3])
#
if(bM==bN):
    print("Este no es un trapezio")
    area=print("no es un trapezio, por lo tanto no hay area")
else:
    print("Este es un trapezio")

#processing
area_trapezio=libreria.area_trapezio(bM,bN,alt)

#output.
print("el area del trapezio es:", area_trapezio)
