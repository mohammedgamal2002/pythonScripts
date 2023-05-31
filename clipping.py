from sympy import symbols, Eq, solve
import numpy as np


def Solve_Intersection(segment_vertices, edge_vertices):
    intersect = False
    alpha, beta = symbols('alpha beta')

#Segment
    point_seg = segment_vertices[0]
    V_ks_seg = segment_vertices[1] - segment_vertices[0]
    

#Edge
    point = edge_vertices[0]
    V_ks = edge_vertices[1] - edge_vertices[0]


    eq1 = Eq(lhs= point[0] + alpha * V_ks[0], rhs = point_seg[0] + beta * V_ks_seg[0])
    eq2 = Eq(lhs= point[1] + alpha * V_ks[1], rhs = point_seg[1] + beta * V_ks_seg[1])

    result = solve((eq1,eq2) ,(alpha, beta))
    print(f'alpha = {result[alpha]}')
    print(f'beta = {result[beta]}')

    if(0 < result[alpha] < 1  and 0< result[beta] < 1):
        intersect = True
        x_intersect = point[0] + result[alpha] * V_ks[0]
        y_intersect = point[1] + result[alpha] * V_ks[1]
        point_of_intersection = np.array([x_intersect, y_intersect])
        return intersect, point_of_intersection

    return intersect, np.zeros(shape=(2))


def Clip(vertices, line_segment):
    count = 0
    for i in range(len(vertices)):
        vk = vertices[i]
        if(i == 0):
            vs = vertices[len(vertices) - 1]
        else:
            vs = vertices[i - 1]
        e = np.array([vs, vk])
        has_intersection, point_intersect = Solve_Intersection(line_segment, edge_vertices= e)
        if(has_intersection):
            count = count + 1
            print("\n edge :{e} intersect with segment : {s}\n at point{point} \n".format(e=e, s = line_segment, point = point_intersect))
    print("number of intersection {num}".format(num = count))



# sp1 = np.array([30,15])
# sp2 = np.array([20,16])
# s = [sp1, sp2]

# ep1 = np.array([15,10])
# ep2 = np.array([22, 10])
# e = [ep1, ep2]


# vertices = np.array([[15,10],[22, 10], [25,18], [20,25], [10,20]])
# Clip(vertices, s)

s = np.array([[1,11], [25,12]])
vertices = np.array([[1,5], [15,7], [10,20]])
Clip(vertices, s)

