import os
import libreria
#calcular la hipotenusa de un triangulo
#input
catA=int(os.sys.argv[1])
catB=int(os.sys.argv[2])

#
if(catA==catB):
    print("es un triangulo rectangulo notable de 45 45")
if(catA==2*catB):
    print("es un triangulo rectangulo notable de 30 60")
if(catA/catB==3/4):
    print("es un triangulo rectangulo notable de 37 53")
else:
    print("es un triangulo cualquiera")
#fin if

#processing
hipotenusa=libreria.calc_hipotenusa(catA,catB)

#output
print("la hipotenusa es igual a:", hipotenusa)