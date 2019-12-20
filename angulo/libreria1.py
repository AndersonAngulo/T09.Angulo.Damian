# funcion1
def factorial_numero(numero):
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial


# funcion2
def saludar(nombre, animo):
    print("Hola", nombre)
    print("Te encuentras", animo, "\nEspero te sientas mucho mejor", nombre)


# funcion3
def numero_dni(numero):
    numero_invalido = (len(numero) != 8 or numero.isdigit() == False)
    while (numero_invalido == True):
        numero = input("ingrese numero de DNI valido:")
        numero_invalido = (len(numero) != 8 or numero.isdigit() == False)
    return (numero)


# funcion4
def promedio_notas(a, b, c):
    a_invalido = (a < 0 or a > 20)
    b_invalido = (a < 0 or a > 20)
    c_invalido = (a < 0 or a > 20)
    while (a_invalido == True):
        a = int(input("ingrese nota 1(0-20):"))
        a_invalido = (a < 0 or a > 20)
    while (b_invalido == True):
        b = int(input("ingrese nota 2(0-20):"))
        b_invalido = (b < 0 or b > 20)
    while (a_invalido == True):
        c = int(input("ingrese nota 3(0-20):"))
        c_invalido = (c < 0 or c > 20)
    return ((a + b + c) / 3)


# funcion5
def resta_positiva(a, b):
    if (a > b):
        return (a - b)
    if (b > a):
        return (b - a)


# funcion6
def producto(a, b, c):
    if (a == 0):
        return (b * c)
    if (b == 0):
        return (a * c)
    if (c == 0):
        return (a * b)
    return(a*b*c)

#funcion 7
def division_entera(a,b):
    a_invalido=(a % b!=0 or b>a)
    while(a_invalido==True):
        a=int(input("Ingrese valor de a:"))
        a_invalido = (a % b!=0 or b>a)
    return(a/b)

#funcion 8
def charla(nombre,lugar):
    print("Hola",nombre)
    print("Como estas?")
    animo=input().lower()
    if(animo=="bien"):
        print("Que bueno que estes",animo)
    if (animo=="mal"):
        print("Espero te encuntres mejor")
    print("Te diriges a ",lugar,"\nQue te vaya muy bien")
#funcion9
def ruc(numero):
    numero_invalido = (len(numero) != 11 or numero.isdigit() == False)
    while(numero_invalido==True):
        numero=input("Ingrese numero de RUC:")
        numero_invalido = (len(numero) != 11 or numero.isdigit() == False)
    return (numero)
#funcion 10
def numero_celular(cel):
    cel_invalido = (len(cel) != 9 or cel.startswith("9")==False or cel.isdigit() == False)
    while (cel_invalido == True):
        cel = input("Ingrese numero de celular :")
        cel_invalido = (len(cel) != 9 or cel.startswith("9") == False or cel.isdigit() == False)
    if(len(cel)==9):
        print("Tu numero de celular es:")
    return (cel)
#funcion 11
def numero_telefonico(tel):
    tel_invalido = (len(tel) != 6  or tel.isdigit() == False)
    while (tel_invalido == True):
        tel = input("Ingrese numero de celular :")
        tel_invalido = (len(tel) != 6 or tel.isdigit() == False)
    if(len(tel)==9):
        print("Tu numero de telefono es:")
    return (tel)
#funcion 12
def placa(numero):
    numero_invalido=numero[0:4].isdigit()==False or numero[5:8].isdigit()==True or len(numero)!=8
    while (numero_invalido == True):
        numero = input("Ingrese numero de placa(1234-abc) :")
        numero_invalido = numero[0:4].isdigit() == False or numero[5:8].isdigit() == True or len(numero)!=8
    return(numero)
