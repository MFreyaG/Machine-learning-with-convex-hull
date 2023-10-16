from entities.point import Point
from utils.tools import Tools

class ConvexHull:
    def __init__(self, point_set):
        self.point_set = point_set
        self.hull = []
        self.tools = Tools
    
    def print_point_set(self):
        for point in self.point_set:
            point.print_coordinates()
        
    def find_point_index(self, p):
        index = 0
        
        for point in self.point_set:
            if p.x == point.x and p.y == point.y:
                return index
            index += 1
        
    def find_ancor(self):
        ancor = self.point_set[0]
        
        for point in self.point_set:
            if point.x < ancor.x:
                ancor = point
        
        return ancor
    
    def find_next_ancor(self, p, q):
        for point in self.point_set:
            if self.tools.find_orientation(p,q,point) == 1:
                q = point
        
        return q
    
    def find_convex_hull(self):
        set_size = len(self.point_set)
        
        ancor = self.find_ancor()
        self.hull.append(ancor)
        next = self.point_set[(self.find_point_index(ancor)+1)%set_size]
        
        current = self.find_next_ancor(ancor, next)
        
        while True:
            self.hull.append(current)
            next = self.point_set[(self.find_point_index(current)+1)%set_size]
            current = self.find_next_ancor(current, next)
            
            if current.x == self.hull[0].x and current.y == self.hull[0].y:
                break
        
    def print_convex_hull(self):
        for point in self.hull:
            point.print_coordinates()
            
    def clean_current_hull(self):
        self.hull = []