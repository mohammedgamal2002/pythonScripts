import numpy as np
import math

np.set_printoptions(suppress=True)


def ToSpecialMatrix(viewer, midpoint):
    #translate by (- viewer)
    translate_matrix = np.array([
            [1, 0, 0, (-viewer[0])],
            [0, 1, 0,(- viewer[1]) ],
            [0, 0, 1, (- viewer[2])],
            [0, 0, 0, 1]
            ])
    delta_x = midpoint[0] - viewer[0]
    delta_y = midpoint[1] - viewer[1]
    delta_z = midpoint[2] - viewer[2]
    theta_x = math.atan(np.abs(delta_y)/delta_z)
    theta_y = math.atan(np.abs(delta_x)/delta_z)

    rotation_x_angle = 0
    rotation_y_angle = 0

    if delta_z >= 0:
        if delta_x >= 0:
           rotation_y_angle = - theta_y 
        else:
            rotation_y_angle = theta_y

        if delta_y >= 0:
            rotation_x_angle = theta_x
        else:
            rotation_x_angle = - theta_x

    print("Translate By ({x}, {y}, {z})".format(x= (-viewer[0]), y=(-viewer[1]), z=(-viewer[2])))
    print("Rotate Around X by ({angle})".format(angle = rotation_x_angle))
    print("Rotate Around Y by ({angle})".format(angle = rotation_y_angle))

    rotation_x_matrix = np.array([
            [1, 0, 0, 0],
            [0, math.cos(rotation_x_angle), - math.sin(rotation_x_angle), 0],
            [0, math.sin(rotation_x_angle), math.cos(rotation_x_angle), 0],
            [0, 0, 0, 1]
            ])

    rotation_y_matrix = np.array([
            [math.cos(rotation_y_angle), 0, math.sin(rotation_y_angle), 0],
            [0, 1, 0, 0],
            [- math.sin(rotation_y_angle), 0, math.cos(rotation_y_angle), 0],
            [0, 0, 0, 1]
            ])
    CTM = np.matmul(np.matmul(rotation_y_matrix, rotation_x_matrix), translate_matrix)
    print(CTM)
    return CTM

def Ortho3D(viewer, midpoint, point, zp):
    CTM_sp = ToSpecialMatrix(viewer, midpoint)
    projection = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, zp],
            [0, 0, 0, 1]
            ])
    CTM_gn = np.linalg.inv(CTM_sp)
    CTM_all = np.matmul(np.matmul(CTM_gn, projection,), CTM_sp)
    return np.matmul(CTM_all, point)

def Perspective3D(viewer, midpoint, point, zp):
    CTM_sp = ToSpecialMatrix(viewer, midpoint)
    alpha = zp/point[2]
    projection = np.array([
            [alpha, 0, 0, 0],
            [0, alpha, 0, 0],
            [0, 0, 0, zp],
            [0, 0, 0, 1]
            ])
    CTM_gn = np.linalg.inv(CTM_sp)
    CTM_all = np.matmul(np.matmul(CTM_gn, projection,), CTM_sp)
    return np.matmul(CTM_all, point)

# viewer = np.array([15, 25, 35, 1])
# midpoint = np.array([10, 40, 100, 1])

# point = np.array([15, 40, 120, 1])

# zp = 33.45


viewer = np.array([0, 1.6, 0, 1])
midpoint = np.array([10, 10, 10, 1])

point = np.array([12, 17, 7, 1])

zp = 5

print(np.round(Perspective3D(viewer, midpoint, point, zp), decimals= 2))

