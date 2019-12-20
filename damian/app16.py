import os
import libreria
#programa para calcular el area lateral de un cubo expresado en metros cuadrados

#input
arista=int(os.sys.argv[1])
if(arista>100):
    print("es un cubo demaciado grande")
#processing
area_lat_cubo=libreria.area_lateral_cubo(arista)

#output
print("el area lateral del cubo es:", area_lat_cubo," metros cuadrados")
