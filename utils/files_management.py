import os


def crear_diccionario_pregunta(lista_valores:list) -> dict:
    '''
    Crea un diccionario partiendo de una lista de valores. El formato es:
      {
        pregunta:str,
        respuesta_n:str
        respuesta_correcta:int
      }
    '''
    diccionario = {}
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
    print(f"ruta_absoluta: {ruta_absoluta}")
    
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


# print('Esta es la lista de diccionarios: \n\n',leer_archivo_preguntas())



# #CSV -> Me permite guardar un conjunto de información separado por un separador especifico normalmente (,) y puedo por ejemplo usarlo en una tabla excel

# #Alumno -> nombre, apellido, genero, nota_final

# #Leer el csv y generar una lista de diccionarios con la data (parse)

# def crear_diccionario_alumno(lista_valores:list) -> dict:
#     diccionario = {}
#     diccionario["nombre"] = lista_valores[0]
#     diccionario["apellido"] = lista_valores[1]
#     diccionario["genero"] = lista_valores[2]
#     diccionario["nota_final"] = int(lista_valores[3])
    
#     return diccionario

# def leer_csv_alumnos(nombre_archivo:str,lista_alumnos:list) -> bool:
#     if os.path.exists(nombre_archivo):
#         with open(nombre_archivo,"r") as archivo:
#             #Leer la primer linea del archivo y no hacer nada.
#             archivo.readline()
#             for linea in archivo:
#                 linea = linea.replace("\n","") 
#                 lista_valores = linea.split(",")
#                 diccionario = crear_diccionario_alumno(lista_valores)
#                 lista_alumnos.append(diccionario)
#             retorno = True
#     else:
#         retorno = False
        
#     return retorno

# # def crear_cabecera(diccionario:dict,separador:str) -> str:
# #     lista_claves = list()

# def crear_cabecera(diccionario:dict,separador:str):
#     claves = diccionario.keys()
#     cabecera = separador.join(claves)
    
#     return cabecera

# def crear_dato_csv(diccionario:dict,separador:str) -> str:
#     lista_valores = list(diccionario.values())
#     for i in range(len(lista_valores)):
#         lista_valores[i] = str(lista_valores[i])    
    
#     separador = ","
#     dato = separador.join(lista_valores)
#     return dato

# def guardar_csv(nombre_archivo:str,lista:list) -> bool:
#     if type(lista) == list and len(lista) > 0:
#         #Obtengo la cabecera
#         cabecera = crear_cabecera(lista[0],",")
        
#         with open(nombre_archivo,"w") as archivo:
#             #Guardamos la cabecera
#             archivo.write(cabecera + "\n")
            
#             #Guardamos todos los datos de la lista
#             # for diccionario in lista:
#             #     dato = crear_dato_csv(diccionario,",")
#             #     archivo.write(dato + "\n")
            
#             for i in range(len(lista)):
#                 dato = crear_dato_csv(lista[i],",")
#                 #Si es el ultimo elemeno
#                 if i != len(lista) - 1:
#                     archivo.write(dato + "\n")
#                 else:
#                     archivo.write(dato)
#         retorno = True
        
#     else:
#         retorno = False

# def mostrar_diccionario(diccionario) -> None:
#     for clave,valor in diccionario.items():
#         print(f"{clave.title().replace("_"," ")} : {valor}")
        
# def mostrar_lista_diccionarios(lista:list) -> bool:
#     retorno = False
#     for elemento in lista:
#         retorno = True
#         mostrar_diccionario(elemento)
#         print("")
        
#     return retorno

# #1. Leer csv -> Generamos la lista de diccionarios de los alumnos
# # lista_alumnos = []
# # leer_csv_alumnos("alumnos.csv",lista_alumnos)
# # mostrar_lista_diccionarios(lista_alumnos)

# #2. Guardar csv -> Creamos el csv con los datos de la lista de diccionarios de alumnos

# lista_alumnos = [{"nombre":"Mariano","apellido":"Fernandez","genero":"masculino","nota_final":10},{"nombre":"Maria","apellido":"Perez","genero":"femenino","nota_final":8}]
# guardar_csv("alumnos_nuevos.csv",lista_alumnos)






# separador = ','
# lista = ['Carlos', 'Perez', '9']

# fila = separador.join(lista)

# print('FILA:', fila)


# acumulador = ''

# for item in lista:
#     acumulador += item + separador


# print('acum:', acumulador)

