import pygame
from Constantes import *
from Funciones import *

pygame.init()

fondo = pygame.image.load("assets\images\_fondo_ventanas.jpg")
fondo = pygame.transform.scale(fondo,VENTANA)

boton_volver = {}
boton_volver["superficie"] = pygame.image.load("assets\images\_posible_fondo_botones3.jpg")
boton_volver["superficie"] = pygame.transform.scale(boton_volver["superficie"],TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()


def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    retorno = "puntuaciones"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
    
    pantalla.blit(fondo,(0,0))
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))

    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_22_NEGRITA,COLOR_NEGRO)
    mostrar_texto(pantalla,f"ACA DEBEN MOSTRAR EL TOP 10",(20,200),FUENTE_32,COLOR_NEGRO)

    return retorno