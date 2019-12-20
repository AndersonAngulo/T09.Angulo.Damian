import os
import libreria

#simular el buscaddor por voz de google
#la frase es ok google, si escribes otra frase diferente a OK google simplemente no hace nada
#input
frase=os.sys.argv[1]
#si la frase dicha es ok google, mostrar escuchando
if(frase=="OK google"):
    print("Escuchando...")
if(frase=="OK GOOGLE"):
    print("Escuchando...")
if(frase=="ok google"):
    print("Escuchando...")
#fin if

#processing
frase_buscador=libreria.buscador_voz(frase)

#output
print("la frase coorecta es:", frase)