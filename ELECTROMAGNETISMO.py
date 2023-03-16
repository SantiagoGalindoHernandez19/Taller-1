def calcularlongitudespectroelectromagnetico(frecuencia:float) -> float:
  velocidad : float = 299792,458 # velocidad de la luz [km/s]
frecuencia = float(input("Ingresa la frecuencia de la onda en Hz: "))

if frecuencia < 3**9:
    print("La onda se encuentra en la parte del espectro electromagnetico de banda de radio")
elif frecuencia < 3**12:
    print("La onda se encuentra en la parte del espectro electromagnetico de banda de microondas")
elif frecuencia < 4.3**14:
    print("La onda se encuentra en la parte del espectro electromagnetico de banda infrarroja")
elif frecuencia < 7.5**14:
    print("La onda se encuentra en la parte del espectro electromagnetico de banda visible")
elif frecuencia < 3**17:
    print("La onda se encuentra en la parte del espectro electromagnetico de banda ultravioleta")
elif frecuencia < 3**19:
    print("La onda se encuentra en la parte del espectro electromagnetico de banda de rayos X")
else:
    print("La onda se encuentra en la parte del espectro electromagnetico de 1banda de rayos gamma")