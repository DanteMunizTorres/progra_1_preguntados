import pygame
from Funciones import *
from Constantes import *
from pantallas.Menu import *
from pantallas.Juego import *
from pantallas.Configuraciones import *
from pantallas.Puntuaciones import *
from pantallas.Terminado import *

pygame.init()
pygame.display.set_caption("JUEGO 314")
icono = pygame.image.load("assets\images\icono_final.png")
pygame.display.set_icon(icono)
pantalla = pygame.display.set_mode(VENTANA)


corriendo = True
reloj = pygame.time.Clock()
datos_juego = {"puntuacion":0,"aciertos":CANTIDAD_ACIERTOS,"cantidad_vidas":CANTIDAD_VIDAS,"nombre":"","volumen_musica":100}
datos_juego["comodines"] = {
    'bomba':False,
    'x2' : False,
    'doble_chance': False,
    'pasar': False
}
ventana_actual = "menu"
bandera_juego = False




while corriendo:
    cola_eventos = pygame.event.get()
    reloj.tick(FPS)

    if ventana_actual == "menu":
        ventana_actual = mostrar_menu(pantalla,cola_eventos,fondo)
    elif ventana_actual == "juego":
        if bandera_juego == False:
            porcentaje_coma = datos_juego["volumen_musica"] / 100
            pygame.mixer.init()
            pygame.mixer.music.load("assets\sounds\musica_juego.mp3")
            pygame.mixer.music.set_volume(porcentaje_coma)
            pygame.mixer.music.play(-1)
            bandera_juego = True
        ventana_actual = mostrar_juego(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "configuracion":
        ventana_actual = mostrar_ajustes(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "puntuaciones":
        ventana_actual = mostrar_rankings(pantalla,cola_eventos)
    elif ventana_actual == "terminado":
        ventana_actual = mostrar_fin_juego(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "salir":
        corriendo = False
    
    pygame.display.flip()
pygame.quit()
    
    