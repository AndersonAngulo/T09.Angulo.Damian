import os
import libreria
#programa que me recuerde cuantas horas debo estudiar segun el dia
#input
dia=os.sys.argv[1]
#cuantas horas debo estudiar

horas=0
if(dia=="lunes"):
    print("hoy debes estudiar 4 horas")
    horas=4
if(dia=="martes"):
    print("hoy debes estudiar 6 horas")
    horas=6
if(dia=="miercoles"):
    print("hoy debes estudiar 8 horas")
    horas=8
if(dia=="jueves"):
    print("hoy debes estudiar 3 horas")
    horas=3
if(dia=="viernes"):
    print("hoy debes estudiar 9 horas")
    horas=9
if(dia=="sabado"):
    print("hoy debes estudiar 12 horas")
    horas=12
if(dia=="domingo"):
    print("hoy debes estudiar 12 horas sin descanso")
    horas=12
#processing
horas=libreria.horas_estudio(dia)

print("te reitero que hoy debes estudiar:", horas, " horas" )