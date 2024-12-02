import pygame 
from Constantes import *
from Funciones import *

input_texto = {}
input_texto["superficie"] = pygame.Surface(INPUT_TEXTO)
input_texto["rectangulo"] = input_texto["superficie"].get_rect() 
input_texto["superficie"].fill(COLOR_BLANCO)

boton_continuar = {}
boton_continuar["superficie"] = pygame.Surface(TAMAÑO_BOTON)
boton_continuar["rectangulo"] = boton_continuar["superficie"].get_rect()
boton_continuar["superficie"].fill(COLOR_AZUL)



def mostrar_fin_juego(pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event], datos_juego:dict) -> str:
    '''Muestra la pantalla de fin del juego donde se carga el nombre y se muestra la puntuación obtenida'''
    print('mostrar_fin_juego --- check')

    ventana_actual = "terminado"
    print('mostrar_fin_juego --- cola_eventos:', cola_eventos)
    print('mostrar_fin_juego --- datos_juego:', datos_juego)

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            ventana_actual = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_continuar["rectangulo"].collidepoint(evento.pos):
                if len(datos_juego["nombre"].strip()) == 0:
                    ERROR_SONIDO.play()
                    
                else:
                    # guardar estadistica de jugador 
                    ventana_actual = "menu"
                    CLICK_SONIDO.play()
            
        
        elif evento.type == pygame.KEYDOWN:
            #caracter = chr(evento.key)
            tecla_presionada = pygame.key.name(evento.key)
            bloc_mayus = pygame.key.get_mods() and pygame.KMOD_CAPS
            print('tecla_presionada:',tecla_presionada)
            print('nombre:',datos_juego["nombre"]) # aca logueo a nombre como un string vacío. No me muestra lo que veo en pantalla que son efectivamente las letras que escribía antes. Queda siempre como vacío
            print('len(nombre):',len(datos_juego["nombre"]))
            print('tecla_presionada == "backspace":',tecla_presionada == "backspace")
            print('tecla_presionada == "backspace" and len(nombre) > 0:',tecla_presionada == "backspace" and len(datos_juego["nombre"]) > 0)
            # print(evento.key)
            
            if tecla_presionada == "backspace" and len(datos_juego["nombre"]) > 0: # borrar
                print('Borrando -----------------------------------------------------------------------------')
                datos_juego["nombre"] = datos_juego["nombre"][0:-1]
                print('Borrando nombre:', datos_juego["nombre"])

            elif len(datos_juego["nombre"]) >= 16:
                ERROR_SONIDO.play()
                # pass
            
            elif tecla_presionada == "space":
                datos_juego["nombre"] += " "
            
            elif len(tecla_presionada) == 1:
                if bloc_mayus != 0:
                    datos_juego["nombre"] += tecla_presionada.upper()
                else:
                    datos_juego["nombre"] += tecla_presionada
                    print(f"Nombre después de agregar carácter: {datos_juego["nombre"]}")
        
    
    pantalla.fill(COLOR_VIOLETA)
    input_texto["rectangulo"] = pantalla.blit(input_texto["superficie"],(25,200))
    boton_continuar["rectangulo"] = pantalla.blit(boton_continuar["superficie"],(125,355))

    input_texto["superficie"].fill(COLOR_BLANCO)
    mostrar_texto(input_texto["superficie"], datos_juego["nombre"],(10,0), FUENTE_40, COLOR_AZUL)

    pygame.draw.rect(pantalla, COLOR_NEGRO, input_texto["rectangulo"], 3)
    mostrar_texto(pantalla,f"USTED OBTUVO {datos_juego["puntuacion"]} PUNTOS",(25,50),FUENTE_40,COLOR_BLANCO)
    mostrar_texto(boton_continuar["superficie"],"CONTINUAR",(50,12),FUENTE_30,COLOR_BLANCO)
    
    return ventana_actual