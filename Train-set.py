#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set_theme(color_codes = True)


# In[6]:


#### import the dataset
DataFrame = "C:/Users/Ayieko/Documents/EMILY/linkedin/archive/Train-Set.csv"
DataFrame = pd.read_csv(DataFrame)
print(DataFrame)


# In[7]:


DataFrame.head()


# In[8]:


### let's check the number of unique values
DataFrame.select_dtypes(include = 'object').nunique()


# In[10]:


### we can drop product IDs because they are unnecessary
DataFrame.drop(columns = 'ProductID', inplace = True)
DataFrame.head()


# In[14]:


### list of categorical variables to plot
cat_vars = ['FatContent', 'ProductType', 'OutletID', 'OutletSize', 'LocationType', 'OutletType']


### we can create a figure of barplots
fig, axs = plt.subplots(nrows = 2, ncols = 3, figsize = (20, 10))
axs = axs.flatten()

######### we can create a barplot for each categorical variable
for i, var in enumerate(cat_vars):
    sns.barplot(x = var, y = 'OutletSales', data = DataFrame, ax = axs[i])
    axs[i].set_xticklabels(axs[i].get_xticklabels(), rotation = 0)

    
############# we can adjust spacing between the subplots
fig.tight_layout()

plt.show()


# In[16]:


cat_vars  = ['FatContent', 'OutletID', 'OutletSize', 'LocationType', 'OutletType']


##### we can create figure and axes
fig, axs = plt.subplots(nrows = 2, ncols = 3, figsize = (15, 15))

### we can create  apie chart for every categorical variable
for i, var in enumerate(cat_vars):
    if i < len(axs.flat):
        ######### count the numbers of occurances
        cat_counts = DataFrame[var].value_counts()
        
        ##### create a pie chart
        axs.flat[i].pie(cat_counts, labels = cat_counts.index, autopct = '%1.1f%%', startangle = 90)
        
        #### set titles for the plots
        axs.flat[i].set_title(f'{var} Distribution')

#### adjust the spacing between the plots
fig.tight_layout()
fig.delaxes(axs[1][2])
        
    
##### display the plots
plt.show()


# In[23]:


######   we can create boxplots for the data
num_vars = ['Weight', 'ProductVisibility', 'MRP']

fig. axs = plt.subplots(nrows=1, ncols=3, figsize=(20, 10))
axs = axs.flatten()

for i, var in enumerate(num_vars):
    sns.boxplot(x=var, data=DataFrame, ax=axs[i])
    
#### adjust the space between the plots
fig.tight_layout()

plt.show()


# In[22]:


num_vars = ['Weight', 'ProductVisibility', 'MRP']

fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(20, 10))
axs = axs.flatten()

for i, var in enumerate(num_vars):
    sns.violinplot(x=var, data=DataFrame, ax=axs[1])
    
#### adjust the spaces between the plots
fig.tight_layout()

plt.show()


# In[20]:


num_vars = ['Weight', 'ProductVisibility', 'MRP']

fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(20, 10))
axs = axs.flatten()

for i, var in enumerate(num_vars):
    sns.histplot(x=var, data=DataFrame, ax=axs[i])
    
### adjust space between the plots
fig.tight_layout()

plt.show()


# In[24]:


sns.lineplot(data=DataFrame, x="EstablishmentYear", y="OutletSales", hue="OutletSize")


# In[27]:


sns.lineplot(data=DataFrame, x="EstablishmentYear", y="OutletSales", hue="LocationType")


# In[28]:


sns.lineplot(data=DataFrame, x="EstablishmentYear", y="OutletSales", hue="FatContent")


# In[29]:


sns.lineplot(data=DataFrame, x="EstablishmentYear", y="OutletSales", hue="OutletType")


# In[30]:


### we can check missing values
check_missing = DataFrame.isnull().sum() * 100 / DataFrame.shape[0]
check_missing[check_missing > 0].sort_values(ascending=False)


# In[31]:


DataFrame.shape


# In[32]:


###### fill the weight size with mean
DataFrame['Weight'] = DataFrame['Weight'].fillna(DataFrame['Weight'].mean())


# In[33]:


unique_sizes_train3 = DataFrame.groupby('OutletType')['OutletSize'].unique()
unique_sizes_train3


# In[34]:


### fill null value in OutletSize where OutletType == Grocery store with 'Small' value
DataFrame.loc[(DataFrame['OutletType'] == 'Grocery Store') & (DataFrame['OutletSize'].isna()), 'OutletSize'] = 'Small'


# In[35]:


#### let's identify any missing values
check_missing = DataFrame.isnull().sum() * 100 / DataFrame.shape[0]
check_missing[check_missing > 0 ].sort_values(ascending=False)


# In[36]:


### drop 'OutletSize' null value row
DataFrame.dropna(subset=['OutletSize'], inplace=True)
DataFrame.shape


# In[37]:


DataFrame.head()


# In[ ]:




