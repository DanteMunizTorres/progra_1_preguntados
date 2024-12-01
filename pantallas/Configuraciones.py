import pygame
from Constantes import *
from Funciones import *

pygame.init()

#CREAMOS BOTONES
boton_suma = crear_objeto(TAMAÑO_BOTON_VOLUMEN,COLOR_ROJO)
boton_resta = crear_objeto(TAMAÑO_BOTON_VOLUMEN,COLOR_ROJO)
boton_volver = crear_objeto((100,30),COLOR_AZUL)





def mostrar_ajustes(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "configuracion"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_suma["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                if datos_juego["volumen_musica"] < 100:
                    datos_juego["volumen_musica"] += 5
                else:
                    ERROR_SONIDO.play()
                print("SUMA VOLUMEN")
            elif boton_resta["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                if datos_juego["volumen_musica"] > 0:
                    datos_juego["volumen_musica"] -= 5
                else:
                    ERROR_SONIDO.play()
                print("RESTA VOLUMEN")
            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
                print("VUELVE AL MENU")
    
    pantalla.fill(COLOR_BLANCO)
    
    boton_resta["rectangulo"] = pantalla.blit(boton_resta["superficie"],(20,200))
    boton_suma["rectangulo"] = pantalla.blit(boton_suma["superficie"],(420,200))    
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    
    mostrar_texto(boton_suma["superficie"],"VOL+",(0,10),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(boton_resta["superficie"],"VOL-",(0,10),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(pantalla,f"{datos_juego['volumen_musica']} %",(200,200),FUENTE_50,COLOR_NEGRO)
    
    return retorno