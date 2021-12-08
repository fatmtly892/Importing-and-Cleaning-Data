#!/usr/bin/env python
# coding: utf-8

# In[23]:


#importing liberaries 
import pandas as pd



# In[24]:


#importing data
df= pd.read_csv('IMDB_Movies.csv')
df


# In[25]:


df.info()


# In[26]:


#cleaning data
#Missing Values
df.isnull().sum()


# In[27]:


df = df.dropna(subset=['director_name'])
df


# In[28]:


#Dealing with Duplicates
df.duplicated()


# In[30]:


df.drop_duplicates(subset=['director_name'])
df


# In[32]:


df.dtypes


# In[ ]:




