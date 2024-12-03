import pygame 
import random
from Constantes import * 
from Funciones import *
# from data.Preguntas import *
from utils.files_management import parsear_archivo_preguntas



pygame.init()

#CREO CUADROS DE PREGUNTAS, RESPUESTAS Y BOTONES INTERACTIVOS
boton_tiempo = crear_objeto(TAMAÑO_BOTON_TIEMPO,COLOR_NEGRO)
boton_volumen_silenciado = crear_objeto_imagen("assets\images\mute.png",(25,25))
boton_volumen = crear_objeto_imagen("assets\images\sound.png",(25,25))
boton_rect = boton_rect = pygame.Rect(470, 770, 25, 25)
cuadro_pregunta = crear_objeto(TAMAÑO_PREGUNTA,COLOR_NEGRO)
lista_respuestas = crear_cuadros(4,TAMAÑO_RESPUESTA,COLOR_NEGRO)
lista_comodines = crear_cuadros(4,TAMAÑO_COMODIN,COLOR_VIOLETA)
lista_preguntas = parsear_archivo_preguntas()
musica_activa = True
vida_extra = False
cantidad_bucles = 0

COMODIN_BOMBA = 'Bomba'
COMODIN_X2 = 'X2'
COMODIN_CANCHE_EXTRA = 'Chance +'
COMODIN_PASAR = 'Pasar'
comodines_ids = [COMODIN_BOMBA, COMODIN_X2, COMODIN_CANCHE_EXTRA, COMODIN_PASAR,]
for index, comodin in enumerate(lista_comodines):
    comodin["utilizado"] = False
    comodin['id'] = comodines_ids[index]

    
indice = 0 #Son inmutables
bandera_respuesta = False #Son inmutables
random.shuffle(lista_preguntas)

def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    tiempo_actual = pygame.time.get_ticks() // 1000
    
    #VARIABLES GLOBALES
    global indice
    global bandera_respuesta
    global musica_activa
    global vida_extra
    global cantidad_bucles

    pregunta_actual = lista_preguntas[indice]
    
    #AGREGO LOS DATOS DE LA CUENTA REGRESIVA
    if 'inicio_tiempo' not in datos_juego:
        datos_juego['inicio_tiempo'] = tiempo_actual
    
    tiempo_restante = 10 - (tiempo_actual - datos_juego['inicio_tiempo'])
    

    retorno = "juego"

    if bandera_respuesta:
        pygame.time.delay(250)
        
        cuadro_pregunta["superficie"] = pygame.image.load("assets/images/fondo.jpg")
        cuadro_pregunta["superficie"] = pygame.transform.scale(cuadro_pregunta["superficie"],TAMAÑO_PREGUNTA)
        for i in range(len(lista_respuestas)):
            lista_respuestas[i]["superficie"].fill(COLOR_AZUL)
        bandera_respuesta = False
    
    
    if tiempo_restante <= 0:
        datos_juego['inicio_tiempo'] = tiempo_actual
        indice += 1
        if indice >= len(lista_preguntas):
            indice = 0
            random.shuffle(lista_preguntas)
        datos_juego["cantidad_vidas"] -= 1

        if datos_juego["cantidad_vidas"] <= 0:
            retorno = "terminado"


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

            

            for comodin in lista_comodines:
                if comodin["rectangulo"].collidepoint(evento.pos):
              
                    if comodin["utilizado"] == True:
                        ERROR_SONIDO.play()
                        print("YA USASTE ESTE COMODIN AMIGO")
                        lista_comodines[i]["superficie"].fill(COLOR_VERDE_OSCURO)
                    else:
                        ACIERTO_SONIDO.play()
                        comodin["utilizado"] = True
                        if comodin['id'] == COMODIN_BOMBA:
                          print(f"Apretaste el comodin: {comodin['id']}")
                        elif comodin['id'] == COMODIN_X2:
                          print(f"Apretaste el comodin: {comodin['id']}")
                        elif comodin['id'] == COMODIN_CANCHE_EXTRA:
                          print(f"Apretaste el comodin: {comodin['id']}")
                        elif comodin['id'] == COMODIN_PASAR:
                          print(f"Apretaste el comodin: {comodin['id']}")
                            
                        
                        # lista_comodines[i]["superficie"].fill(COLOR_ROJO)
                        # if datos_juego["puntuacion"] > 0:
                        #     datos_juego["puntuacion"] -= PUNTUACION_ERROR
                        # datos_juego["cantidad_vidas"] -= 1
                        # vida_extra = False

                
                    

    
    pantalla.fill(COLOR_BLANCO)
    
   
    # Limpiar y mostrar respuestas individualmente
    cuadro_pregunta["superficie"].fill(COLOR_NEGRO)
    mostrar_texto(cuadro_pregunta["superficie"],f"{pregunta_actual['pregunta']}",(20,20),FUENTE_27,COLOR_BLANCO)

    lista_respuestas[0]["superficie"].fill(COLOR_NEGRO) 
    mostrar_texto(lista_respuestas[0]["superficie"], pregunta_actual['respuesta_1'], (20, 20), FUENTE_22, COLOR_BLANCO)

    lista_respuestas[1]["superficie"].fill(COLOR_NEGRO)
    mostrar_texto(lista_respuestas[1]["superficie"], pregunta_actual['respuesta_2'], (20, 20), FUENTE_22, COLOR_BLANCO)

    lista_respuestas[2]["superficie"].fill(COLOR_NEGRO)
    mostrar_texto(lista_respuestas[2]["superficie"], pregunta_actual['respuesta_3'], (20, 20), FUENTE_22, COLOR_BLANCO)

    lista_respuestas[3]["superficie"].fill(COLOR_NEGRO)
    mostrar_texto(lista_respuestas[3]["superficie"], pregunta_actual['respuesta_4'], (20, 20), FUENTE_22, COLOR_BLANCO)

    # mostrar comodines
    lista_comodines[0]["superficie"].fill(COLOR_GRIS if lista_comodines[0]["utilizado"] == True else COLOR_NEGRO) 
    mostrar_texto(lista_comodines[0]["superficie"], lista_comodines[0]['id'], (20, 20), FUENTE_22, COLOR_BLANCO)

    lista_comodines[1]["superficie"].fill(COLOR_GRIS if lista_comodines[1]["utilizado"] == True else COLOR_NEGRO)
    mostrar_texto(lista_comodines[1]["superficie"], lista_comodines[1]['id'], (20, 20), FUENTE_22, COLOR_BLANCO)

    lista_comodines[2]["superficie"].fill(COLOR_GRIS if lista_comodines[2]["utilizado"] == True else COLOR_NEGRO)
    mostrar_texto(lista_comodines[2]["superficie"], lista_comodines[2]['id'], (20, 20), FUENTE_22, COLOR_BLANCO)

    lista_comodines[3]["superficie"].fill(COLOR_GRIS if lista_comodines[3]["utilizado"] == True else COLOR_NEGRO)
    mostrar_texto(lista_comodines[3]["superficie"], lista_comodines[3]['id'], (20, 20), FUENTE_22, COLOR_BLANCO)

    #MOSTRAR CUADROS EN PANTALLA    
    cuadro_pregunta["rectangulo"] = pantalla.blit(cuadro_pregunta["superficie"],(80,80))
    lista_respuestas[0]["rectangulo"] = pantalla.blit(lista_respuestas[0]["superficie"],(75,245))#r1
    lista_respuestas[1]["rectangulo"] = pantalla.blit(lista_respuestas[1]["superficie"],(75,345))#r2
    lista_respuestas[2]["rectangulo"] = pantalla.blit(lista_respuestas[2]["superficie"],(75,445))#r3
    lista_respuestas[3]["rectangulo"] = pantalla.blit(lista_respuestas[3]["superficie"],(75,545))#r4
    #comodines
    lista_comodines[0]["rectangulo"] = pantalla.blit(lista_comodines[0]["superficie"],(35,680))#r1
    lista_comodines[1]["rectangulo"] = pantalla.blit(lista_comodines[1]["superficie"],(145,680))#r2
    lista_comodines[2]["rectangulo"] = pantalla.blit(lista_comodines[2]["superficie"],(255,680))#r3
    lista_comodines[3]["rectangulo"] = pantalla.blit(lista_comodines[3]["superficie"],(365,680))#r4
    boton_imagen = boton_volumen["superficie"] if musica_activa else boton_volumen_silenciado["superficie"]
    pantalla.blit(boton_imagen, boton_rect.topleft)
    boton_tiempo["rectangulo"] = pantalla.blit(boton_tiempo["superficie"],(10,770))
    
    #CREAR RECTANGULOS INTERACTIVOS
    pygame.draw.rect(pantalla,COLOR_NEGRO,cuadro_pregunta["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[0]["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[1]["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[2]["rectangulo"],2)
    
    #MUESTRO INFORMACIÓN DEL JUEGADOR
    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(10,10),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,f"VIDAS: {datos_juego['cantidad_vidas']}",(10,40),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,f"TIEMPO: {tiempo_restante}",(10,770),FUENTE_25,COLOR_BLANCO)
    
    
    return retorno