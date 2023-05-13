#!/usr/bin/env python
# coding: utf-8

# In[1]:


##### plotting a 2D function

#### x and y have 50 steps from 0 to 5
import numpy as np


# In[3]:


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]

z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[6]:


### creating a density and contour plot

plt.imshow(z, origin = 'lower', extent = [0, 5, 0, 5],
          cmap = 'viridis')
plt.colorbar();


# In[ ]:




