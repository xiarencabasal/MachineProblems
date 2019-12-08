# Importing_of_libraries
import matplotlib.pyplot as plt
import numpy as np
import sys

# User Inputs 
h0 = int(input('Enter the initial height: '))
v = int(input('Enter the magnitude of velocity: '))
angle = int(input('Enter the angle: '))
ax = int(input('Input x-component of the acceleration with the sign: '))
ay = int(input('Input y-component of the acceleration with the sign: '))

# Error if vertical acceleration is 0
if ay == 0:
    sys.exit('Error! Acceleration value must not be equal to zero.')

# X and Y components of the velocity
voy = v*np.sin(angle*np.pi/180)
vox = v*np.cos(angle*np.pi/180)

# Peak time for the highest point
tpk = -voy/ay
# Total distance travelled in the y-axis
y_total = h0 + voy*tpk + 0.5*ay*tpk**2
# Time from peak to ground
t_down = np.sqrt(2*y_total/np.abs(ay))
# Total time of travel
t_total = tpk + t_down
# Total distance travelled in the x-axis
s_horizontal = vox*t_total + 0.5*np.abs(ax)*t_total
# Create vector for x-axis
t = np.linspace(0, t_total, num=10000)
# Substitute time to get y at any instant
y = h0 + t*voy + 0.5*ay*(t**2)

# Modifies x depending on the sign of the acceleration in the x-axis
if ax > 0:
    x = np.linspace(0, s_horizontal, num=10000)
elif ax < 0:
    x = np.linspace(-s_horizontal, 0, num=10000)
    y = np.fliplr(y)

plt.plot(x, y)
plt.title('Projectile Trajectory')
plt.xlabel('Displacement in meters')
plt.ylabel('Height in meters')
plt.grid(which='both')
plt.show()