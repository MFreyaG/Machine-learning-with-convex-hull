from entities.point import Point

class Segment:
    def __init__(self, smaller: Point, greater: Point):
        self.smaller = smaller
        self.greater = greater
        
    def get_y_for_x(self, x):
        # Treat x out of range - How can I treat this better?
        if x < self.smaller.x or x > self.greater.x:
            return 0
        
        # Treat vertical line
        if x == self.smaller.x:
                return min(self.smaller.y, self.greater.y)
        
        try:
            gradient = (self.greater.y-self.smaller.y)/(self.greater.x-self.smaller.x)
            c = self.greater.y + gradient*self.greater.x
        except:
            raise Exception()
        
        return gradient*x + c
        
    # Comparison for tree insertion
    def __gt__(self, other):
        eps = 1e-6
        my_y_value = self.get_y_for_x(other.smaller.x)
        
        if other.smaller.y >= my_y_value:
            if abs(other.smaller.y - my_y_value) > eps:
                #print(f"{other.smaller.x, other.smaller.y}: {other.greater.x, other.greater.y} is greater than {self.smaller.x,self.smaller.y}: {self.greater.x, self.greater.y}")
                return False
        #print(f"{other.smaller.x, other.smaller.y}: {other.greater.x, other.greater.y} is smaller than {self.smaller.x,self.smaller.y}: {self.greater.x, self.greater.y}")
        return True
        
    def __eq__(self, other):
        epsilon = 1e-6

        if (
            abs(self.smaller.x - other.smaller.x) < epsilon
            and abs(self.smaller.y - other.smaller.y) < epsilon
            and abs(self.greater.x - other.greater.x) < epsilon
            and abs(self.greater.y - other.greater.y) < epsilon
        ):
            return True
        return False
        