from Constantes import *
import random
import pygame

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


def crear_objeto (tamaño:tuple,color:tuple)->dict:
    
    objeto = {}
    objeto["superficie"] = pygame.Surface(tamaño)
    objeto["rectangulo"] = objeto["superficie"].get_rect()
    objeto["superficie"].fill(color)
    return objeto

def crear_cuadros(cantidad_cuadros:int,tamaño:tuple,color:tuple)->list:
    lista = []
    for i in range (cantidad_cuadros):
        objeto = {}
        objeto["superficie"] = pygame.Surface(tamaño)
        objeto["rectangulo"] = objeto["superficie"].get_rect()
        objeto["superficie"].fill(color)
        lista.append(objeto)
    return lista

def crear_objeto_imagen(imagen:str,tamaño:tuple)->dict:
    objeto = {}
    objeto["superficie"] = pygame.image.load(imagen)
    objeto["superficie"] = pygame.transform.scale(objeto["superficie"],tamaño)
    objeto["rectangulo"] = objeto["superficie"].get_rect()
    return objeto

def crear_comodines()->list:
    lista_comodines = crear_cuadros(4,TAMAÑO_COMODIN,COLOR_VIOLETA)
    comodines_ids = [COMODIN_BOMBA, COMODIN_X2, COMODIN_CANCHE_EXTRA, COMODIN_PASAR,]
    for index, comodin in enumerate(lista_comodines):
        comodin["utilizado"] = False
        comodin['id'] = comodines_ids[index]
    return lista_comodines
    

def usar_comodin_bomba(datos_juego, lista_respuestas, pregunta_actual):
    if datos_juego['comodines']['bomba']:
        datos_juego['comodines']['bomba'] = False  # Desactiva el comodín
        # Filtra las respuestas incorrectas
        respuestas_incorrectas = [
            idx for idx, respuesta in enumerate(lista_respuestas)
            if idx + 1 != pregunta_actual["respuesta_correcta"]
        ]
        # Elimina dos respuestas incorrectas
        for idx in random.sample(respuestas_incorrectas, 2):
            lista_respuestas[idx]["superficie"].fill(COLOR_GRIS)
            lista_respuestas[idx]["rectangulo"] = pygame.Rect(0, 0, 0, 0)


def usar_comodin_x2(datos_juego):
    if datos_juego['comodines']['x2']:
        datos_juego['comodines']['x2'] = False  # Desactiva el comodín
        return True  # Señal para doblar los puntos
    return False