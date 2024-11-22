import pygame
from constantes import *
pygame.init()




pygame.display.set_caption('Mi Juego')

# icono = pygame.image.load('./assets/option.png')
pantalla = pygame.display.set_mode(VENTANA)
corriendo = True
contador_tiempo = 0

# reloj
clock = pygame.time.Clock()


# textos
fuente = pygame.font.SysFont('Arial', 24)
text = fuente.render(f'Contador de tiempo: {contador_tiempo} segundos', False, COLOR_NEGRO)


#Sonidos
sonido_click = pygame.mixer.Sound("parcial_2/assets/vuelta_de_pagina.mp3")
sonido_click.set_volume(0.3)

# musica de fondo
pygame.mixer.init()
# pygame.mixer.music.load('musica.mp3')
# pygame.mixer.music.set_volume(0.1)
# pygame.mixer.music.play(-1) # -1 lo deja haciendo infito


fondo = pygame.image.load("parcial_2/assets/fondo.jpg")
fondo = pygame.transform.scale(fondo, VENTANA)

mi_superficie = pygame.Surface((50,50))


evento_tiempo_1s = pygame.USEREVENT
print('evento_tiempo_1s:', evento_tiempo_1s)
pygame.time.set_timer(evento_tiempo_1s, 1000)
evento_tiempo_5s = pygame.USEREVENT + 1 # le cambio el numero
print('evento_tiempo_5s:', evento_tiempo_5s)
pygame.time.set_timer(evento_tiempo_5s, 5000)



while corriendo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            sonido_click.play()
        if event.type == evento_tiempo_1s:
            print('paso un segundo')
            contador_tiempo += 1
            text = fuente.render(f'Contador de tiempo: {contador_tiempo} segundos', False, COLOR_NEGRO)

    # actualizar juego
    clock.tick(FPS)
    # dibujar elementos

    pantalla.fill((232,23,23)) # para colores se usa RGB o hexa
    pantalla.blit(fondo, (0,0))
    pantalla.blit(text, (10,10))

    pygame.draw.circle(pantalla, COLOR_ROJO, (250,250), 50)
    pygame.draw.rect(pantalla, COLOR_AZUL, (250,250, 100, 100)) # (X,Y,alto,ancho)

    # actualizar la pantalla
    pygame.display.flip()

pygame.quit()

