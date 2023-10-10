class ConvexHull:
    def __init__(self, point_set):
        self.point_set = point_set
        self.hull = []
        self.utils = Utils
        
    def find_ancor(self):
        ancor = self.point_set[0]
        
        for point in s:
            if point.x < ancor.x:
                ancor = point
        
        return ancor
    
    def find_next_point(self, p, q):
        for point in self.point_set:
            if self.utils.find_orientation(p,q,point) == 1:
                q = point
        
        return q
    
    def find_convex_hull(self):
        current_point = self.find_ancor()
        next_point = self.point_set[1]
        
        self.hull.append(current_point)
        
        while next_point.x != self.hull[0].x and next_point.y != self.hull[0].y:
            current_point = self.find_next_point(current_point, next_point)
            next_point = self.point_set[2]
            
            self.hull.append(current_point)
            
        
    def print_convext_hull(self):
        for point in self.hull:
            point.print_coordinates()
            
    def clean_current_hull(self):
        self.hull = []