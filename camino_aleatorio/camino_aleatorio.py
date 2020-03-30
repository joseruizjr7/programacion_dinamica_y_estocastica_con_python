from borracho import BorrachoTradicional, BienBorracho
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coord(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.camina(campo.obtener_coord(borracho))

def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    # borracho = tipo_de_borracho(BorrachoTradicional)
    borracho = tipo_de_borracho(BienBorracho)
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.agregar_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))
    
    return distancias

def graficar(x, y):
    grafica = figure(title='Camino Aleatorio')
    grafica.line(x, y, legend = 'distancia media')

    show(grafica)

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    distancias_medias_por_caminata = []

    # simula varias caminatas de diferentes distancias
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_medias_por_caminata.append(distancia_media)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Distancia media = {distancia_media}')
        print(f'Distancia maxima = {distancia_maxima}')
        print(f'Distancia minima = {distancia_minima}')

    graficar(distancias_de_caminata, distancias_medias_por_caminata)

if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 1000

    main(distancias_de_caminata, numero_de_intentos, BienBorracho)