# Definir la velocidad de la luz en m/s y la velocidad del sonido en el aire en m/s
velocidadDeLaLuz = 299792458
velocidadDelSonidoEnElAire = 343

distancia = float(input("Ingrese la distancia en metros: "))

tiempoLuz = distancia / velocidadDeLaLuz

tiempoSonido = distancia / velocidadDelSonidoEnElAire

velocidadVehiculoMasVeloz = 490.48 # velocidad en m/s
tiempoVehiculomasVeloz = distancia / velocidadVehiculoMasVeloz

velocidadBolt = 9.58  # velocidad en m/s
tiempoBolt = distancia / velocidadBolt

print("La luz tardaria", round(tiempoLuz, 20), "segundos.")
print("El sonido tardaria", round(tiempoSonido, 4), "segundos.")
print("El vehiculo comercial mas veloz tardaria", round(tiempoVehiculomasVeloz, 4), "segundos.")
print("Usain Bolt tardaria", round(tiempoBolt, 4), "segundos.")
