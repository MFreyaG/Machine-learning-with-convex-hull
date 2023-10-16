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
    # Check if point q lies on line segment pr
    def on_segment(cls, p, q, r):
        return (
            (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x))
            and (q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y))
        )
    
    
    @classmethod
    def do_segments_intercept(cls, s1: Segment, s2: Segment):
        if s1.smaller == s2.smaller or s1.smaller == s1.greater or s1.smaller == s2.greater or s1.smaller == s2.greater:
            return True
        
        o1 = cls.find_orientation(s1.smaller, s1.greater, s2.smaller)
        o2 = cls.find_orientation(s1.smaller, s1.greater, s2.greater)
        o3 = cls.find_orientation(s2.smaller, s2.greater, s1.smaller)
        o4 = cls.find_orientation(s2.smaller, s2.greater, s1.greater)
        
        # General case
        if o1 != o2 and o3 != o4:
            return True

        # Special cases (colinear or one segment's endpoint on the other segment)
        if (
            o1 == 0 and cls.on_segment(s1.smaller, s2.smaller, s1.greater)
            or o2 == 0 and cls.on_segment(s1.smaller, s2.greater, s1.greater)
            or o3 == 0 and cls.on_segment(s2.smaller, s1.smaller, s2.greater)
            or o4 == 0 and cls.on_segment(s2.smaller, s1.greater, s2.greater)
        ):
            return True
        return False
    
    @classmethod
    def hullsort(cls, array):
        cls._hull_sort(array, 0, len(array)-1)
        
        
    @classmethod
    def _hull_sort(cls, array, low, high):
        if low < high:
            pi = cls._partition(array, low, high)
            cls._hull_sort(array, low, pi-1)
            cls._hull_sort(array, pi+1, high)
    
    @classmethod
    def _partition(cls, array, low, high):
        # Pivot is last element
        pivot = array[high]
        p = low-1
        
        for j in range(low,high):
            if array[j].x < pivot.x or (array[j].x == pivot.x and array[j].y < pivot.y):
                p = p + 1
                (array[p], array[j]) = (array[j], array[p])
                
        (array[p + 1], array[high]) = (array[high], array[p + 1])
        
        return p + 1
    