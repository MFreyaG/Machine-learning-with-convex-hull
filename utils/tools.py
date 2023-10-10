from entities.point import Point

class Tools:
    def find_orientation(p1: Point, p2: Point, p3: Point):
        cross_product = (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)

        if cross_product == 0:
            return 0
        elif cross_product > 0:
            return 1
        else:
            return -1
