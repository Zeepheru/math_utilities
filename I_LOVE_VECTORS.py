import numpy as np

def vector_length(a):
    return np.sqrt ( a[0][0] ** 2 + a[1][0] ** 2 + a[2][0] ** 2)

def cross_product(a, b):
    x1, x2 = a[0][0], b[0][0]
    y1, y2 = a[1][0], b[1][0]
    z1, z2 = a[2][0], b[2][0]

    return np.array([
        [ y1 * z2 - y2 * z1 ],
        [ -(x1 * z2 - x2 * z1) ],
        [ x1 * y2 - x2 * y1 ]
    ])

def unit_vector(a):
    x = a[0][0]
    y = a[1][0]
    z = a[2][0]

    mod_a = vector_length(a)

    return np.array([
        [ x / mod_a ],
        [ y / mod_a ],
        [ z / mod_a ]
    ])

def dot_product(a, b):
    x1, x2 = a[0][0], b[0][0]
    y1, y2 = a[1][0], b[1][0]
    z1, z2 = a[2][0], b[2][0]

    return x1 * x2 + y1 * y2 + z1 * z2

def get_angle_rad(a, b):
    return np.arccos( (dot_product(a, b)) / (vector_length(a) * vector_length(b)) )

def get_angle_deg(a, b):
    return np.arccos( (dot_product(a, b)) / (vector_length(a) * vector_length(b)) ) / np.pi * 180

def ratio_theorem(a, b, la = 1, lb = 1):
    return ( a * lb + b * la ) / ( la + lb )

def midpoint(a, b):
    return ratio_theorem(a, b)

def parallel(a, b): #compares int(k * 10 ** 9) - yeah floats are annoying
    x1, x2 = a[0][0], b[0][0]
    y1, y2 = a[1][0], b[1][0]
    z1, z2 = a[2][0], b[2][0]

    #zeroes are an issue atm.
    k1 = x1 / x2
    k2 = y1 / y2
    k3 = z1 / z2

    if k1 * 10 ** 9 == k2 * 10 ** 9 and k2 * 10 ** 9 == k3 * 10 ** 9:
        return True
    else:
        return False

def foot_of_perpendicular(a, b):
    return 0

def length_of_perpendicular(A, b):
    return 0




def main(): #main calculator code lol
    ### nparrays are np.array(array)
    k = -4
    a = np.array([
        [5],
        [4],
        [0]
    ])
    b = np.array([
        [-1],
        [0],
        [4]
    ])
    c = np.array([
        [2 * k],
        [17 + 2 * k],
        [-2 - 1 * k]
    ])
    e = np.array([
        [1],
        [-5],
        [8]
    ])


    e = a + 3 * b

    return cross_product(a, b)

if __name__ == "__main__":
    print(main())