#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Author: Gaurav Nagal
Created: 09/08/2019
Course: FE595
Assignment 1: Python Refresher
'''


# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[20]:


# Taking one period (2 * pi) on X-axis
X = np.arange(0, 2 * np.pi, 0.001)

# Sine and Cosine graph for one period
sine = np.sin(X)
cosine = np.cos(X)

# Generating plot
plt.plot(X, sine, X, cosine)
plt.subplot().legend(['Sine','Cosine'])  
plt.subplot().axvline(x = 0, color = 'black', lw = 2.5)
plt.subplot().axhline(y = 0, color = 'black', lw = 2.5)
plt.show()


# In[ ]:




