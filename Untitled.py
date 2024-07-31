#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


data = pd.read_csv('C:\\Users\\Shri Hema\\Downloads\\01.Data Cleaning and Preprocessing.csv')


# In[4]:


type(data)


# In[5]:


data.info #concise summary


# In[6]:


data.describe() #descriptive statistics


# In[7]:


data = data.drop_duplicates()
data


# In[8]:


data.isnull()


# In[9]:


data.isnull().sum()


# In[10]:


data.notnull()


# In[11]:


data.isnull().sum().sum()


# In[14]:


data2 = data.fillna(value=0)
data2


# In[16]:


data2.isnull().sum().sum()


# In[17]:


data3 = data.fillna(method='pad')
data3


# In[19]:


data4 = data.fillna(method='bfill')
data4


# In[20]:


import numpy as np
from scipy import stats


# In[21]:


data2.columns


# In[23]:


data2.drop(['Observation'], axis=1, inplace=True)
data2.columns


# In[24]:


Q1= data2.quantile(0.25)
Q3= data2.quantile(0.75)
IQR=Q3-Q1
print(IQR)


# In[25]:


data2=data2[~((data2<(Q1-1.5*IQR))|(data2>(Q3+1.5*IQR))).any(axis=1)]
data2


# In[27]:


data2.describe()


# In[ ]:


# 

