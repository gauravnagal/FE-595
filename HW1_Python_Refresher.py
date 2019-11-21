#!/usr/bin/env python
# coding: utf-8


'''
Author: Gaurav Nagal
Created: 09/08/2019
Course: FE595
Assignment 1: Python Refresher
'''


import numpy as np
import matplotlib.pyplot as plt


def plot_graphs():

    # Taking one period (2 * pi) on X-axis
    X = np.arange(0, 2 * np.pi, 0.001)


    # Sine and Cosine plot for one period
    sine = np.sin(X)
    cosine = np.cos(X)
    tangent = np.tan(X)
    
    # tangent = np.tan(2*(X - np.pi/2))
    threshold = 5
    tangent[tangent > threshold] = np.inf
    tangent[tangent < -threshold] = np.inf
    
    # Generating plot
    plt.plot(X, sine, X, cosine, X, tangent)
    plt.subplot().legend(['Sine', 'Cosine', 'Tangent'])
    plt.subplot().axvline(x = 0, color = 'black', lw = 2.5)
    plt.subplot().axhline(y = 0, color = 'black', lw = 2.5)
    
    plt.show()

if __name__ == '__main__':
    plot_graphs()