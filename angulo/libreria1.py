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
