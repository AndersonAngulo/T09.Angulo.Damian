import os
import libreria
#ingresar clave WIFI
#si la clave es correcta, mostrar estableciendo conexion...
#input
clave=os.sys.argv[1]
clave_invalida=(clave!="123456E" and clave!="123456A" and clave!="123456D")

#mientras la clave sea incorrecta, pedir clave nuevamente
while(clave_invalida):
    clave=input("ingrese nuevamente:")
    clave_invalida=(clave!="123456E" and clave!="123456A" and clave!="123456D")

#
if(len(clave)==7):
    print("nro de caracteres completos")
else:
    print("Nro de caracteres incorrecto")
#fin if
#processing
clave_secreta=libreria.clave_secreta(clave)

#cada clave, tiene un determinado benefcio
#condicional
if(clave_secreta=="123456E"):
    print("Estableciendo conexion con 5MG/s de velocidad...")
if(clave_secreta=="123456A"):
    print("Estableciendo conexion con 10MG/s de velocidad...")
if(clave_secreta=="123456D"):
    print("Estableciendo conexion con 20MG/s de velocidad...")

#fin if

#output
print("La clave es:", clave_secreta)