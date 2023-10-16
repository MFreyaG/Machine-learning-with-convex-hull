from entities.point import Point
from utils.convex_hull import ConvexHull

n = int(input())
point_set = [Point(float(input()),float(input())) for x in range(0,n)]

hull = ConvexHull(point_set)

hull.find_convex_hull()
hull.print_convex_hull()