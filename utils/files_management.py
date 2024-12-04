import os
import json
from datetime import datetime

def crear_diccionario_pregunta(lista_valores:list) -> dict:
    '''
    Crea un diccionario partiendo de una lista de valores. El formato es:
      {
        pregunta:str,
        respuesta_n:str
        respuesta_correcta:int
      }
    '''
    diccionario = {
        # "pregunta"
        # "respuesta_"
        # "respuesta_"
        # "respuesta_"
        # "respuesta_"
        # "respuesta_correcta"
    }
    last_index = (len(lista_valores) -1)
    for index, valor in enumerate(lista_valores):
        if index == 0:
            diccionario["pregunta"] = lista_valores[0]
        elif index == last_index:
            print('respuesta correcta:', lista_valores[last_index])
            valor_sin_espacios = lista_valores[last_index].strip()
            print('valor_sin_espacios:', valor_sin_espacios)
            print('valor_sin_espacios len:', len(valor_sin_espacios))
            diccionario["respuesta_correcta"] = int(valor_sin_espacios)
        else:
            diccionario[f"respuesta_{index}"] = lista_valores[index]
    
    return diccionario

def parsear_archivo_preguntas() -> list:
    '''Lee el archivo de preguntas y devuelve una lista de diccionarios'''
    ruta_relativa = "data\Preguntas_Examen.csv"
    ruta_absoluta = os.path.abspath(ruta_relativa)
    print(f"ruta_absoluta: {ruta_relativa}")
    
    resultado = []
    if os.path.exists(ruta_relativa):
        with open(ruta_relativa,"r", encoding="utf-8") as archivo:
            #Leer la primer linea del archivo y no hacer nada.
            archivo.readline()
            for linea in archivo:
                print('Printeo linea: ',linea)
                linea = linea.replace("\n","") 
                lista_valores = linea.split(";")
                diccionario = crear_diccionario_pregunta(lista_valores)
                resultado.append(diccionario)
        print(f"Fin del with: {archivo.closed}")
    else:
        print("EL ARCHIVO NO EXISTE, NO SE PUEDE ABRIR")
    return resultado


def leer_json(nombre_archivo:str) -> list:
    lista = []
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r") as archivo:
            lista = json.load(archivo)
    return lista

def generar_json(nombre_archivo:str,lista:list) -> bool: 
    if type(lista) == list and len(lista) > 0:
        with open(nombre_archivo,"w") as archivo:
            json.dump(lista,archivo, indent=4)
        resultadoExitoso = True
    else:
        resultadoExitoso = False
    return resultadoExitoso     

def obtener_estadisticas() -> list:
    '''Lee el archivo de partidas previas'''
    ruta_relativa = "data\partidas.json"  
    resultado = leer_json(ruta_relativa)
    return resultado

def guardar_estadisticas(nombre, puntuacion) -> list:
    '''Guarda partida con fecha en el arhcivo de partidas.json'''
    resultado = obtener_estadisticas()
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime("%d/%m/%Y %H:%M:%S")

    datos_jugador = {
        "nombre": nombre,
        "puntuacion": puntuacion,
        "fecha": fecha_formateada,
    }

    ya_esta_en_la_lista = -1
    for index, persona in enumerate(resultado):
        if persona and persona['nombre'] == nombre:
            ya_esta_en_la_lista = index
            break
    
    if ya_esta_en_la_lista > -1:
        resultado[ya_esta_en_la_lista] = datos_jugador
    else:
        resultado.append(datos_jugador)

    resultado.sort(key=lambda x: x["puntuacion"], reverse=True) # aca ordeno con una funcion lambda, que es como un arrow function de JS
    resultado = resultado[:10] # aca corto los primeros 10
    ruta_relativa = "data\partidas.json"  
    generar_json(ruta_relativa, resultado)


