#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[13]:


# styles and line colors
plt.plot(x, x + 1, linestyle='solid')
plt.plot(x, x + 2, linestyle='dashed')
plt.plot(x, x + 3, linestyle='dashdot')
plt.plot(x, x + 4, linestyle='dotted');
# For short, you can use the following codes:
plt.plot(x, x + 5, linestyle='-') # solid
plt.plot(x, x + 6, linestyle='--') # dashed
plt.plot(x, x + 7, linestyle='-.') # dashdot
plt.plot(x, x + 8, linestyle=':'); # dotted


# In[14]:


#### controlling colors and styles with shorthand syntax
plt.plot(x, x + 0, '-g') # solid green
plt.plot(x, x + 1, '--c') # dashed cyan
plt.plot(x, x + 2, '-.k') # dashdot black
plt.plot(x, x + 3, ':r'); # dotted red


# In[24]:


#### adjusting the limits of the plot
#### use the plt.xlim() and the plt.ylim() methods

### we can add labels and legends
###### for labels, we use the function plt.xlabel and plt.ylabel
######### for legend, we use the function plt.legend()
plt.plot(x, np.sin(x))

plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5)
plt.xlabel("X-axis")
plt.ylabel("Sin(x)")

plt.legend()


# In[21]:


### we can reverse the plot above
plt.plot(x, np.sin(x)) 


### reversing the y-axis
plt.xlim(10, 0)
plt.ylim(1.2, -1.2)
plt.xlabel("X-axis")
plt.ylabel("Sin(x)")


# In[22]:


## we can automatically tighten the bonds around the current plot

plt.plot(x, np.sin(x))
plt.axis('tight')
plt.xlabel("X-axis")
plt.ylabel("Sin(x)")


# In[25]:


## we can put equal aspects ratio on the plot so that 1 unit of x = 1 unit of y
plt.plot(x, np.sin(x))
plt.axis('equal')
plt.xlabel("X-axis")
plt.ylabel("Sin(x)")

plt.legend()


# In[26]:


plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), ':b', label='cos(x)')
plt.axis('equal')

plt.legend();


# In[28]:


### plt.xlabel() -> ax.set_xlabel
### plt.ylabel() -> ax.set_ylabel
###### plt.xlim() -> ax.set_xlim()
###### plt.ylim() -> ax.set_ylim()

######### plt.title -> ax.set_title()

### THESE ARE USEFUL MATPLOTLIB FUNCTIONS

ax = plt.axes()
ax.plot(x, np.sin(x))
ax.set(xlim=(0, 10), ylim=(-2, 2),
xlabel='X-axis',
ylabel='Sin(x)',
title='MATPLOTLIB FUNCTIONS')


# In[ ]:




