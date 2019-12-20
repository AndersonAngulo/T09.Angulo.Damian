import os
import libreria
#
#programa para calcular el area de una elipse
#input
semiejeA=int(os.sys.argv[1])
semiejeB=int(os.sys.argv[2])
#
if(semiejeA==semiejeB):
        print("Este no es una elipse, es un circulo")
    #fin if
#processing
area_elipse=libreria.area_elipse(semiejeA,semiejeB)

#output
print("El area de la elipse es:", area_elipse)