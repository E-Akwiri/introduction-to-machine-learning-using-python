#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Importing requried packages and libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error


# In[4]:


DataFrame = "C:/Users/Ayieko/Documents/EMILY/archive/train.csv"
DataFrame = pd.read_csv(DataFrame)
print(DataFrame)


# In[5]:


DataFrame.head()


# In[6]:


#### create a bar chart to visualize the count of passengers in each passenger class ###
### we can determine which class of passengers was more in titanic ###
import matplotlib.pyplot as plt

class_count = DataFrame.groupby('Pclass').size().reset_index(name='count')
plt.bar(class_count['Pclass'], class_count['count'])
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.show()

#### passenger class 3 had the highest passengers; 500 in count


# In[15]:


DataFrame.info()
#### this gives the info about the dataset


# In[7]:


#### we generate a histogram showing the distribution of the ages of passenges

plt.hist(DataFrame['Age'].dropna(), bins=10)
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

### from the histogram, we can tell the age group with the highest and least numbers in the titanic ####


# In[9]:


####  we can create a scatter plot to see if there is a relationship between age and fare paid by the passengers. 
##### from this, we can determine if the older passengers paid more for their tickets.


plt.scatter(DataFrame['Age'], DataFrame['Fare'])
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()


# In[10]:


###  a stacked bar chart to visualize the count of passengers who survived or not for each passenger class. 
#### from this, we can understand the survival rates of passengers in different classes. 

survived_class_count = DataFrame.groupby(['Survived', 'Pclass']).size().reset_index(name='count')
survived_class_count = survived_class_count.pivot(index='Pclass', columns='Survived', values='count')
survived_class_count.plot(kind='bar', stacked=True)
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.show()


# In[20]:


from sklearn.naive_bayes import GaussianNB
ngnb = GaussianNB()


# In[25]:


X_train = DataFrame.drop('Survived', axis = 1)
Y_train = DataFrame['Survived']
X_train.head(10)


# In[18]:


DataFrame.shape


# In[ ]:




