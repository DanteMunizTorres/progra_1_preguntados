import pygame
from Constantes import *
from Funciones import *
from utils.files_management import obtener_estadisticas

pygame.init()

fondo = pygame.image.load("assets\images\_fondo_ventanas.jpg")
fondo = pygame.transform.scale(fondo,VENTANA)

boton_volver = {}
boton_volver["superficie"] = pygame.image.load("assets\images\_posible_fondo_botones3.jpg")
boton_volver["superficie"] = pygame.transform.scale(boton_volver["superficie"],TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()



lista_partidas = obtener_estadisticas()
partidas_obtenidas_flag = False

def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    global lista_partidas
    global partidas_obtenidas_flag
    ventana_actual = "puntuaciones"

    if not partidas_obtenidas_flag:
        partidas_obtenidas_flag = True
        lista_partidas = obtener_estadisticas()
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            ventana_actual = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                partidas_obtenidas_flag = False
                ventana_actual = "menu"
    
    pantalla.blit(fondo,(0,0))
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))

    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_22_NEGRITA,COLOR_NEGRO)
    # mostrar_texto(pantalla,f"ACA DEBEN MOSTRAR EL TOP 10",(20,200),FUENTE_32,COLOR_NEGRO)
    for index, partida in enumerate(lista_partidas):
        cuadro_partida = crear_objeto(PUNTUACION_TEXTO, COLOR_BLANCO)
        y_pos = 100 + index * 44
        mostrar_texto(cuadro_partida["superficie"], f"{partida["nombre"]}: {partida["puntuacion"]} puntos. {partida["fecha"]}",(10,10),FUENTE_17,COLOR_NEGRO)
        cuadro_partida["rectangulo"] = pantalla.blit(cuadro_partida["superficie"], (25, y_pos))
        # pygame.draw.rect(pantalla,COLOR_BLANCO,cuadro_partida["rectangulo"],2)

    return ventana_actual