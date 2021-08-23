#Spiral Index
#First Method:
def spiral_index(x, y):
    startx = starty = output = 0
    direction = step = 1
    while  (starty != y) or (startx != x):
        for i in range(step):
            if (starty == y) and (startx == x):
                break
            output +=1
            startx += direction
    
        for i in range(step):
            if (starty == y) and (startx == x):
                break
            output +=1
            starty += direction
        
        direction *= -1
        step +=1
    print(" Spiral index of ("+str(x)+", "+str(y)+") is "+ str(output)+".")

#Second method:
def spiral_index(x, y):
    layer = max(abs(x),abs(y))
    output = 0
    for i in range(layer):
        output += 8*(i)
    step = 1 + 2*(layer-1)
    output += 1
    startx = layer
    starty = 1-layer
    direction = 1
    while  (starty != y) or (startx != x):
        for i in range(step):
            if (starty == y) and (startx == x):
                break
            output +=1
            starty += direction
        step +=1
        direction *= -1
        for i in range(step):
            if (starty == y) and (startx == x):
                break
            output +=1
            startx += direction    
    print(" Spiral index of ("+str(x)+", "+str(y)+") is "+ str(output)+".")



#Euclidean Distance:
import random
class ConvexHull:
	def __init__(self, points):
		if not points:
			self.points = [(random.randint(0,100),random.randint(0,100)) for i in range(50)]
		else:
			self.points = points
		self.hull = self.compute_convex_hull()
    
	def get_cross_product(self,p1, p2, p3):
		return ((p2[0] - p1[0])*(p3[1] - p1[1])) - ((p2[1] - p1[1])*(p3[0] - p1[0]))

	def get_slope(self,p1, p2):
		if p1[0] == p2[0]:
			return float('inf')
		else:
			return 1.0*(p1[1]-p2[1])/(p1[0]-p2[0])

	def compute_convex_hull(self):
		hull = []
		self.points.sort(key=lambda x:[x[0],x[1]])
		start = self.points.pop(0)
		hull.append(start)
		self.points.sort(key=lambda p: (self.get_slope(p,start), -p[1],p[0]))
		for pt in self.points:
			hull.append(pt)
			while len(hull) > 2 and self.get_cross_product(hull[-3],hull[-2],hull[-1]) < 0:
				hull.pop(-2)
		return hull

def find_farthest_points(points):
    h = ConvexHull(points).hull
    dmax = 0
    listofpoints = []
    for i in range(len(h)):
        for j in range(len(h)):
            d = ((h[j][0]-h[i][0])**2+(h[j][1]-h[i][1])**2)**(1/2)
            if d > dmax:
                dmax = d
                firstpoint = (h[j][0],h[j][1])
                secondpoint = (h[i][0], h[i][1])
    listofpoints.extend((firstpoint,secondpoint))
    return listofpoints

