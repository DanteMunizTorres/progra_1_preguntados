import pygame 
import random
from Constantes import * 
from Funciones import *
# from data.Preguntas import *
from utils.files_management import parsear_archivo_preguntas



pygame.init()

#CREO CUADROS DE PREGUNTAS, RESPUESTAS Y BOTONES INTERACTIVOS

boton_volumen_silenciado = crear_objeto_imagen("assets\images\mute.png",(25,25))
boton_volumen = crear_objeto_imagen("assets\images\sound.png",(25,25))
boton_rect = boton_rect = pygame.Rect(470, 770, 25, 25)
cuadro_pregunta = crear_objeto(TAMAÑO_PREGUNTA,COLOR_NEGRO)
lista_respuestas = crear_cuadros(4,TAMAÑO_RESPUESTA,COLOR_NEGRO)
lista_preguntas = parsear_archivo_preguntas()
musica_activa = True
vida_extra = False

    
indice = 0 #Son inmutables
bandera_respuesta = False #Son inmutables
random.shuffle(lista_preguntas)

def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global indice
    global bandera_respuesta
    global musica_activa
    global vida_extra

    retorno = "juego"
    if bandera_respuesta:
        pygame.time.delay(250)
        
        cuadro_pregunta["superficie"] = pygame.image.load("assets/images/fondo.jpg")
        cuadro_pregunta["superficie"] = pygame.transform.scale(cuadro_pregunta["superficie"],TAMAÑO_PREGUNTA)
        for i in range(len(lista_respuestas)):
            lista_respuestas[i]["superficie"].fill(COLOR_AZUL)
        bandera_respuesta = False
    
    pregunta_actual = lista_preguntas[indice]
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            
            if boton_rect.collidepoint(evento.pos):
                    if musica_activa:
                        pygame.mixer_music.pause()
                        
                    else:
                        pygame.mixer.music.unpause()
                        
                    musica_activa = not musica_activa
            for i in range(len(lista_respuestas)):
                

                if lista_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                    respuesta_seleccionada = (i + 1)
                    print("respuesta_seleccionada:", respuesta_seleccionada)
                    print("pregunta_actual[respuesta_correcta]:", pregunta_actual["respuesta_correcta"])
                    
                    if respuesta_seleccionada == pregunta_actual["respuesta_correcta"]:
                        ACIERTO_SONIDO.play()
                        print("RESPUESTA CORRECTA")
                        lista_respuestas[i]["superficie"].fill(COLOR_VERDE_OSCURO)
                        datos_juego["puntuacion"] += PUNTUACION_ACIERTO
                        datos_juego["aciertos"] += 1
                        vida_extra = True
                    else:
                        ERROR_SONIDO.play()
                        lista_respuestas[i]["superficie"].fill(COLOR_ROJO)
                        if datos_juego["puntuacion"] > 0:
                            datos_juego["puntuacion"] -= PUNTUACION_ERROR
                        datos_juego["cantidad_vidas"] -= 1
                        vida_extra = False

                    if datos_juego["aciertos"] == 5 and vida_extra == True:
                        datos_juego["cantidad_vidas"] += 1
                    elif datos_juego["cantidad_vidas"] == 0:
                        retorno = "terminado"    
                    
                    indice += 1
                    

                    if indice == len(lista_preguntas):
                        indice = 0
                        random.shuffle(lista_preguntas)
                        
                        
                    bandera_respuesta = True
                
                    

    
    pantalla.fill(COLOR_BLANCO)
   
    #MOSTRAR TEXTO DENTRO DE LOS CUADROS Y BOTONES
    mostrar_texto(cuadro_pregunta["superficie"],f"{pregunta_actual['pregunta']}",(20,20),FUENTE_27,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[0]["superficie"],f"{pregunta_actual['respuesta_1']}",(20,20),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[1]["superficie"],f"{pregunta_actual['respuesta_2']}",(20,20),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[2]["superficie"],f"{pregunta_actual['respuesta_3']}",(20,20),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[3]["superficie"],f"{pregunta_actual['respuesta_4']}",(20,20),FUENTE_22,COLOR_BLANCO)

    #MOSTRAR CUADROS EN PANTALLA    
    cuadro_pregunta["rectangulo"] = pantalla.blit(cuadro_pregunta["superficie"],(80,80))
    lista_respuestas[0]["rectangulo"] = pantalla.blit(lista_respuestas[0]["superficie"],(75,245))#r1
    lista_respuestas[1]["rectangulo"] = pantalla.blit(lista_respuestas[1]["superficie"],(75,345))#r2
    lista_respuestas[2]["rectangulo"] = pantalla.blit(lista_respuestas[2]["superficie"],(75,445))#r3
    lista_respuestas[3]["rectangulo"] = pantalla.blit(lista_respuestas[3]["superficie"],(75,545))#r4
    boton_imagen = boton_volumen["superficie"] if musica_activa else boton_volumen_silenciado["superficie"]
    pantalla.blit(boton_imagen, boton_rect.topleft)
    
    #CREAR RECTANGULOS INTERACTIVOS
    pygame.draw.rect(pantalla,COLOR_NEGRO,cuadro_pregunta["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[0]["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[1]["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[2]["rectangulo"],2)
    
    #MUESTRO INFORMACIÓN DEL JUEGADOR
    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(10,10),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,f"VIDAS: {datos_juego['cantidad_vidas']}",(10,40),FUENTE_25,COLOR_NEGRO)
    
    
    return retorno