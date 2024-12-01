import pygame 
from Constantes import *
from Funciones import *

pygame.init()

lista_botones = crear_cuadros(4,TAMAÑO_BOTON,COLOR_NEGRO)
    
def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
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
   
                
    pantalla.fill(COLOR_BLANCO)
    lista_botones[BOTON_JUGAR]["rectangulo"] = pantalla.blit(lista_botones[BOTON_JUGAR]["superficie"],(125,115))
    lista_botones[BOTON_AJUSTES]["rectangulo"] = pantalla.blit(lista_botones[BOTON_AJUSTES]["superficie"],(125,195))
    lista_botones[BOTON_RANKINGS]["rectangulo"] = pantalla.blit(lista_botones[BOTON_RANKINGS]["superficie"],(125,275))
    lista_botones[BOTON_SALIR]["rectangulo"] = pantalla.blit(lista_botones[BOTON_SALIR]["superficie"],(125,355))
        
    mostrar_texto(lista_botones[BOTON_JUGAR]["superficie"],"JUGAR",(75,20),FUENTE_30,COLOR_BLANCO)
    mostrar_texto(lista_botones[BOTON_AJUSTES]["superficie"],"AJUSTES",(60,20),FUENTE_30,COLOR_BLANCO)
    mostrar_texto(lista_botones[BOTON_RANKINGS]["superficie"],"RANKINGS",(50,20),FUENTE_30,COLOR_BLANCO)
    mostrar_texto(lista_botones[BOTON_SALIR]["superficie"],"SALIR",(75,20),FUENTE_30,COLOR_BLANCO)
    
    return retorno
