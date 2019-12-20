#para el primer ejercicio
def volumen_prisma(area_base,altura):
    while(area_base<0 or altura<0):
        print("Numeros invalidos")
        exit(1)
    volumen=area_base*altura
    return volumen


#fin def

#para el segundo ejercicio
#siendo la clave 123456E
#la longitud de la clave es 7 mostrar nro de caracteres completos
#caso contrario mostrar Nro de caracteres incorrecto

def clave_secreta(clave):
    return clave
#fin def

#para el tercer ejercicio
def buscador_voz(frase):
    if(len(frase)==9):
        return frase
#fin def

#para el ejercio 4
def calc_hipotenusa(catA,catB):

    hipotenusa=((catA**2 + catB**2)**(1/2))

    return hipotenusa
#fin def

#para el ejercicio 5
def area_trapezio(baseM,baseN,altura):
    area=(((baseM+baseN)/2)*altura)
    return area


#fin def

#para el ejercio 6
def nro_cell(numero):
    nro=str(numero)
    if(len(nro)==9):
        return "nro de digito correcto"
    else:
        return "nro de digitos es incorrecto"

#fin def

#para el ejercici 7
def volumen_esfera(radio):
    volumen_esf=(4/3*3.14*(radio)**3)
    if(volumen_esf>1000):
        return "la esfera es de volumen "+str(volumen_esf)+" es una esfera muy grande"
    else:
        return "la esfera de volumen "+str(volumen_esf)+" es una esfera de vol regular"

    #fin if

#fin def




#para el ejerciocio 8

def tiempo_encuentro(dist, vel1,vel2):
    suma_vel=vel1+vel2
    encuentro=((dist)/suma_vel)
    if(dist<0):
        return "verifique la distancia ingresada, algo esta mal"

    return "El encuentro es {}".format(encuentro)
#fi def

#para el ejerciocio 9
def tiempo_alcance(dist,vel1,vel2):
    diferencia_vel=vel2-vel1
    alcance=((dist)/diferencia_vel)
    if(dist<=0):
        return "verifique la distancia ingresada, algo esta mal"
    return "El alcanse es {}".format(alcance)
#fi def




#para el ejerciocio 10
#teniendo una recta y el valor de su pendiente, encontrar la pendiente de la recta perpendicular a esta.
def calc_pendiente(pendiente):
    pendiente_ortogonal=(-1/(pendiente))
    if(pendiente_ortogonal<0):
        return "valor: "+str(pendiente_ortogonal)+" la pendiente ortogonal es negativa"
    else:
        return "valor: "+str(pendiente_ortogonal)+" la pendiente ortogonal es positiva"
    return pendiente_ortogonal
#fin def

#para el ejerciocio 11
def horas_estudio(dia):
    return dia
#fin def

#para el ejerciocio 12
def vol_cono_circular(radio,altura,):
    volumen_cono=(1/3*3.14*(radio**2*altura))

    return volumen_cono

#para el ejerciocio 13
def volumen_cilindro(radio,altura):

    vol_cilindro=(3.14*(radio**2*altura))
    return vol_cilindro
#fin def

#para el ejerciocio 14
def area_elipse(A,B):
    area=(3.14*(A*B))

    return area
#fin def


#para el ejerciocio 15
def area_lateral_cilindro(radio,altura):
    area_lateral=(2*3.14*(radio)*(altura))
    return area_lateral
#fin def

#para el ejercicio 16
#si la arista es mayor a 100 metros entonces mostrar que es un cubo demaciado grande
def area_lateral_cubo(arista):
    area_lat_cubo=(6*arista**2)

    return area_lat_cubo
#fin def

#para el ejerciocio 17
#calcular la fuerza elastica de un resorte, la cual depende de una constante K variable y la deformacion que sufre
def fuerza_elastica(k,x):
    fuerza_elast=(k*x)
    return fuerza_elast
#fin def

#para el ejerciocio 18
def fuerza_rozamiento(u,N):
    fuerza_roz=(u*N)
    return fuerza_roz
#fin def

#para el ejerciocio 19
def precio_de_venta(pc,gan):
    precio_venta=(pc+gan)
    return precio_venta
#fin def

#para el ejercicio 20
def longitud_arco(angulo,radio):
    long_arco=(angulo*radio)
    return long_arco
#fin def

#para el ejercicio 21
def area_rombo(semieje1,eje):
    area_romb=(semieje1*eje)
    return area_romb
#fin_def

#para el ejercicio 22
#movimientto parabolico
def altura_maxima(velocidad_inicial,gravedad):
    altura=((velocidad_inicial**2)/(2*gravedad))
    return altura
#fin def

#para el ejercicio 23
def energ_pot_gravitatoria(m,g,h):
    energia_pot=(m*g*h)
    return energia_pot
#fin def

#para el ejercicio 24
def densidad(masa,volumen):
    densidad=(masa/volumen)
    return densidad
#fin def

#para el ejercicio 25
#programa que al ingresar una estacion
#te vote un rango de los mese que dura

def estacion(estacion_ano):
    estacion_ano=estacion_ano.upper()
    if(estacion_ano=="VERANO"):
        return "Verano comienza en \"Diciembre\" y termina en \Febrero\""
    if(estacion_ano=="OTONIO"):
        return "Otoño comienza en \"Febrero\" y termina en \"Mayo\""
    if(estacion_ano=="INVIERNO"):
        return "Invierno comienza en \"Mayo\" y termina en \"Septiembre\""
    if(estacion_ano=="PRIMAVERA"):
        return "Primavera comienza en \"Septiembre\" y termina en \"Diciembre\""
