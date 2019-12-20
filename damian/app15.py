import os
import libreria
#
#input
#programa para calcular el area lateral de un  triangulo
radio=int(os.sys.argv[1])
altura=int(os.sys.argv[2])

#processing
area_lateral_cil=libreria.area_lateral_cilindro(radio,altura)

#output
print("El area lateral del cilindro es:", area_lateral_cil)
