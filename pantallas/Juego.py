
import pygame 
import random
from Funciones import *
# from data.Preguntas import *
from utils.files_management import parsear_archivo_preguntas

pygame.init()

#CREO CUADROS DE PREGUNTAS, RESPUESTAS Y BOTONES INTERACTIVOS
boton_tiempo = crear_objeto(TAMAÑO_BOTON_TIEMPO,COLOR_NEGRO)
boton_volumen_silenciado = crear_objeto_imagen("assets\images\mute.png",(25,25))
boton_volumen = crear_objeto_imagen("assets\images\sound.png",(25,25))
boton_rect = boton_rect = pygame.Rect(470, 770, 25, 25)
# cuadro_pregunta = crear_objeto(TAMAÑO_PREGUNTA,COLOR_NEGRO)
# lista_respuestas = crear_cuadros(4,TAMAÑO_RESPUESTA,COLOR_NEGRO)
# lista_preguntas = parsear_archivo_preguntas()
musica_activa = True
vida_extra = False
cantidad_bucles = 0
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
lista_comodines = crear_comodines()

    
indice = 0 #Son inmutables
bandera_respuesta = False #Son inmutables
random.shuffle(lista_preguntas)


def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    tiempo_actual = pygame.time.get_ticks() // 1000

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
        #cuadro_pregunta["superficie"].fill(COLOR_ROJO)
        #Limpio la superficie
        cuadro_pregunta["superficie"] = pygame.image.load("assets\images\_fondo_respuestas.jpg")
        cuadro_pregunta["superficie"] = pygame.transform.scale(cuadro_pregunta["superficie"],TAMAÑO_PREGUNTA)

        for i in range(len(lista_respuestas)):
            lista_respuestas[i]["superficie"] = pygame.image.load("assets\images\_fondo_respuestas.jpg")
            lista_respuestas[i]["superficie"] = pygame.transform.scale(lista_respuestas[i]["superficie"],TAMAÑO_RESPUESTA)
        bandera_respuesta = False


    if tiempo_restante <= 0:
   
        datos_juego['inicio_tiempo'] = tiempo_actual

        # Limpia el cuadro de la pregunta
        cuadro_pregunta["superficie"] = pygame.image.load("assets\images\_fondo_respuestas.jpg")
        cuadro_pregunta["superficie"] = pygame.transform.scale(cuadro_pregunta["superficie"],TAMAÑO_PREGUNTA)  
        for i in range(len(lista_respuestas)):
            lista_respuestas[i]["superficie"] = pygame.image.load("assets\images\_fondo_respuestas.jpg")
            lista_respuestas[i]["superficie"] = pygame.transform.scale(lista_respuestas[i]["superficie"],TAMAÑO_RESPUESTA)
        # Pasa a la siguiente pregunta
        indice += 1
        if indice >= len(lista_preguntas):
            indice = 0  #reinicia indice de preguntas
            random.shuffle(lista_preguntas)          
        datos_juego["cantidad_vidas"] -= 1     
        
        if datos_juego["cantidad_vidas"] <= 0:
            retorno = "terminado"        
        pregunta_actual = lista_preguntas[indice]  #Actualiza los datos para la siguiente pregunta

      
        # mostrar_texto(cuadro_pregunta["superficie"], f"{pregunta_actual['pregunta']}", (20, 20), FUENTE_20, COLOR_BLANCO)
        # mostrar_texto(lista_respuestas[0]["superficie"], f"{pregunta_actual['respuesta_1']}", (20, 20), FUENTE_17, COLOR_BLANCO)
        # mostrar_texto(lista_respuestas[1]["superficie"], f"{pregunta_actual['respuesta_2']}", (20, 20), FUENTE_17, COLOR_BLANCO)
        # mostrar_texto(lista_respuestas[2]["superficie"], f"{pregunta_actual['respuesta_3']}", (20, 20), FUENTE_17, COLOR_BLANCO)
        # mostrar_texto(lista_respuestas[3]["superficie"], f"{pregunta_actual['respuesta_4']}", (20, 20), FUENTE_17, COLOR_BLANCO)


    # if tiempo_restante <= 0:
    #     datos_juego['inicio_tiempo'] = tiempo_actual
    #     indice += 1
        
    #     if indice >= len(lista_preguntas):
    #         indice = 0
    #         random.shuffle(lista_preguntas) 
      
    #     datos_juego["cantidad_vidas"] -= 1

    #     if datos_juego["cantidad_vidas"] <= 0:
    #         retorno = "terminado"
    
    
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


                        puntos = PUNTUACION_ACIERTO

                        if datos_juego['comodines']['x2'] == True:
                            puntos = PUNTUACION_ACIERTO * 2
                            datos_juego['comodines']['x2'] = False

                        datos_juego["puntuacion"] += puntos



                    else:
                        if datos_juego["comodines"]["doble_chance"]:
                            # Permitir una segunda selección antes de penalizar
                            datos_juego["comodines"]["doble_chance"] = False
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
                        #  Bomba: Elimina dos respuestas y solo deja la correcta y una
                        # incorrecta
                        # ■ X2: Permite duplicar la cantidad de puntos que se obtienen
                        # ■ Doble chance: En caso de errarle a la pregunta, tiene una segunda
                        # chance de responder con las 3 opciones que quedan.
                        # ■ Pasar:Me permite pasar a la siguiente pregunta, sin sumar ni restar
                        # puntos ni vidas.

                        ACIERTO_SONIDO.play()
                        comodin["utilizado"] = True
                        if comodin['id'] == COMODIN_BOMBA:
                          print(f"Apretaste el comodin: {comodin['id']}")
                        elif comodin['id'] == COMODIN_X2:
                            usar_comodin_x2(datos_juego)
                            # if respuesta_seleccionada == pregunta_actual["respuesta_correcta"]:
                            #     puntos = PUNTUACION_ACIERTO * 2 if x2_activado 
                            # else:
                            #     PUNTUACION_ACIERTO
                            #     datos_juego["puntuacion"] += puntos
                            print(f"Apretaste el comodin: {comodin['id']}")
                        elif comodin['id'] == COMODIN_CANCHE_EXTRA:
                            print(f"Apretaste el comodin: {comodin['id']}")
                        elif comodin['id'] == COMODIN_PASAR:
                            print(f"Apretaste el comodin: {comodin['id']}")




    
                    
    

    
    
    
    
    
    pantalla.blit(fondo,(0,0))
    # pantalla.fill(COLOR_BLANCO)
    #pantalla.blit(fondo,(0,0))
    circulo_volumen = pygame.draw.circle(fondo,COLOR_BLANCO,(490, 790),40)





    
    mostrar_texto(cuadro_pregunta["superficie"],f"{pregunta_actual["pregunta"]}",(20,20),FUENTE_20,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[0]["superficie"],f"{pregunta_actual["respuesta_1"]}",(20,20),FUENTE_17,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[1]["superficie"],f"{pregunta_actual["respuesta_2"]}",(20,20),FUENTE_17,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[2]["superficie"],f"{pregunta_actual["respuesta_3"]}",(20,20),FUENTE_17,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[3]["superficie"],f"{pregunta_actual["respuesta_4"]}",(20,20),FUENTE_17,COLOR_BLANCO)
    

#FOR PARA MOSTRAR PREGUNTAS
    # for i, respuesta in enumerate(lista_respuestas):
    #     respuesta["superficie"].fill(COLOR_NEGRO)
    #     mostrar_texto(respuesta["superficie"], pregunta_actual[f'respuesta_{i+1}'], (20, 20), FUENTE_22, COLOR_BLANCO)


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
    cuadro_pregunta["rectangulo"] = pantalla.blit(cuadro_pregunta["superficie"],(50,100))
    lista_respuestas[0]["rectangulo"] = pantalla.blit(lista_respuestas[0]["superficie"],(50,255))#r1 #conn estos numeros modifico la posicion de las respuestas
    lista_respuestas[1]["rectangulo"] = pantalla.blit(lista_respuestas[1]["superficie"],(50,355))#r2
    lista_respuestas[2]["rectangulo"] = pantalla.blit(lista_respuestas[2]["superficie"],(50,455))#r3
    lista_respuestas[3]["rectangulo"] = pantalla.blit(lista_respuestas[3]["superficie"],(50,555))#r4
    #comodines
    lista_comodines[0]["rectangulo"] = pantalla.blit(lista_comodines[0]["superficie"],(35,680))#r1
    lista_comodines[1]["rectangulo"] = pantalla.blit(lista_comodines[1]["superficie"],(145,680))#r2
    lista_comodines[2]["rectangulo"] = pantalla.blit(lista_comodines[2]["superficie"],(255,680))#r3
    lista_comodines[3]["rectangulo"] = pantalla.blit(lista_comodines[3]["superficie"],(365,680))#r4

    # cuadro_pregunta["rectangulo"] = pantalla.blit(cuadro_pregunta["superficie"],(80,80))

    # for i, respuesta in enumerate(lista_respuestas):
    #     y_pos = 255 + i * 100  # Calcula la posición en Y dinámicamente
    #     lista_respuestas[i]["rectangulo"] = pantalla.blit(lista_respuestas[i]["superficie"], (50, y_pos))

    
    boton_imagen = boton_volumen["superficie"] if musica_activa else boton_volumen_silenciado["superficie"]
    pantalla.blit(boton_imagen, boton_rect.topleft)
    
    boton_tiempo["rectangulo"] = pantalla.blit(boton_tiempo["superficie"],(10,770))


    
    # pygame.draw.rect(pantalla,COLOR_NEGRO,cuadro_pregunta["rectangulo"],2)
    # pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[0]["rectangulo"],2)
    # pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[1]["rectangulo"],2)
    # pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[2]["rectangulo"],2)
    # pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[3]["rectangulo"],2)
    
    # mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(10,10),FUENTE_22,COLOR_BLANCO)
    # mostrar_texto(pantalla,f"VIDAS: {datos_juego['cantidad_vidas']}",(375,10),FUENTE_22,COLOR_BLANCO)
   

    for i in range(len(lista_respuestas)):
        pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[i]["rectangulo"],2)
    #MUESTRO INFORMACIÓN DEL JUEGADOR
    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(10,10),FUENTE_25,COLOR_BLANCO)
    mostrar_texto(pantalla,f"VIDAS: {datos_juego['cantidad_vidas']}",(375,10),FUENTE_25,COLOR_BLANCO)
    mostrar_texto(pantalla,f"TIEMPO: {tiempo_restante}",(10,770),FUENTE_25,COLOR_BLANCO)
    
    
    return retorno