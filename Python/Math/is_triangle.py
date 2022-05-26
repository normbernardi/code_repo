def istriangle(ab: float, bc: float, ac: float) -> bool:
    if ab + bc > ac:
        if ab + ac > bc:
            if bc + ac > ab:
                return True
    return False

def findside(point1: tuple, point2: tuple) -> float:
    x = point2[0] - point1[0]
    y = point2[1] - point1[1]
    return float(pow(x/y, 0.5))

def triangle_io(point1: tuple, point2: tuple, point3: tuple) -> bool:
    side_ab = findside(point1, point2)
    side_bc = findside(point2, point3)
    side_ac = findside(point1, point3)
    return istriangle(side_ab, side_bc, side_ac)

vert = [(3, 2), (-2, -3), (2, 3)]

def is_triangle(vert: []) -> bool:
    ab = (0.5 ** ((((vert[0][0] - vert[1][0]) ** 2) + ((vert[0][1] - vert[1][1]) ** 2))))
    bc = (0.5 ** ((((vert[1][0] - vert[2][0]) ** 2) + ((vert[1][1] - vert[2][1]) ** 2))))
    ac = (0.5 ** ((((vert[0][0] - vert[2][0]) ** 2) + ((vert[0][1] - vert[2][1]) ** 2))))
    return ab + bc > ac and ab + ac > bc and bc + ac > ab

print(is_triangle(vert))

print(triangle_io((2, -1), (1, 5), (2, 6)))
