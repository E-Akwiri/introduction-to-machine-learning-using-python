#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[4]:


# create a typical figure
plt.figure()

#### start by creating the first two panels and set the current axis
plt.subplot(4, 2, 2) ### (this includes the rows, columns and panel number)
plt.plot(x, np.sin(x))

#### create the second panel and set the current axis

plt.subplot(4, 2, 4)
plt.plot(x, np.cos(x));

plt.show()


# In[ ]:




