import os
import libreria
#
#
#input
k=float((os.sys.argv[1]))
deformacion=float((os.sys.argv[2]))

#depndiendo de la constante k , mostrar de que material esta echo el resorte
if(k>0 and k<10):
    print("el resorte es de cobre")
if(k>10 and k<50):
    print("el resorte es de hierro")
if(k>50 and k<100):
    print("el resorte es de acero")
#processing
fuerza_elastica=libreria.fuerza_elastica(k,deformacion)

#output
print("la ferza elastica es igual a:", fuerza_elastica)