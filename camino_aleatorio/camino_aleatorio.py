from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coord(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.camina(campo.obtener_coord(borracho))

def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(BorrachoTradicional)
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.agregar_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))
    
    return distancias

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    # simula varias caminatas de diferentes distancias
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Distancia media = {distancia_media}')
        print(f'Distancia maxima = {distancia_maxima}')
        print(f'Distancia minima = {distancia_minima}')

if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100

    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)