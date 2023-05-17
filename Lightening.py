import numpy as np

global PRECISION
PRECISION = 2
#For values exactly halfway between rounded decimal values, NumPy rounds to the nearest even value.
#Thus 1.5 and 2.5 round to 2.0, -0.5 and 0.5 round to 0.0, etc.

def Vector(p1, p2):
    return np.round(p1 - p2, decimals = PRECISION)

def UnitVec(vector):
    return np.round(vector / np.linalg.norm(vector), decimals = PRECISION)

#throws error when point = light_source_point ==>> magnitude = 0
def CalcReflection(point, light_sources_p, viewer_p, norm, Ia, I, Ka, Kd, Ks, Ns):

    v = UnitVec(Vector(viewer_p , point))
    light_sources_vec = []
    H = []
    for i in range(0,len(light_sources_p)):
        if (not ((light_sources_p[i] == point).all())):
            light_sources_vec.append(UnitVec(Vector(light_sources_p[i], point)))
    for i in range(0,len(light_sources_vec)):
        H.append(UnitVec(light_sources_vec[i] + v)) # H = L + V / ||L+V||


    #print(light_sources_vec)
    print("Unit Vectors : \n")
    print("V = {viewer_vector}\n".format(viewer_vector = v))
    print("L = {light_vectors}\n".format(light_vectors = light_sources_vec))
    print("H = {halfpoint_vectors}\n".format(halfpoint_vectors = H))
    # Summation of Kd(L N) + Ks(H N)^Ns
    print("Summation of ( Kd(L N) + Ks(H N)^Ns ):\n")
    sum = 0
    for i in range(0, len(light_sources_vec)):
        x = Kd *np.dot(light_sources_vec[i], norm) + Ks * (np.dot(H[i], norm))**Ns
        x = np.round(x, decimals= PRECISION)
        sum += x
        print("Diffuse & Specular For L{ls_num} = {y}".format(ls_num = i ,y = x))
    sum = np.round(sum, decimals = PRECISION)
    print("Summation of Diffuse & Specular For all light sources = {y}".format(y = sum))
    print("\nCalculating Reflected Light : \n")
    print("I_reflec = Ka * Ia + I* \u03A3( Kd(L N) + Ks(H N)^Ns )\n")
    print("I_reflec = Ka * Ia + I*({y})\n".format(y = sum))
    print("I_reflec = {Ka} * {Ia} + {I}*({y})\n".format(y = sum, Ka = Ka , Ia = Ia, I=I,))

    I_reflec = Ka * Ia + I * sum
    I_reflec = np.round(I_reflec, decimals= PRECISION)
    return I_reflec


point = np.array([106, 0, 68])

l1 = np.array([0,12,0])
l2 = np.array([106,12,0])
l3 = np.array([0,12,68])
l4 = np.array([106,12,68])
light_sources_points = [l1, l2, l3 ,l4]

viewer = np.array([53, 10, -50])
norm = np.array([0, 1, 0])

Ia = 20
I = 50000
Ka = 0.8
Kd = 0.6
Ks = 0.7
Ns = 2

Ir = CalcReflection(point, light_sources_points, viewer
               , norm, Ia, I, Ka, Kd, Ks, Ns)
print("\nI_reflected from point{p} = {I_reflec}\nwith Precision of({prec})".format(p = point, I_reflec = Ir,prec= PRECISION))
