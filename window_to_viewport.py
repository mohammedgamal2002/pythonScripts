class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def WindowToViewPort(rmin, rmax ,dmin, dmax, vertices , has_distortion = False, is_adapted = True, n = 1000):
    if(is_adapted == False):
        temp_min = (n-1) - dmin.y
        temp_max = (n-1) - dmax.y
        dmin.y = min(temp_min, temp_max)
        dmax.y = max(temp_min, temp_max)

    print(dmin.y)
    print(dmax.y)

    scale_x = (dmax.x - dmin.x) / (rmax.x - rmin.x)
    scale_y = (dmax.y - dmin.y) / (rmax.y - rmin.y)

    print("Scale(X) = {scale_x}".format(scale_x = scale_x))
    print("Scale(Y) = {scale_y}".format(scale_y = scale_y))

    if(has_distortion == False):
        print("No Distortion Mode.\n")
        scale = min(scale_x, scale_y)
        scale_x = scale
        scale_y = scale
    else:
        print("Distortion Mode.\n")


    for vertex in vertices:
        vertex.x = dmin.x + (vertex.x - rmin.x) * scale_x
        vertex.y = dmin.y + (vertex.y - rmin.y) * scale_y
    return vertices



# rmin = Point(100,200)
# rmax = Point(700,900)

# dmin = Point(300,400)
# dmax = Point(900,1200)

# vertices = [Point(150,250), Point(400, 400), Point(450, 600), Point(500, 830)]


rmin = Point(5,5)
rmax = Point(105,55)

dmin = Point(10,10)
dmax = Point(610,610)

vertices = [Point(20, 90)]


new_vertices = WindowToViewPort(rmin, rmax, dmin, dmax, vertices, is_adapted= False, n= 2000)
for vertex in new_vertices:
    print("Point({x}, {y})".format(x = vertex.x , y = vertex.y))

