valores = input().split()

tempo_de_viagem = int(valores[0])
velociadade_media = int(valores[1])

KILOMETRO_LITRO = 12

distancia = tempo_de_viagem*velociadade_media

litros_necessarios = float(distancia/KILOMETRO_LITRO)

print("{:.3f}".format(litros_necessarios))