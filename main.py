from entities.point import Point

from utils.hull_interception import HullInterception
from utils.tools import Tools

hull_interception = HullInterception()

# Find hull - Grands
# hull_1 = [Point(0,0), Point(0.5,2), Point(1,0)]
hull_1 = [Point(3,0), Point(2.6,1.8), Point(2,1)]
hull_2 = [Point(1.5,2), Point(2,0), Point(2.5,2)]

# Now we'll create 'segments' lists and the 'hull' list; both of them will be used
segments = hull_interception.create_hull_segments(hull_1, hull_2)

# Now we'll sort the hull points
points = hull_1 + hull_2
Tools.hullsort(points)

# Checking if intercept
print(hull_interception.do_hulls_intercept(segments, points))