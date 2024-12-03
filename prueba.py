import sys
import pygame

# Configuration
# pygame.init()

# print(pygame.font.get_fonts())

import pygame

# Inicializar Pygame
pygame.init()

# Crear la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Texto con contorno")

# Establecer colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TEXT_COLOR = (0, 128, 255)  # Color del texto (puedes elegir otro)

# Cargar la fuente
FUENTE_30 = pygame.font.SysFont("segoeuiblack", 30)

# Crear el texto con el contorno
def render_text_with_outline(text, font, text_color, outline_color, position):
    # Renderizar el contorno
    outline_text = font.render(text, True, outline_color)
    # Crear la superficie del texto principal
    main_text = font.render(text, True, text_color)
    
    # Dibujar el contorno primero (un poco desplazado)
    screen.blit(outline_text, (position[0] - 2, position[1] - 2))
    screen.blit(outline_text, (position[0] + 2, position[1] - 2))
    screen.blit(outline_text, (position[0] - 2, position[1] + 2))
    screen.blit(outline_text, (position[0] + 2, position[1] + 2))
    
    # Dibujar el texto principal encima
    screen.blit(main_text, position)

# Mostrar el texto con contorno
screen.fill(BLACK)
render_text_with_outline("Texto con contorno", FUENTE_30, TEXT_COLOR, WHITE, (250, 250))

# Actualizar la pantalla
pygame.display.flip()

# Mantener la ventana abierta
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Cerrar Pygame
pygame.quit()
