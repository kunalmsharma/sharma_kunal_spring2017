
# coding: utf-8

# In[11]:

import pandas as pd


# In[12]:

df = pd.read_csv("Data/vehicle_collisions.csv")


# In[13]:

df


# In[14]:

dfl = df[['UNIQUE KEY','BOROUGH']]
dfv = df[['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']]
dfv = dfv.notnull()
dfv = dfv.applymap(lambda x:1 if x else 0)
new_df = pd.concat([dfl,dfv],axis=1)

new_df


# In[6]:

dfc = new_df.groupby('BOROUGH').sum()
dfc


# In[15]:

dfc['ONE_VEHICLE_INVOLVED'] =  dfc['VEHICLE 1 TYPE']-dfc['VEHICLE 2 TYPE']

dfc['TWO_VEHICLES_INVOLVED'] =  dfc['VEHICLE 2 TYPE']-dfc['VEHICLE 3 TYPE']

dfc['THREE_VEHICLES_INVOLVED'] =  dfc['VEHICLE 3 TYPE']-dfc['VEHICLE 4 TYPE']


dfc['MORE_VEHICLES_INVOLVED'] = dfc['VEHICLE 4 TYPE'] - dfc['VEHICLE 5 TYPE'] + dfc['VEHICLE 5 TYPE'] 

dfc = dfc[['ONE_VEHICLE_INVOLVED','TWO_VEHICLES_INVOLVED','THREE_VEHICLES_INVOLVED','MORE_VEHICLES_INVOLVED']]
dfc


# In[8]:

dfc.to_csv("Q1_p2.csv",index=True,sep=',')


# In[ ]:



