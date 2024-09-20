import numpy as np
import matplotlib.pyplot as plt


def z_function(x, y):
    return np.sin(5 * x ) * np.cos(5 * y) / 5

def calculate_gradient(x, y):
    #so we need to do partial derivative with respect to x
    #partial derivative with respect to y
    #we are returning the gradient vector
    return np.cos(5*x) * np.cos(5*y), -np.sin(5*x) *np.sin(5 * y)




x = np.arange(-1, 1, .05)
y = np.arange(-1, 1, .05)
X, Y = np.meshgrid(x, y)
Z = z_function(X, Y)

current_pos1 = (0.7, 0.4, z_function(.7, .4))
current_pos2 = (.3 , .8, z_function(.7, .4))
current_pos2 = (-.3 , .5, z_function(.7, .4))


learning_rate = 0.01

ax = plt.subplot(projection = "3d", computed_zorder=False) #we are prioritizing the point
#you specify a tolerance rather than the range, if loss change or improvement is negligible, you stop
for _ in range(1000):
    X_derivative, Y_derivative = calculate_gradient(current_pos[0], current_pos[1])
    X_new, Y_new = current_pos[0] - learning_rate * X_derivative, current_pos[1] - learning_rate * Y_derivative
    current_pos = (X_new, Y_new, z_function(X_new, Y_new))
    ax.plot_surface(X, Y, Z, cmap = "viridis", zorder = 0)
    ax.scatter(current_pos[0], current_pos[1], current_pos[2], color= "magenta", zorder = 1)
    plt.pause(0.001)
    ax.clear()




# ax = plt.subplot(projection = "3d")

# ax .plot_surface(X, Y, Z, cmap = "viridis")
# plt.show()