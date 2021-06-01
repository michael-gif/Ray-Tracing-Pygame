import pygame
import os
import math
from shapes import *
import renderer

os.environ["SDL_VIDEO_CENTERED"]='1'
width, height = 1680, 1050

pygame.init()
pygame.display.set_caption("3D cube Projection")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60
pygame.mouse.set_visible(0); pygame.event.set_grab(1)

class Camera:
    def __init__(self, pos=[0, 0, 0], angle=[0, 0]):
        self.pos = pos
        self.angle = angle

camera = Camera()

renderer = renderer.Renderer(screen)

run = True
while run:
    clock.tick(fps)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.mouse.set_visible(1); pygame.event.set_grab(0)
                run = False
        if event.type == pygame.MOUSEMOTION:
            x,y = event.rel
            x/=200
            y/=200
            camera.angle[0] -= math.degrees(x)
            camera.angle[1] += math.degrees(y)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        for shape in renderer.queue:
            shape.add_pos((0, -0.1, 0))
    if keys[pygame.K_LSHIFT]:
        for shape in renderer.queue:
            shape.add_pos((0, 0.1, 0))

    renderer.draw(camera)
        
    pygame.display.update()

pygame.quit()
