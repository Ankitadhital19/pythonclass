#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[ ]:


file = open("info.csv",'x')
file.close()


# In[1]:


info = ""
file = open("info.csv",'w')
file.write("name,age,add\n")
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name = ")
    age = int(input("Enter age = "))
    add = input("Enter add = ")
    info = info+f"{name},{age},{add}\n"
file.write(info)
file.close()


# In[2]:


import pandas as pd
df = pd.read_csv('info.csv')
df


# In[5]:


df = pd.read_csv('info.csv',nrows = 3)
df


# In[6]:


df = pd.read_csv('info.csv')
df.head()


# In[7]:


df.tail()


# In[8]:


df= pd.read_csv('info.csv',usecols=['name','add']) #data frame
df


# In[9]:


df= pd.read_csv('info.csv',usecols=['name','age']) #data frame
df


# In[10]:


df = pd.read_csv('info.csv')
df


# In[11]:


df.iloc[1:5]


# In[12]:


df['add']


# In[16]:


df[df['add'] == "Chitwan"]


# In[17]:


df[(df['add'] == "Chitwan")& (df['age']>=20)]


# In[18]:


df[(df['add'] == "Chitwan") | (df['age']>=20)]


# In[19]:


info = ""
file = open("info.csv",'w')
file.write("name,age,add\n")
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name = ")
    age = int(input("Enter age = "))
    add = input("Enter add = ")
    info = info+f"{name},{age},{add}\n"
file.write(info)
file.close()


# In[35]:


import pandas as pd
df = pd.read_csv('info.csv')
df


# In[23]:


df[(df['add'] == "ktm") | (df['age']>=30)]


# In[24]:


df


# In[36]:


df['sn'] = [i for i in range(1,7)] #serial.no


# In[37]:


df


# In[41]:


data = {'sn':[7,8],'age':[22,33],'name':['Akash','Aayush'], 'add':['lalitpur','ktm']}
data


# In[42]:


df1 = pd.DataFrame(data)
df1


# In[43]:


df = pd.concat([df,df1])
df


# In[44]:


df.to_csv('new_data.csv')


# In[47]:


df = pd.read_csv('new_data.csv',usecols = ['sn','name','age','add'],index_col = 'sn')
df


# In[48]:


df.drop([3,4],axis = 0)


# In[50]:


df.drop(["age"],axis = 1)


# In[ ]:




