
# coding: utf-8


# In[2]:


import os
import pandas as pd
import numpy as np


# In[21]:

#reading the csv file
df = pd.read_csv("Data/cricket_matches.csv")


# In[22]:

df.head()


# In[23]:

df_column = df[['home','winner','innings1','innings1_runs','innings2','innings2_runs']]


# In[25]:

df_column.head()


# In[26]:

df1 = df_column[df_column['home'] == df_column['winner']]
df1.head()


# In[27]:

df1['score'] = np.where(df1['home'] == df1['innings1'], df1['innings1_runs'], df1['innings2_runs'])
df1.head()


# In[28]:

total_score = df1['score'].groupby(df1['home']).sum()
total_score.head()


# In[29]:

total_count = df1['score'].groupby(df1['home']).count()



# In[30]:

total_avg = df1['score'].groupby(df1['home']).sum() / df1['score'].groupby(df1['home']).count()



# In[31]:

unique_home = df1['home']


# In[32]:

df2 = pd.DataFrame({ 'score' : total_avg})
df2.head()


# In[33]:

df3 = pd.DataFrame({'home' : df2.index,'score' : total_avg })
df3.head()


# In[36]:

df3.to_csv('Q3_P1.csv',index = False, sep=',')


# In[ ]:



