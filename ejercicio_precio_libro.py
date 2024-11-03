# Author: Matias Miranda Martinez
# Date: November 3, 2024
# This script resolve the excercise 2.2,2 in the page 15
# 
#
# Supongamos que el precio original de un libro es $24.95, 
# pero las librerías obtienen un 40 % de descuento. 
# El envío cuesta $3 para la primera copia y 75 centavos por cada copia adicional.
# ¿Cuál es el costo al por mayor para 60 copias?


precio_libro = 24.95
procentaje_descuento = 0.6
costo_descuento_libro = precio_libro * procentaje_descuento
costo_envio_1_copia = 3
costo_envio_copia_adicional = 0.75
copias = 60
costo_60_copias = (copias * costo_descuento_libro)
costo_60_copias_con_envio = costo_60_copias + costo_envio_1_copia + (costo_envio_copia_adicional * (copias - 1))


print ("El costo de 60 libros con 40 porciento de descuento es de %s" % costo_60_copias)

print ("El costo de 60 libros con 40 porciento de descuento con envio es de %s" % costo_60_copias_con_envio)