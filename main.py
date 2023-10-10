class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def print_coordinates(self):
        print(f'({self.x},{self.y})')

class Utils:
	def find_orientation(p1: Point, p2: Point, p3: Point):
		cross_product = (p2.y-p1.y)*(p3.x-p2.x)-(p2.x-p1.x)*(p3.y-p2.y)

		if cross_product == 0:
			return 0
		elif cross_product > 0:
			return 1
		else:
			return -1

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

s = []      
s.append(Point(1,1)), s.append(Point(1.56,1.46)), s.append(Point(2.02,1.18)) 
s.append(Point(2.4,1.68)), s.append(Point(1.26,2.06)), s.append(Point(2,2))

hull = ConvexHull(s)
hull.find_convex_hull()
hull.print_convext_hull()
        