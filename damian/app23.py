import os
import libreria
#programa para calculara la energia potencial gravitatoria
#
#input
masa=int(os.sys.argv[1])
gravedad=float(os.sys.argv[2])
altura=int(os.sys.argv[3])
#processing
ener_pot=libreria.energ_pot_gravitatoria(masa,gravedad,altura)

#output
print("La energia potencial gravitatoria es igual a:", ener_pot)
