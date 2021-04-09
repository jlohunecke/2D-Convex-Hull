#module imports
from random import randint
import matplotlib.pyplot as plt

# sort points lexicographically
def lexicoSort(points):
    return sorted(points, key=lambda k: [k[0], k[1]])

# checks weather points x,y and z make a right turn using determinant-criterion
def rBend(x, y, z):
    return (((y[0]-x[0])*(z[1]-x[1]))-((z[0]-x[0])*(y[1]-x[1])) < 0)

# computes upper hull
def upperHull(points):
    u = [points[i] for i in range(0,2)]

    for i in range(2, len(points)):
        u.append(points[i])

        while (not rBend(u[len(u)-3], u[len(u)-2], u[len(u)-1])) and len(u) > 2:
            u.remove(u[len(u)-2])

    return u

# computes lower hull
def lowerHull(points):
    l = [points[i] for i in range(0,2)]

    for i in range(2, len(points)):
        l.append(points[i])

        while (rBend(l[len(l)-3], l[len(l)-2], l[len(l)-1])) and len(l) > 2:
            l.remove(l[len(l)-2])

    l.reverse()
    return l

# computes convex hull
def convexHull (points):
    points = lexicoSort(points)
    u = upperHull(points)
    l = lowerHull(points)

    return u + l


# coordinate sampling
points = []

for i in range(0,40):
    a = (randint(-1000, 1000), randint(-1000, 1000))
    points.append(a)

# compute convex hull
convexHull = convexHull(points)

# plot
plt.scatter([i[0] for i in points], [i[1] for i in points], marker='x')
plt.plot([i[0] for i in convexHull], [i[1] for i in convexHull], c="g")
plt.show()

