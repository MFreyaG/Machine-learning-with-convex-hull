from entities.point import Point
from entities.segment import Segment

class Tools:
    @classmethod
    def find_orientation(cls, p1: Point, p2: Point, p3: Point):
        cross_product = (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)

        if cross_product == 0:
            return 0
        elif cross_product > 0:
            return 1
        else:
            return -1
    
    @classmethod
    def do_segments_intercept(cls, s1: Segment, s2: Segment):
        if s1.smaller == s2.smaller or s1.smaller == s1.greater or s1.smaller == s2.greater or s1.smaller == s2.greater:
            return True
        
        orientation_1 = cls.find_orientation(s2.greater,s2.smaller,s1.greater)
        orientation_2 = cls.find_orientation(s2.greater,s2.smaller,s1.smaller)
        if orientation_1 == orientation_2:
            return False
        return True
    
    @classmethod
    def __partition(cls, array, low, high):
        # Pivot is last element
        pivot = array[high]
        p = low-1
        
        for j in range(low,high):
            if array[j].x < pivot.x or (array[j].x == pivot.x and array[j].y < pivot.y):
                p = p + 1
                (array[p], array[j]) = (array[j], array[p])
                
        (array[p + 1], array[high]) = (array[high], array[p + 1])
        
        return p + 1
        
    @classmethod
    def hull_sort(cls, array, low, high):
        if low < high:
            pi = cls.__partition(array, low, high)
            cls.hull_sort(array, low, pi-1)
            cls.hull_sort(array, pi+1, high)