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
pantalla = pygame.display.set_mode(VENTANA)
corriendo = True
reloj = pygame.time.Clock()
datos_juego = {"puntuacion":0,"cantidad_vidas":CANTIDAD_VIDAS,"nombre":"","volumen_musica":100, "game_over": False}
ventana_actual = "menu"
# ventana_actual = "terminado" # mockup
bandera_juego = False

terminado_music_on = False

while corriendo:
    #Gestion de Eventos -> No lo programamos aca
    #Actualizacion de estados -> No lo programamos aca
    #Imprimir en pantalla esa informacion -> No lo programamos aca
    cola_eventos = pygame.event.get()
    reloj.tick(FPS)

    if ventana_actual == "menu":
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
    elif ventana_actual == "juego":
        if bandera_juego == False:
            porcentaje_coma = datos_juego["volumen_musica"] / 100
            pygame.mixer.init()
            pygame.mixer.music.load("assets/sounds/musica.mp3")
            pygame.mixer.music.set_volume(porcentaje_coma)
            pygame.mixer.music.play(-1)
            bandera_juego = True
        ventana_actual = mostrar_juego(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "configuracion":
        ventana_actual = mostrar_ajustes(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "puntuaciones":
        ventana_actual = mostrar_rankings(pantalla,cola_eventos)
    elif ventana_actual == "terminado":
        if terminado_music_on == False:
            terminado_music_on = True
            musica = "assets\sounds\game_over.mp3"
            if datos_juego['game_over'] == False:
                musica = "assets\sounds\game_won.mp3"
            pygame.mixer.music.load(musica)
            pygame.mixer.music.set_volume(datos_juego["volumen_musica"] / 120)
            pygame.mixer.music.play(-1)
        ventana_actual = mostrar_fin_juego(pantalla, cola_eventos, datos_juego)
    elif ventana_actual == "salir":
        corriendo = False
    
    pygame.display.flip()
pygame.quit()
    
    