from entities.point import Point
from utils.convex_hull import ConvexHull

n = int(input())
point_set = [Point(input(),input()) for x in range(0,n)]

for point in point_set:
    point.print_coordinates()
    
hull = ConvexHull(point_set)
