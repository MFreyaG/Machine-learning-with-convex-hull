from entities.point import Point

from utils.hull_interception import HullInterception
from utils.tools import Tools

# Achar envoltória
hull_1 = [Point(0,0), Point(0.5,2), Point(1,0)]
hull_2 = [Point(2.5,2.5), Point(1,2), Point(0.5,1), Point(2,0)]


# Now we'll create 'segments' lists and the 'hull' list; both of them will be used
segments = HullInterception.create_hull_segments(hull_1, hull_2)
points = hull_1 + hull_2
Tools.hull_sort(points, 0, len(points)-1)

# Checking if intercept
print(HullInterception.do_hulls_intercept(segments, points))