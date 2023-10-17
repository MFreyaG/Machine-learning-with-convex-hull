from entities.point import Point

from utils.hull_interception import HullInterception
from utils.tools import Tools

hull_interception = HullInterception()

# Find hull - Grands
# hull_1 = [Point(0,0), Point(0.5,2), Point(1,0)]
hull_1 = [Point(1,0), Point(3,0), Point(2,4)]
hull_2 = [Point(0,4), Point(0.9,0), Point(1.9,4)]

# Now we'll create 'segments' lists and the 'hull' list; both of them will be used
segments = hull_interception.create_hull_segments(hull_1, hull_2)
breakpoint()
# Now we'll sort the hull points
points = hull_1 + hull_2
Tools.hullsort(points)

# Checking if intercept
print(hull_interception.do_hulls_intercept(segments, points))