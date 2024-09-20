# Studying time form 0 - infinity
#exam score form 0 - 100
# represent this as a 2d coordinate system
#linear regression tries to find a line that fits a set of points "the best"
#for linear regression, we care about minimizing the "error"
#error of is how far our prediction is from the reality
#we want to find a function which minimizes this error
# for a linear function y = mx + b
# we expect to find a line that has a relatively low error
# for y = mx+b we want to adjust m and b so we can find the best possible y
# the error funciton E = (1/n) * Summation from i to n (yi - (yhat(predicted vallue)))^2 this is the mean squared error
# this function 
#this i a mathetimatical way of getting the y value of the actual point and substracting the actual value and then square the actual difference
# we find the average error which is called the mean squared error, a fancy way of saying
# we take the difference of all the actual points and square the difference and divide it by the actual mnumber of points
# we want to minimize the error funciton, so we are trying to get the lowest possible e
# to do this, we take th epartial derivative with respect to m and b
#go to the opposite direction of the steepest gradient
# take partial derivative with respect to m
#we substract because we want to go to to the direction opposite of the steepest gradient descent
#the lower the learning the rate, the more detail oriented
# learning rate of .001

import pandas as pd
import matplotlib.pyplot at plt
#studytime, score
data = pd.read_csv('data.csv')
print(data)
plt.scatter(data.tsudytime, data.score) #scatter plot
plt.show()#show the scatter plot

def loss_function(m, b, points):
    total_error = 0 #we add all individual squared errors to this
    for i in range(len(points)):
        x = points.iloc[i].studytime
        y = points.iloc[i].score
        total_error +=((y - m * x + b) ** 2)
    total_error/float(len(points)) #tells us how much we are off from the actual result

#we want to minimze the loss function, you can use it to calculate loss, we want to use

#L is learning rate
def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_graident = 0
    n = len(points)

    for i in range(n):
        x = points.iloc[i].studytime
        y = points.iloc[i].score

        m_gradient += (-2/n) * x * (y - m_now + b_now) 
        b_gradient += (-2/n) * (y - m_now + b_now) 

    m = m_now - m_gradient * L
    b = b_now * b_gradient * L
    return m, b
    
m = 0 
b = 0
L = 0.0001
epochs = 100 #how many iterations we do
for i in range(epochs):
    m, b = gradient_descent(m, b, data,L)

print(m, b)
plt.scatter(data.studytime, data.score, color="black")
plt.plot(list(range(20, 80)), [m * x + b for x in range(20, 80)], color = "red")
plt.show()