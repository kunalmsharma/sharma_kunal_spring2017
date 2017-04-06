
# coding: utf-8

# In[30]:

import pandas as pd


# In[31]:

df = pd.read_csv("Data/vehicle_collisions.csv")


# In[32]:

df


# In[33]:

df['MONTH'] = pd.DatetimeIndex(df['DATE']).month


# In[35]:

df['YEAR'] = pd.DatetimeIndex(df['DATE']).year


# In[36]:

df.head()


# In[37]:


df16 = df[df['YEAR']==2016] 


dfM16 = df16[df16['BOROUGH']=='MANHATTAN']


dfM16_count = dfM16.groupby(dfM16['MONTH']).agg('count')

 
dfM16_Unicount = dfM16_count['UNIQUE KEY']


# In[38]:

print(dfM16_Unicount)


# In[39]:


dfNYC16_count = df16.groupby([df16['MONTH']]).agg('count')

 
dfNYC16_Unicount = dfNYC16_count['UNIQUE KEY']


# In[40]:

print(dfNYC16_Unicount)


# In[44]:

result = pd.concat([dfM16_Unicount,dfNYC16_Unicount],axis=1)

result.columns.values[0]= "MANHATTAN"
result.columns.values[1]= "NYC"


result['PERCENTAGE']=result[['MANHATTAN']].div(result['NYC'],axis=0)


result['PERCENTAGE']=result['PERCENTAGE'].apply(lambda x:x*100) 

result['MONTH'] = result.index.astype(str).astype(int)

print(result)



# In[46]:

output = result[['MONTH','MANHATTAN','NYC','PERCENTAGE']]



# In[47]:

output.to_csv('Q1_P1.csv',index=False,sep=',')


# In[ ]:



