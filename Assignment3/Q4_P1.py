
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np



# In[2]:

output_df=pd.DataFrame(columns=['Awards','Awards_won','Awards_nominated','Prime_awards_Nominated','Oscar_awards_Nominated','Gloden_Globe_Nominate','BAFTA_Awards_Nominated','Prime_awards_Won','Oscar_awards_Won','Gloden_Globe_Won','BAFTA_Awards_Won'])


# In[4]:

df=pd.read_csv('Data/movies_awards.csv')


# In[5]:

df['Awards']=df['Awards'].str.replace(r'&','.')   
df['Awards']=df['Awards'].str.replace(r'Another','') 
df=df.drop(df.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18]],axis=1)


# In[6]:

for index, row in df.iterrows():
    wins=0
    nominations=0
    Oscar_nominations=0
    Oscar_won=0
    Golden_Globe_won=0
    Golden_Globe_nominations=0
    Primetime_nominations=0
    Primetime_won=0
    BAFTA_nominations=0
    BAFTA_won=0
    if type(row['Awards'])!=float:
        row['Awards']=row['Awards'].split('.')
        for i in range(len(row['Awards'])-1):
            if 'win' in row['Awards'][i]:
                wins+=int(row['Awards'][i].split()[0])
            if 'nomination' in row['Awards'][i]:
                nominations+=int(row['Awards'][i].split()[0])
            if 'Oscar' in row['Awards'][i]:
                if 'Nominated' in row['Awards'][i]:
                    Oscar_nominations+=int(row['Awards'][i].split()[2])
                    nominations+=Oscar_nominations
                if 'Won' in row['Awards'][i]:
                    Oscar_won+=int(row['Awards'][i].split()[1])
                    wins+=Oscar_won
            if 'Golden Globe' in row['Awards'][i]:
                if 'Nominated' in row['Awards'][i]:
                    Golden_Globe_nominations+=int(row['Awards'][i].split()[2])
                    nominations+=Golden_Globe_nominations
                if 'Won' in row['Awards'][i]:
                    Golden_Globe_won+=int(row['Awards'][i].split()[1])
                    wins+=Golden_Globe_won
            if 'Primetime Emmy' in row['Awards'][i]:
                if 'Nominated' in row['Awards'][i]:
                    Primetime_nominations+=int(row['Awards'][i].split()[2])
                    nominations+=Primetime_nominations
                if 'Won' in row['Awards'][i]:
                    Primetime_won+=int(row['Awards'][i].split()[1])
                    wins+=Primetime_won
            if 'BAFTA' in row['Awards'][i]:
                if 'Nominated' in row['Awards'][i]:
                    BAFTA_nominations+=int(row['Awards'][i].split()[2])
                    nominations+=BAFTA_nominations
                if 'Won' in row['Awards'][i]:
                    BAFTA_won+=int(row['Awards'][i].split()[1])
                    wins+=BAFTA_won
        output_df=output_df.append(pd.Series([row['Awards'],wins,nominations,Primetime_nominations,Oscar_nominations,Golden_Globe_nominations,BAFTA_nominations,Primetime_won,Oscar_won,Golden_Globe_won,BAFTA_won],index=['Awards','Awards_won','Awards_nominated','Prime_awards_Nominated','Oscar_awards_Nominated','Gloden_Globe_Nominate','BAFTA_Awards_Nominated','Prime_awards_Won','Oscar_awards_Won','Gloden_Globe_Won','BAFTA_Awards_Won']),ignore_index=True)


# In[7]:

print(output_df.head())


# In[9]:

output_df.to_csv('Q4_P1.csv')


# In[ ]:



