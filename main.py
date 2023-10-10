from utils.hull_interception import HullInterception
from utils.tools import Tools

# Achar envoltória
hull_1 = []
hull_2 = []


# Now we'll create 'segments' lists and the 'hull' list; both of them will be used
segments = HullInterception.create_hull_segments(hull_1, hull_2)
points = hull_1.append(hull_2)
Tools.hull_sort(points)