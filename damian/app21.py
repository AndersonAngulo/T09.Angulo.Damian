import os
import libreria
#programa para calcular el area de un rombio
#
#input
semieje=int(os.sys.argv[1])
eje=int(os.sys.argv[1])

#processing
area_rombo=libreria.area_rombo(semieje,eje)

#output
print("el area del rombo es:", area_rombo)