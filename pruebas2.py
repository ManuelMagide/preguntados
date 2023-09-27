import pygame
from constantes import *
from datos import lista

posicion_imagen = [0, 0]
posicion_imagen_dos = [0, 0]
posicion = 0
titulo = ''
puntaje = 0
opcion_a = ''
opcion_b = ''
opcion_c = ''
opcion_correcta = ''
error = 0
bandera_reinicio = False

def listar_tipos(lista_preg, key: str):
    lista = []

    for pregunta in lista_preg:
        lista.append(pregunta[key])
    
    return lista

pregunta = listar_tipos(lista, 'pregunta')
a = listar_tipos(lista, 'a')
b = listar_tipos(lista, 'b')
c = listar_tipos(lista, 'c')
correcta = listar_tipos(lista, 'correcta')

pygame.init()

#Definimos pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA)) #Tamaño de pantalla
pygame.display.set_caption('Preguntados manaos!!') #Titulo

#Definimos una imagen
imagen = pygame.image.load('logo_preg.png')
imagen = pygame.transform.scale(imagen, (200, 200))

imagen_dos = pygame.image.load('fondo.jpg')
imagen_dos = pygame.transform.scale(imagen_dos, (1400, 1200))

#Definir texto
fuente = pygame.font.SysFont('Arial', 30)
texto_titulo = fuente.render(str(titulo), True, COLOR_BLANCO)
texto_reiniciar = fuente.render(str('Reiniciar'), True, COLOR_BLANCO)

texto_pregunta = fuente.render(str('Pregunta'), True, COLOR_BLANCO)
texto_a = fuente.render(str(opcion_a), True, COLOR_BLANCO)
texto_b = fuente.render(str(opcion_b), True, COLOR_BLANCO)
texto_c = fuente.render(str(opcion_c), True, COLOR_BLANCO)

flag_ejecutar = True
while flag_ejecutar:

    lista_evento = pygame.event.get()

    for evento in lista_evento:
        if evento.type == pygame.QUIT:
            flag_ejecutar = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            
            if posicion < len(pregunta):
                if (posicion_click[0] > 460 and posicion_click[0] < 700) and (posicion_click[1] > 95 and posicion_click[1] < 150):
                    bandera_reinicio = False
                    titulo = pregunta[posicion]
                    opcion_a = a[posicion]
                    opcion_b = b[posicion]
                    opcion_c = c[posicion]
                    opcion_correcta = correcta[posicion]
                    texto_a = fuente.render(str(opcion_a), True, COLOR_BLANCO)
                    texto_b = fuente.render(str(opcion_b), True, COLOR_BLANCO)
                    texto_c = fuente.render(str(opcion_c), True, COLOR_BLANCO)
                    error = 0
                    posicion = posicion + 1
                
                if bandera_reinicio == False:
                    if error == 2:
                        texto_a = fuente.render(str(''), True, COLOR_BLANCO)
                        texto_b = fuente.render(str(''), True, COLOR_BLANCO)
                        texto_c = fuente.render(str(''), True, COLOR_BLANCO)
                    
                    else:
                        if (posicion_click[0] > 140 and posicion_click[0] < 380) and (posicion_click[1] > 600 and posicion_click[1] < 630):
                            if opcion_correcta == 'a':
                                puntaje += 10
                                titulo = pregunta[posicion]
                                opcion_a = a[posicion]
                                opcion_b = b[posicion]
                                opcion_c = c[posicion]
                                opcion_correcta = correcta[posicion]
                                posicion = posicion + 1
                                texto_a = fuente.render(str(opcion_a), True, COLOR_BLANCO)
                                texto_b = fuente.render(str(opcion_b), True, COLOR_BLANCO)
                                texto_c = fuente.render(str(opcion_c), True, COLOR_BLANCO)
                                error = 0
                            else:
                                texto_a = fuente.render(str(''), True, COLOR_BLANCO)
                                error += 1
                        
                        elif (posicion_click[0] > 440 and posicion_click[0] < 680) and (posicion_click[1] > 600 and posicion_click[1] < 630):
                            if opcion_correcta == 'b':
                                puntaje += 10
                                titulo = pregunta[posicion]
                                opcion_a = a[posicion]
                                opcion_b = b[posicion]
                                opcion_c = c[posicion]
                                opcion_correcta = correcta[posicion]
                                posicion = posicion + 1
                                texto_a = fuente.render(str(opcion_a), True, COLOR_BLANCO)
                                texto_b = fuente.render(str(opcion_b), True, COLOR_BLANCO)
                                texto_c = fuente.render(str(opcion_c), True, COLOR_BLANCO)
                                error = 0
                            else:
                                texto_b = fuente.render(str(''), True, COLOR_BLANCO)
                                error += 1
                        
                        elif (posicion_click[0] > 740 and posicion_click[0] < 980) and (posicion_click[1] > 600 and posicion_click[1] < 630):
                            if opcion_correcta == 'c':
                                puntaje += 10
                                titulo = pregunta[posicion]
                                opcion_a = a[posicion]
                                opcion_b = b[posicion]
                                opcion_c = c[posicion]
                                opcion_correcta = correcta[posicion]
                                posicion = posicion + 1
                                texto_a = fuente.render(str(opcion_a), True, COLOR_BLANCO)
                                texto_b = fuente.render(str(opcion_b), True, COLOR_BLANCO)
                                texto_c = fuente.render(str(opcion_c), True, COLOR_BLANCO)
                                error = 0
                            else:
                                texto_c = fuente.render(str(''), True, COLOR_BLANCO)
                                error += 1
            
            else:
                posicion = 0
                puntaje = 0
                texto_a = fuente.render(str(''), True, COLOR_BLANCO)
                texto_b = fuente.render(str(''), True, COLOR_BLANCO)
                texto_c = fuente.render(str(''), True, COLOR_BLANCO)
                bandera_reinicio = True
            
            if (posicion_click[0] > 440 and posicion_click[0] < 680) and (posicion_click[1] > 800 and posicion_click[1] < 880):
                    posicion = 0
                    puntaje = 0
                    texto_a = fuente.render(str(''), True, COLOR_BLANCO)
                    texto_b = fuente.render(str(''), True, COLOR_BLANCO)
                    texto_c = fuente.render(str(''), True, COLOR_BLANCO)
                    texto_puntaje = fuente.render(str(puntaje), True, COLOR_ROJO)
                    bandera_reinicio = True
    
    if bandera_reinicio == False:
        texto_titulo = fuente.render(str(titulo), True, COLOR_BLANCO)
        texto_puntaje = fuente.render(str(puntaje), True, COLOR_ROJO)
    else:
        texto_titulo = fuente.render(str(''), True, COLOR_BLANCO)
    
    pantalla.blit(imagen_dos, (posicion_imagen_dos))
    pygame.draw.rect(pantalla, COLOR_AMARILLO, (460, 90, 200, 60), 1) #LEFT, TOP, ANCHO Y ALTO
    pygame.draw.rect(pantalla, COLOR_CELESTE, (460, 800, 200, 60), 1)
    pantalla.blit(imagen, (posicion_imagen)) #Pusimos una imagen sobre la pantalla
    pantalla.blit(texto_pregunta, (500,100))
    pantalla.blit(texto_reiniciar, (500,810))
    pantalla.blit(texto_puntaje, (1100,100))
    pantalla.blit(texto_titulo, (300,300))
    pantalla.blit(texto_a, (150,600))
    pantalla.blit(texto_b, (450,600))
    pantalla.blit(texto_c, (750,600))
    pygame.display.flip() #Actualizacion de mi pantalla

pygame.quit()