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