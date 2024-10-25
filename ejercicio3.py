###########################################################################
# Este script resuelve el problema numero 3, el cual 
# describo a continuacion:
#
# Si corres una carrera de 10 kilómetros en 42 minutos con 
# 42 segundos, ¿Cuál es tu ritmo promedio 
# (tiempo por cada milla en minutos y segundos)? 
# ¿Cuál es tu rapidez promedio en millas por hora?
###########################################################################


# Declaro mis variables
kilometros = 10
minutos = 42
segundos = 42
millas = 1.61

# Declaro mis formulas
tiempo=(minutos*60)+segundos
km_a_millas=kilometros/millas
velocidad = km_a_millas/tiempo

#########################
#
# Imprimo mis resultados
#
#########################

print("El tiempo es: %s segundos" %  tiempo) 
print("%s Millas son 10 Kilometros" % km_a_millas)

#la velocidad esta en millas por segundos
print("La velocidad es: %s millas por segundos" % velocidad)
print ("\n")

# ToDo:
# Para convertir de millas por segundo a millas por hora, 
# multiplicamos la velocidad en millas por segundo por 3600, ya que una hora tiene 3600 segundos.
# Terminar la convesiion, aqui pongo lo que me hace falta implementar:
# 0.0024243482139826703millas/segundo×3600segundos/hora=8.727653570337613millas/hora
# Así que 
# 0.0024243482139826703
# 0.0024243482139826703 millas por segundo es aproximadamente 8.73 millas por hora.


