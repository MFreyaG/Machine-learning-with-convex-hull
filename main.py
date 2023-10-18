from matplotlib import pyplot as plt
from numpy.random import randint

from entities.point import Point

from utils.convex_hull import ConvexHull
from utils.hull_interception import HullInterception
from utils.tools import Tools

### This was implemented as a function on Colab

full_point_set = []

random_point_set1 = []
for x in range(0,5):
  point_temp = Point(randint(0,35),randint(0,25))
  random_point_set1.append(point_temp)
  full_point_set.append(point_temp)

new_array_point_set = Tools.point_to_list(random_point_set1)

random_point_set2 = []
for x in range(0,5):
  point_temp = Point(randint(-5,35),randint(-15,25))
  random_point_set2.append(point_temp)
  full_point_set.append(point_temp)

new_array_point_set_full = Tools.point_to_list(set=full_point_set)
new_array_point_set1 = Tools.point_to_list(random_point_set1)
new_array_point_set2 = Tools.point_to_list(set=random_point_set2)

plt.scatter(x=new_array_point_set_full[0],y=new_array_point_set_full[1])

new_hull1 = ConvexHull(random_point_set1)
new_hull_points1 = new_hull1.find_convex_hull()
new_hull_points_array1 = Tools.point_to_list(set=new_hull_points1)
new_hull_points_array1[0].append(new_hull_points1[0].x)
new_hull_points_array1[1].append(new_hull_points1[0].y)

new_hull2 = ConvexHull(random_point_set2)
new_hull_points2 = new_hull2.find_convex_hull()
new_hull_points_array2 = Tools.point_to_list(set=new_hull_points2)
new_hull_points_array2[0].append(new_hull_points2[0].x)
new_hull_points_array2[1].append(new_hull_points2[0].y)

plt.plot(new_hull_points_array1[0],new_hull_points_array1[1], color="red")
plt.plot(new_hull_points_array2[0],new_hull_points_array2[1], color="green")
plt.show()


hull_interception = HullInterception()

# Now we'll create 'segments' lists and the 'hull' list; both of them will be used
segments = hull_interception.create_hull_segments(new_hull_points1, new_hull_points2)


# Now we'll sort the hull points
points = new_hull_points1 + new_hull_points2
Tools.hullsort(points)

# Checking if intercept
print(hull_interception.do_hulls_intercept(segments, points))

print("Printing points hull 1")
for p in points:
    if p.hull_id == 1:
        print(p.__dict__)
        
print("Printing points hull 2")
for p in points:
    if p.hull_id == 2:
        print(p.__dict__)