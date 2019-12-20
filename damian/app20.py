import os
import libreria
#programa para hallar la longitud de arco deuna circunferencia
#
#input
angulo=int(os.sys.argv[1])
radio=int(os.sys.argv[2])

#processing
longitud_de_arco=libreria.longitud_arco(angulo,radio)

#mientras el radio sea invalido
radio_invalido=(radio<0)
while(radio_invalido):
    radio=int(input("ingresar radio:"))
    radio_invalido=(radio<0)
#output
print("la longitud de arco es:", longitud_de_arco)