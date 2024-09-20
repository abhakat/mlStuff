import numpy as np
import matplotlib.pyplot as plt


def y_function(x):
    return np.sin(x)

# to find minimum of a function, we have to compute the derivative of a funciton
# positive slope
# we care anout how sensitive the y function is respective to 
# we go in the opposite direction to decrease
# we multiply the gradient("slope") by a constant
# we need to compute derivative, calculate it at a particular point, go potentially the opposite directio to progess towards minima

def y_derivative(x):
    return np.cos(x)

x = np.arange(-5, 5, .1)
y = y_function(x)

current_pos = (1.5, y_function(.15))
learning_rate = .01

# plt.plot(x, y)
# plt.show()


for _ in range(1000):
    new_x = current_pos[0] - learning_rate * y_derivative(current_pos[0])
    new_y = y_function(new_x)
    current_pos = (new_x, new_y)
    plt.plot(x, y)
    plt.scatter(current_pos[0], current_pos[1], color="red")
    plt.pause(.001)
    plt.clf()



#the steeper the slope, the faster we approach the minimia
#we usually start at multiple points and check where it converges to find the absolute minima

