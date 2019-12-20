import os
import libreria
#programa para calcular el precio de venta de un producto
#
#input
precio_costo=int(os.sys.argv[1])
ganancia=int(os.sys.argv[2])

#
if(ganancia>100):
    print("El producto puede hacerle un desuento hasta del 10%")
if(ganancia==0):
    print("este producto, no te genera ingresos, ¡ya no vendas este tipo de productos!")
#processing
precio_venta=libreria.precio_de_venta(precio_costo,ganancia)

#output
print("El precio de venta del producto es:", precio_venta)