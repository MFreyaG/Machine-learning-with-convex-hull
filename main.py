from entities.point import Point
from utils.convex_hull import ConvexHull

point_set = []

point_set.append(Point(0,3))
point_set.append(Point(0,0)) 
point_set.append(Point(1,1))
point_set.append(Point(2,2))
point_set.append(Point(3,3))
point_set.append(Point(4,4))
point_set.append(Point(3,1))
point_set.append(Point(1,2))

hull = ConvexHull(point_set)
hull.find_convex_hull()
hull.print_convex_hull()