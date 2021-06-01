class Shape:
    def __init__(self, pos, angle):
        self.pos = pos
        self.angle = angle
        self.offset = [pos[0] * 2, pos[1] * 2, pos[2] * 2]
        self.points = []
        self.edges = []

    def add_pos(self, new_pos=(0, 0, 0)):
        for point in self.points:
            point[0][0] += new_pos[0]
            point[1][0] += new_pos[1]
            point[2][0] += new_pos[2]

class Cube(Shape):
    def __init__(self, pos=[0, 0, 0], angle=[0, 0, 0]):
        super().__init__(pos, angle)
        self.points.append([[-1 + self.offset[0]], [-1 + self.offset[1]], [1 + self.offset[2]]])
        self.points.append([[1 + self.offset[0]], [-1 + self.offset[1]], [1 + self.offset[2]]])
        self.points.append([[1 + self.offset[0]], [1 + self.offset[1]], [1 + self.offset[2]]])
        self.points.append([[-1 + self.offset[0]], [1 + self.offset[1]], [1 + self.offset[2]]])
        self.points.append([[-1 + self.offset[0]], [-1 + self.offset[1]], [-1 + self.offset[2]]])
        self.points.append([[1 + self.offset[0]], [-1 + self.offset[1]], [-1 + self.offset[2]]])
        self.points.append([[1 + self.offset[0]], [1 + self.offset[1]], [-1 + self.offset[2]]])
        self.points.append([[-1 + self.offset[0]], [1 + self.offset[1]], [-1 + self.offset[2]]])

        self.edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]

class Plane(Shape):
    def __init__(self, pos=[0, 0, 0], angle=[0, 0, 0]):
        super().__init__(pos, angle)
        self.points.append([[-1 + self.offset[0]], [-1 + self.offset[1]], [0 + self.offset[2]]])
        self.points.append([[1 + self.offset[0]], [-1 + self.offset[1]], [0 + self.offset[2]]])
        self.points.append([[1 + self.offset[0]], [1 + self.offset[1]], [0 + self.offset[2]]])
        self.points.append([[-1 + self.offset[0]], [1 + self.offset[1]], [0 + self.offset[2]]])

        self.edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
