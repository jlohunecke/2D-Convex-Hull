#module imports
from random import randint
import matplotlib.pyplot as plt

# checks weather points x,y and z make a left turn using determinant-criterion
def lBend(x, y, z):
    return (((y[0]-x[0])*(z[1]-x[1]))-((z[0]-x[0])*(y[1]-x[1])) > 0)

# checks weather points x,y and z make a right turn using determinant-criterion
def rBend(x, y, z):
    return (((y[0]-x[0])*(z[1]-x[1]))-((z[0]-x[0])*(y[1]-x[1])) < 0)

# computes upper bridge
def upperBridge(points,i,k,j):
    cl = k
    cr = k+1

    v = points[cl]
    w = points[cr]
    p2 = points [k+2]
    while (not rBend(points[cl-1], points[cl], points[cr]) or not rBend(points[cl], points[cr], points[cr+1])):
        while not rBend(points[cl-1], points[cl], points[cr]):
            cl = cl-1
        while not rBend(points[cl], points[cr], points[cr+1]):
            cr = cr+1
    return cl, cr

# computes lower bridge
def lowerBridge(points, i, k, j):
    cl = k
    cr = k + 1

    v = points[cl]
    w = points[cr]
    p2 = points[k + 2]
    while (not lBend(points[cl + 1], points[cl], points[cr]) or not lBend(points[cl], points[cr], points[cr - 1])):
        while not lBend(points[cl + 1], points[cl], points[cr]):
            cl = cl + 1
        while not lBend(points[cl], points[cr], points[cr - 1]):
            cr = cr - 1
    return cl, cr

# merge left and right convex hull
def merge(points, i, k, j):
    a, b = upperBridge(points, i, k, j)
    c, d = lowerBridge(points, i, k, j)

    points = points[:a] + points[b:d] + points[c:]
    return points

def dcConvexHull (points, i, j):
    if j-i <= 2:
        return points[i:j]
    else:
        k = int((i+j)/2)
        mid = int(len(points)/2)
        pl = dcConvexHull(points, i,k)
        pr = dcConvexHull(points, k+1, j)

        return merge(points, i,j,k)




# coordinate sampling
points = []

for i in range(0,40):
    a = (randint(-1000, 1000), randint(-1000, 1000))
    points.append(a)

# compute convex hull
convexHull = dcConvexHull(points, 0, len(points)-1)

# plot
plt.scatter([i[0] for i in points], [i[1] for i in points])
plt.plot([i[0] for i in convexHull], [i[1] for i in convexHull], c="g")
plt.show()

