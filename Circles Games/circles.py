import pygame
import sys
import random
import time

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego de Colisiones")

# Definir colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)
COLORES = [(0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]

# Función para inicializar el juego
def iniciar_juego():
    global x, y, circulos, game_over, start_time
    x, y = 400, 300

    # Definir otros círculos
    num_circulos = 5
    circulos = []
    while len(circulos) < num_circulos:
        circ_x = random.randint(50, 750)
        circ_y = random.randint(50, 550)
        circ_dx = random.choice([-1, 1])
        circ_dy = random.choice([-1, 1])
        circ_color = random.choice(COLORES)
        
        # Verificar que no haya colisión inicial con el círculo rojo
        distancia_inicial = ((circ_x - x)**2 + (circ_y - y)**2)**0.5
        if distancia_inicial >= 70:  # 50 es el radio del círculo rojo, 20 es el radio de otros círculos
            circulos.append([circ_x, circ_y, circ_dx, circ_dy, circ_color])
    
    game_over = False
    start_time = time.time()

# Función para mostrar mensaje de Game Over
def mostrar_mensaje(texto):
    font = pygame.font.Font(None, 74)
    text = font.render(texto, True, BLANCO)
    screen.blit(text, (200, 250))

# Función para mostrar el botón de reinicio
def mostrar_boton_reinicio():
    font = pygame.font.Font(None, 36)
    text = font.render("Reiniciar", True, NEGRO)
    rect = text.get_rect(center=(400, 350))
    pygame.draw.rect(screen, BLANCO, rect.inflate(20, 10))
    screen.blit(text, rect)
    return rect

# Función para mostrar el contador de tiempo
def mostrar_contador():
    font = pygame.font.Font(None, 36)
    elapsed_time = int(time.time() - start_time)
    text = font.render(f"Tiempo: {elapsed_time} s", True, BLANCO)
    screen.blit(text, (10, 10))

# Inicializar el juego
iniciar_juego()

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            if reiniciar_rect.collidepoint(event.pos):
                iniciar_juego()

    if not game_over:
        # Obtener el estado de las teclas
        teclas = pygame.key.get_pressed()

        # Mover el círculo rojo según las teclas presionadas
        if teclas[pygame.K_a] and x > 50:  # Izquierda
            x -= 1
        if teclas[pygame.K_d] and x < 750:  # Derecha
            x += 1
        if teclas[pygame.K_w] and y > 50:  # Arriba
            y -= 1
        if teclas[pygame.K_s] and y < 550:  # Abajo
            y += 1

        # Mover otros círculos
        for circ in circulos:
            circ[0] += circ[2]
            circ[1] += circ[3]

            # Rebotar en los bordes
            if circ[0] <= 0 or circ[0] >= 800:
                circ[2] = -circ[2]
            if circ[1] <= 0 or circ[1] >= 600:
                circ[3] = -circ[3]

            # Verificar colisiones
            distancia = ((circ[0] - x)**2 + (circ[1] - y)**2)**0.5
            if distancia < 50 + 20:  # 50 es el radio del círculo rojo, 20 es el radio de otros círculos
                game_over = True

    # Rellenar la pantalla con color negro
    screen.fill(NEGRO)

    # Dibujar el círculo rojo
    pygame.draw.circle(screen, ROJO, (x, y), 50)

    # Dibujar otros círculos
    for circ in circulos:
        pygame.draw.circle(screen, circ[4], (circ[0], circ[1]), 20)

    # Mostrar mensaje de Game Over y botón de reinicio si es necesario
    if game_over:
        mostrar_mensaje("GAME OVER")
        reiniciar_rect = mostrar_boton_reinicio()
    else:
        mostrar_contador()

    # Actualizar la pantalla
    pygame.display.flip()
