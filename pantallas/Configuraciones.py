import pygame
from Constantes import *
from Funciones import *

musica_activa = True
pygame.init()

fondo = pygame.image.load("assets\images\_fondo_ventanas.jpg")
fondo = pygame.transform.scale(fondo,VENTANA)

# boton_suma = {}
# boton_suma["superficie"] = pygame.image.load("assets\images\_volumen_alto.png")
# boton_suma["superficie"] = pygame.transform.scale(boton_suma["superficie"],TAMAÑO_BOTON_VOLUMEN)
# boton_suma["rectangulo"] = boton_suma["superficie"].get_rect()

# boton_resta = {}
# boton_resta["superficie"] = pygame.image.load("assets\images\_volumen_bajo.png")
# boton_resta["superficie"] = pygame.transform.scale(boton_resta["superficie"],TAMAÑO_BOTON_VOLUMEN)
# boton_resta["rectangulo"] = boton_resta["superficie"].get_rect()

# boton_volver = {}
# boton_volver["superficie"] = pygame.image.load("assets\images\_posible_fondo_botones3.jpg")
# boton_volver["superficie"] = pygame.transform.scale(boton_volver["superficie"],TAMAÑO_BOTON_VOLVER)
# boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()


#CREAMOS BOTONES
boton_suma = crear_objeto_imagen("assets\images\_volumen_alto.png",TAMAÑO_BOTON_VOLUMEN)
boton_resta = crear_objeto_imagen("assets\images\_volumen_bajo.png",TAMAÑO_BOTON_VOLUMEN)
boton_volver = crear_objeto_imagen("assets\images\_posible_fondo_botones3.jpg",TAMAÑO_BOTON_VOLVER)
boton_volumen_silenciado = crear_objeto_imagen("assets\images\mute.png",(30,30))
boton_volumen = crear_objeto_imagen("assets\images\sound.png",(30,30))
boton_rect = boton_rect = pygame.Rect(470, 770, 30, 30)

def mostrar_ajustes(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "configuracion"
    global musica_activa
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
    
    
    pantalla.blit(fondo,(0,0))
    
    boton_resta["rectangulo"] = pantalla.blit(boton_resta["superficie"],(20,150))
    boton_suma["rectangulo"] = pantalla.blit(boton_suma["superficie"],(420,150))    
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    boton_imagen = boton_volumen["superficie"] if musica_activa else boton_volumen_silenciado["superficie"]
    pantalla.blit(boton_imagen, boton_rect.topleft)

    
    
    
    # mostrar_texto(boton_suma["superficie"],"",(0,10),FUENTE_22,COLOR_NEGRO)
    # mostrar_texto(boton_resta["superficie"],"",(0,10),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_22_NEGRITA,COLOR_NEGRO)
    mostrar_texto(pantalla,f"{datos_juego["volumen_musica"]} %",(200,150),FUENTE_50_NEGRITA,COLOR_NEGRO)
    
    return retorno