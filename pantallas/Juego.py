import pygame 
import random
from Funciones import *
# from data.Preguntas import *
from utils.files_management import parsear_archivo_preguntas

pygame.init()

#cuadro_pregunta["superficie"].fill(COLOR_ROJO)

fondo = pygame.image.load("assets\images\_fondo_ventanas.jpg")
fondo = pygame.transform.scale(fondo,VENTANA)

def create_cuadro_pregunta() -> dict:
    cuadro_pregunta = {}
    #cuadro_pregunta["superficie"] = pygame.Surface(TAMAÑO_PREGUNTA)
    cuadro_pregunta["superficie"] = pygame.image.load("assets\images\_fondo_respuestas.jpg")
    cuadro_pregunta["superficie"] = pygame.transform.scale(cuadro_pregunta["superficie"],TAMAÑO_PREGUNTA)
    cuadro_pregunta["rectangulo"] = cuadro_pregunta["superficie"].get_rect()
    return cuadro_pregunta

def create_lista_respuestas() -> list:
    lista_respuestas = []
    for i in range(4):
        cuadro_respuesta = {}
        cuadro_respuesta["superficie"] = pygame.image.load("assets\images\_fondo_respuestas.jpg")
        cuadro_respuesta["superficie"] = pygame.transform.scale(cuadro_respuesta["superficie"],TAMAÑO_RESPUESTA)        
        cuadro_respuesta["rectangulo"] = cuadro_respuesta["superficie"].get_rect()
        lista_respuestas.append(cuadro_respuesta)
    return lista_respuestas
    


cuadro_pregunta = create_cuadro_pregunta()
lista_respuestas = create_lista_respuestas()
lista_preguntas = parsear_archivo_preguntas()

    
indice = 0 #Son inmutables
bandera_respuesta = False #Son inmutables
random.shuffle(lista_preguntas)

def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global indice
    global bandera_respuesta
    
    retorno = "juego"
    if bandera_respuesta:
        pygame.time.delay(250)
        #cuadro_pregunta["superficie"].fill(COLOR_ROJO)
        #Limpio la superficie
        cuadro_pregunta["superficie"] = pygame.image.load("assets\images\_fondo_respuestas.jpg")
        cuadro_pregunta["superficie"] = pygame.transform.scale(cuadro_pregunta["superficie"],TAMAÑO_PREGUNTA)

        for i in range(len(lista_respuestas)):
            lista_respuestas[i]["superficie"] = pygame.image.load("assets\images\_fondo_respuestas.jpg")
            lista_respuestas[i]["superficie"] = pygame.transform.scale(lista_respuestas[i]["superficie"],TAMAÑO_RESPUESTA)
        bandera_respuesta = False
    
    pregunta_actual = lista_preguntas[indice]
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
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
                    else:
                        ERROR_SONIDO.play()
                        lista_respuestas[i]["superficie"].fill(COLOR_ROJO)
                        if datos_juego["puntuacion"] > 0:
                            datos_juego["puntuacion"] -= PUNTUACION_ERROR
                        datos_juego["cantidad_vidas"] -= 1
                        print("RESPUESTA INCORRECTA")
                        retorno = "terminado"
                    indice += 1
                    
                    if indice == len(lista_preguntas):
                        indice = 0
                        random.shuffle(lista_preguntas)
                        
                    bandera_respuesta = True

    pantalla.blit(fondo,(0,0))
    # pantalla.fill(COLOR_BLANCO)
    #pantalla.blit(fondo,(0,0))


    
    mostrar_texto(cuadro_pregunta["superficie"],f"{pregunta_actual["pregunta"]}",(20,20),FUENTE_20,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[0]["superficie"],f"{pregunta_actual["respuesta_1"]}",(20,20),FUENTE_17,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[1]["superficie"],f"{pregunta_actual["respuesta_2"]}",(20,20),FUENTE_17,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[2]["superficie"],f"{pregunta_actual["respuesta_3"]}",(20,20),FUENTE_17,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[3]["superficie"],f"{pregunta_actual["respuesta_4"]}",(20,20),FUENTE_17,COLOR_BLANCO)
    


    cuadro_pregunta["rectangulo"] = pantalla.blit(cuadro_pregunta["superficie"],(50,40))
    lista_respuestas[0]["rectangulo"] = pantalla.blit(lista_respuestas[0]["superficie"],(50,155))#r1 #conn estos numeros modifico la posicion de las respuestas
    lista_respuestas[1]["rectangulo"] = pantalla.blit(lista_respuestas[1]["superficie"],(50,255))#r2
    lista_respuestas[2]["rectangulo"] = pantalla.blit(lista_respuestas[2]["superficie"],(50,355))#r3
    lista_respuestas[3]["rectangulo"] = pantalla.blit(lista_respuestas[3]["superficie"],(50,455))#r4
    


    pygame.draw.rect(pantalla,COLOR_NEGRO,cuadro_pregunta["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[0]["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[1]["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[2]["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[3]["rectangulo"],2)
    
    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(10,10),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(pantalla,f"VIDAS: {datos_juego['cantidad_vidas']}",(375,10),FUENTE_22,COLOR_BLANCO)
    
    return retorno