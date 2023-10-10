from entities.point import Point

class Segment:
    def __init__(self, smaller: Point, greater: Point):
        self.smaller = smaller
        self.greater = greater
        
    def get_y_for_x(self, x):
        gradient = (self.greater.y-self.smaller.y)/(self.greater.x-self.smaller.x)
        c = self.greater.y + gradient*self.greater.x
        
        return gradient*x + c
        
    # Comparison for tree insertion
    def __gt__(self, other):
        if other.smaller.y >= self.get_y_for_x(other.smaller.x):
            return False
        return True
        
    def __eq__(self, other):
        return self.smaller == other.smaller and self.greater == other.greater