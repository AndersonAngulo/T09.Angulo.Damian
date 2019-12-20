import os
import libreria
#programa para calcular la fuerza de rozamiento que ejerce la superficie sobre un cuerpo
#
#input
u=float(os.sys.argv[1])
normal=float(os.sys.argv[2])
#dependiendo de la constante u, obtener un diagnostico de la superficie
if(u==0):
    print("no hay rozamiento, la superficie es lisa")
if(u>0 and u<10):
    print("la superficie es aspera")
if(u>10):
    print("la superficie es muy aspera")
#processing
fuerza_roz=libreria.fuerza_rozamiento(u,normal)

#output
print("La fuerza de rozamiento es igual a:", fuerza_roz)