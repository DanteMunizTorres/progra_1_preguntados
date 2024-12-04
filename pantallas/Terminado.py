import pygame 
from Constantes import *
from Funciones import *

pygame.init()

fondo = pygame.image.load("assets\images\_fondo_ventanas.jpg")
fondo = pygame.transform.scale(fondo,VENTANA)

game_over = pygame.image.load("assets\images\_game_over.png")
game_over = pygame.transform.scale(game_over,(400,250))

cuadro_texto = {}
#cuadro_texto ["superficie"] = pygame.Surface(CUADRO_TEXTO)
cuadro_texto["superficie"] = pygame.image.load("assets\images\_posible_fondo_botones3.jpg")
cuadro_texto["superficie"] = pygame.transform.scale(cuadro_texto["superficie"],CUADRO_TEXTO)
cuadro_texto["rectangulo"] = cuadro_texto["superficie"].get_rect()
#cuadro_texto["superficie"].fill(COLOR_AZUL)
nombre = ""

def mostrar_fin_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global nombre
    retorno = "terminado"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif evento.type == pygame.KEYDOWN:
            #caracter = chr(evento.key)
            tecla_presionada = pygame.key.name(evento.key)
            bloc_mayus = pygame.key.get_mods() and pygame.KMOD_CAPS
            print(tecla_presionada)
            # print(evento.key)
            
            if tecla_presionada == "backspace" and len(nombre) > 0:
                #nombre = 'Mariano' -> 'Marian'
                nombre = nombre[0:-1]
                cuadro_texto["superficie"] = pygame.image.load("assets\images\_posible_fondo_botones3.jpg")
                cuadro_texto["superficie"] = pygame.transform.scale(cuadro_texto["superficie"],CUADRO_TEXTO)
                #cuadro_texto["superficie"].fill(COLOR_AZUL)
                #Si su superficie parte de una imagen
                #Tienen que cargar la imagen de nuevo y reescalarla
            
            if tecla_presionada == "space":
                nombre += " "
            
            if len(tecla_presionada) == 1:
                if bloc_mayus != 0:
                    nombre += tecla_presionada.upper()
                else:
                    nombre += tecla_presionada
        
    
    pantalla.blit(fondo,(0,0))
    pantalla.blit(game_over,(50,0))
    cuadro_texto["rectangulo"] = pantalla.blit(cuadro_texto["superficie"],(100,400))
    mostrar_texto(cuadro_texto["superficie"],nombre,(10,0),FUENTE_30,COLOR_NEGRO)
    mostrar_texto(pantalla,f"USTED OBTUVO:\n {datos_juego["puntuacion"]} PUNTOS",(100,250),FUENTE_40_NEGRITA,COLOR_BLANCO)
    
    return retorno