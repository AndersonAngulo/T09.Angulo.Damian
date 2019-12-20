import os
import libreria
#calcular el volumen de un cono
#
#input
radio=int(os.sys.argv[1])
altura=int(os.sys.argv[2])
#

#processing
volumen_cono=libreria.vol_cono_circular(radio,altura)
if(volumen_cono>10000):
    print("es una gran cono")
#output
print("el volumen es igual a:", volumen_cono)