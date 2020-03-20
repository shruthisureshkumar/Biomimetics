#!/usr/bin/env python

import numpy as np
from time import time

F = np.array([[1, 0, 0], 
              [0, 1, 0], 
              [0, 0, 1]])

B = np.array([[1, -2, 1], [-1, 2, -1], [1, -2, 1]])

x0 = np.array([[1, 1, 1]])

u = np.array([[1, 2, -1]])

#Task begins here

def gaussianNoiseModel(sigma, size): 
    #Gaussian G(x, y) can be seperated into G(x) and G(y)
    #           G(x, y) = G(x)*G(y)
    #look for definition of gaussian of x. 
    #you can assume size to be odd
    
    ''' for now calculate Gaussian in 1D '''
    ''' edit the code below to complete the task at hand '''
    Gx = None
    for i in range():
        #create a grid e.g. for size 5, Gx = [-2 -1 0 1 2 ]
        pass
    
    G = None            #calculate gaussian from Gx
    return G


def kalman_prediction(prev_state, u, F, B, sigma):
    #predict the current state based on previous state and model parameters
    # current state is given by x(t) = B*x(t-1) + F*u(t-1) + w(t-1)
    
    size = None                 #determine size of guassian required (hint: it has same dimentions as state vector.
    w = gaussianNoiseModel(sigma, size)
    curr_state = None
    return curr_state

def evaluate(B, F, u, x0):
    x1 = kalman_prediction(x0, u, F, B, 1.4142)
    print x1

if __name__ == "__main__":
    evaluate(B, F, u, x0)
