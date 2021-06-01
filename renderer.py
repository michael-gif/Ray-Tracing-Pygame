import pygame
import math
from matrix import matrix_multiplication
from shapes import *

class Renderer:
    def __init__(self, screen):
        self.queue = [Cube([0, 0, 5])]
        self.screen = screen
        self.scale = 1200
        self.size = pygame.display.get_surface().get_size()
        self.width = self.size[0]
        self.height = self.size[1]
        self.origin = [self.width//2, self.height//2]
        self.black = (20, 20, 20)
        self.white = (230, 230, 230)
        self.blue = (0, 154, 255)

    def connect_point(self, i, j):
        a = j[i[0]]
        b = j[i[1]]
        pygame.draw.line(self.screen, self.black, (a[0], a[1]), (b[0], b[1]), 2)
        
    def draw(self, camera):
        for shape in self.queue:
            index = 0
            projected_points = [j for j in range(len(shape.points))]
            radian_angle = [math.radians(shape.angle[0]), math.radians(shape.angle[1]), math.radians(shape.angle[2])]
            rotation_x = [[1, 0, 0], [0, math.cos(radian_angle[0]), -math.sin(radian_angle[0])], [0, math.sin(radian_angle[0]), math.cos(radian_angle[0])]]
            rotation_y = [[math.cos(radian_angle[1]), 0, -math.sin(radian_angle[1])], [0, 1, 0], [math.sin(radian_angle[1]), 0, math.cos(radian_angle[1])]]
            rotation_z = [[math.cos(radian_angle[2]), -math.sin(radian_angle[2]), 0], [math.sin(radian_angle[2]), math.cos(radian_angle[2]), 0], [0, 0 ,1]]

            for point in shape.points:
                #rotated_2d = matrix_multiplication(rotation_y, point)
                #rotated_2d = matrix_multiplication(rotation_x, rotated_2d)
                rotated_2d = matrix_multiplication(rotation_y, point)
                rotated_2d = matrix_multiplication(rotation_x, rotated_2d)
                distance = 0
                z = 1/(distance - rotated_2d[2][0])
                projection_matrix = [[z, 0, 0],
                                    [0, z, 0]]
                projected_2d = matrix_multiplication(projection_matrix, rotated_2d)

                x = int(projected_2d[0][0] * self.scale) + self.origin[0]
                y = int(projected_2d[1][0] * self.scale) + self.origin[1]
                projected_points[index] = [x, y]
                pygame.draw.circle(self.screen, self.blue, (x, y), 10)
                index += 1
                
            #draw edges
            for m in range(len(shape.edges)):
                self.connect_point(shape.edges[m], projected_points)

            #shape.angle[0] += 1
            shape.angle[0] = -camera.angle[1]
            shape.angle[1] = camera.angle[0]
