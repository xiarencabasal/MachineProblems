import numpy as np

x1, y1 = map(int, input("Input the first point: ").split())
x2, y2 = map(int, input("Input the second point: ").split())
x3, y3 = map(int, input("Input the third point: ").split())

# Coefficients of variable X for the systems of linear equations
A = np.array([[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]])
# Constants at the right-hand side.
B = np.array([[-(x1**2 + y1**2), -(x2**2 + y2**2), -(x3**2 + y3**2)]])
B = np.transpose(B)
# Solutions to the systems of equations
C = np.linalg.inv(A).dot(B)

# Computation for center (h,k) and radius 
h = -C[0]/2
k = -C[1]/2
r = np.sqrt((C[0]**2 + C[1]**2 - 4*C[2])/4)

print('The center is at ', h, k)
print('The radius of the circle is ', r)
print('The coefficients D, E, F of the general equation are ', C) 