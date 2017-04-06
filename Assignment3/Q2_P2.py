
# coding: utf-8

# In[14]:

import pandas as pd
import numpy as np
import os
import calendar

df = pd.read_csv("Data/employee_compensation.csv")


# In[15]:

compensation=df[(df['Year Type']=='Calendar')]
compensation=pd.DataFrame(compensation.groupby(['Employee Identifier','Job Family']).mean())

compensation.drop(['Year', 'Organization Group Code','Union Code'], axis=1, inplace=True)
compensation.head()


# In[16]:

ot=compensation[(compensation['Overtime']>(.05*compensation['Salaries']))]
ot.head()


top_family=ot.groupby([ot.index.get_level_values(1)]).mean()

output=top_family[['Total Benefits','Total Compensation']]
output['Percent_Total_Benefit']=100*(output['Total Benefits']/output['Total Compensation'])
output=output.sort_values(['Percent_Total_Benefit'], ascending=[False])
output.head(5)


# In[17]:

output.to_csv('Q2_P2.csv',index = True, sep=',')


# In[ ]:



