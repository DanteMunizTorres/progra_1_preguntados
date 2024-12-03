import pygame
from Constantes import *
from Funciones import *

musica_activa = True
pygame.init()

#CREAMOS BOTONES
boton_suma = crear_objeto(TAMAÑO_BOTON_VOLUMEN,COLOR_ROJO)
boton_resta = crear_objeto(TAMAÑO_BOTON_VOLUMEN,COLOR_ROJO)
boton_volver = crear_objeto((100,30),COLOR_AZUL)
boton_volumen_silenciado = crear_objeto_imagen("assets\images\mute.png",(25,25))
boton_volumen = crear_objeto_imagen("assets\images\sound.png",(25,25))
boton_rect = boton_rect = pygame.Rect(470, 770, 25, 25)






def mostrar_ajustes(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "configuracion"
    global musica_activa
    for evento in cola_eventos:
        
        if evento.type == pygame.QUIT:
            retorno = "salir"
        
        elif evento.type == pygame.MOUSEBUTTONDOWN:

            if boton_rect.collidepoint(evento.pos):
                    if musica_activa:
                        datos_juego["volumen_musica"] = 0
                        
                    else:
                        datos_juego["volumen_musica"] = 100
                        
                    musica_activa = not musica_activa
            
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
    boton_imagen = boton_volumen["superficie"] if musica_activa else boton_volumen_silenciado["superficie"]
    pantalla.blit(boton_imagen, boton_rect.topleft)
    
    
    
    mostrar_texto(boton_suma["superficie"],"VOL+",(0,10),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(boton_resta["superficie"],"VOL-",(0,10),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(pantalla,f"{datos_juego['volumen_musica']} %",(200,200),FUENTE_50,COLOR_NEGRO)
    
    return retorno