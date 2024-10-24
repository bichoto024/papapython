# Este script resuelve el problema numero 3, el cual 
# describo a continuacion:

# Si corres una carrera de 10 kilómetros en 42 minutos con 
# 42 segundos, ¿Cuál es tu ritmo promedio 
# (tiempo por cada milla en minutos y segundos)? 
# ¿Cuál es tu rapidez promedio en millas por hora?

kilometros = 10
minutos = 42
segundos = 42
tiempo=(minutos*60)+segundos
millas = 1.61

km_a_millas=kilometros/millas
velocidad = km_a_millas/tiempo

print("El tiempo es: %s segundos" %  tiempo) 
print("%s Millas son 10 Kilometros" % km_a_millas)

#la velocidad esta en millas por segundos
print("La velocidad es: %s millas por segundos" % velocidad)
print ("\n")





