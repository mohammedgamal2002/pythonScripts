import numpy as np
import math

def Transform2D(transforms, vertex):
    CTM = np.identity(3)
    i = len(transforms) - 1
    while i >= 0:
        CTM = np.matmul(CTM, transforms[i])
        i = i-1
    return np.matmul(CTM, vertex)



# Usage

T1 = np.array([[1,0 , -20],
              [0, 1, -5],
              [0, 0, 1]])

theta = math.radians(45)

T2 = np.array([[math.cos(theta), -math.sin(theta) , 0],
              [math.sin(theta), math.cos(theta), 0],
              [0, 0, 1]])

T3 = np.array([[1, 0 , 20],
              [0, 1, 5],
              [0, 0, 1]])

transforms = np.array([T1,T2,T3])
print(Transform2D(transforms, np.array([5,10,1])))