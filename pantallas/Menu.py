import pygame 
from Constantes import *
from Funciones import *

pygame.init()

fondo = pygame.image.load("assets\images\_fondo_ventanas.jpg")
fondo = pygame.transform.scale(fondo,VENTANA)


lista_botones = []

for i in range(4):
    boton = {}
    boton["superficie"] = pygame.Surface(TAMAÑO_BOTON)
    boton["superficie"] = pygame.image.load("assets\images\_posible_fondo_botones3.jpg")
    boton["superficie"] = pygame.transform.scale(boton["superficie"],TAMAÑO_BOTON)
    boton["rectangulo"] = boton["superficie"].get_rect()

    lista_botones.append(boton)
    
def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],fondo) -> str:
    retorno = "menu"
    pygame.display.set_caption("MENU")


    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if lista_botones[BOTON_JUGAR]["rectangulo"].collidepoint(evento.pos):
                retorno = "juego"
                CLICK_SONIDO.play()
            elif lista_botones[BOTON_AJUSTES]["rectangulo"].collidepoint(evento.pos):
                retorno = "configuracion"
                CLICK_SONIDO.play()
            if lista_botones[BOTON_RANKINGS]["rectangulo"].collidepoint(evento.pos):
                retorno = "puntuaciones"
                CLICK_SONIDO.play()
            if lista_botones[BOTON_SALIR]["rectangulo"].collidepoint(evento.pos):
                retorno = "salir"
                CLICK_SONIDO.play()
   
    pantalla.blit(fondo,(0,0))
       
    # pantalla.fill(COLOR_BLANCO)
    lista_botones[BOTON_JUGAR]["rectangulo"] = pantalla.blit(lista_botones[BOTON_JUGAR]["superficie"],(125,115))
    lista_botones[BOTON_AJUSTES]["rectangulo"] = pantalla.blit(lista_botones[BOTON_AJUSTES]["superficie"],(125,195))
    lista_botones[BOTON_RANKINGS]["rectangulo"] = pantalla.blit(lista_botones[BOTON_RANKINGS]["superficie"],(125,275))
    lista_botones[BOTON_SALIR]["rectangulo"] = pantalla.blit(lista_botones[BOTON_SALIR]["superficie"],(125,355))
        
    mostrar_texto(lista_botones[BOTON_JUGAR]["superficie"],"JUGAR",(75,10),FUENTE_30,COLOR_NEGRO)
    mostrar_texto(lista_botones[BOTON_AJUSTES]["superficie"],"AJUSTES",(60,10),FUENTE_30,COLOR_NEGRO)
    mostrar_texto(lista_botones[BOTON_RANKINGS]["superficie"],"RANKINGS",(50,10),FUENTE_30,COLOR_NEGRO)
    mostrar_texto(lista_botones[BOTON_SALIR]["superficie"],"SALIR",(75,10),FUENTE_30,COLOR_NEGRO)
    
    return retorno
