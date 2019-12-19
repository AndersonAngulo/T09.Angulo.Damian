#funcion1
def factorial_numero(numero):
    factorial=1
    while numero>0:
        factorial=factorial*numero
        numero-=1
    return factorial
#funcion2
def saludar(nombre,animo):
    print("Hola",nombre)
    print("Te encuentras",animo,"\nEspero te sientas mucho mejor",nombre)

