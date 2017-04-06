
# coding: utf-8

# In[3]:

import pandas as pd



# In[4]:

df = pd.read_csv("Data/employee_compensation.csv")


# In[5]:

df


# In[6]:

test = df.groupby(['Organization Group', 'Department']).mean().reset_index()
#test1 = test['Total Compensation'].groupby(level=0, group_keys=False)


# In[7]:

test


# In[8]:

table = test[['Organization Group','Department','Total Compensation']]


# In[9]:

table


# In[11]:


table_order = table.sort(['Total Compensation'],ascending=False)

table_order_reindexed = table_order.reset_index(drop=True)

table_order_reindexed.head()


# In[12]:

table_order_reindexed.to_csv('Q2_P1.csv',index = False, sep=',')


# In[ ]:



