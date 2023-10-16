from entities.point import Point

from utils.hull_interception import HullInterception
from utils.tools import Tools

hull_interception = HullInterception()

# Find hull - Grands
#hull_1 = [Point(0,0), Point(0.5,2), Point(1,0)]
hull_1 = [Point(3,0), Point(2.5,1), Point(3,2)]
hull_2 = [Point(2.5,2.5), Point(1,2), Point(1,1.5), Point(2,0)]

# Always sort BEFORE
Tools.hull_sort(hull_1, 0, len(hull_1)-1)
Tools.hull_sort(hull_2, 0, len(hull_2)-1)

# Now we'll create 'segments' lists and the 'hull' list; both of them will be used
segments = hull_interception.create_hull_segments(hull_1, hull_2)
points = hull_1 + hull_2

# Checking if intercept
print(hull_interception.do_hulls_intercept(segments, points))