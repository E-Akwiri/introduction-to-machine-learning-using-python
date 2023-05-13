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


# In[7]:


# Generate some random data
x = np.random.normal(0, 1, 500)

# Create a 1D dataset
data = {'x': x}

# Convert to a pandas dataframe
import pandas as pd
df = pd.DataFrame(data)

# Display the first 5 rows of the dataframe
print(df.head())


# In[10]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate some random data
x = np.random.normal(0, 1, 500)

# Create a 1D dataset
data = {'x': x}

# Convert to a pandas dataframe
df = pd.DataFrame(data)

# Create a density plot
sns.kdeplot(data=df, x="x")

# Add labels and title
plt.xlabel('Sales')
plt.ylabel('Density')
plt.title('Sales distribution in 30 days')

# Display the plot
plt.show()


# In[ ]:




