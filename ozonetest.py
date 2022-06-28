#!/usr/bin/env python
# coding: utf-8

# # Analyse de données de la météo d'un dataset de kaggle

# In[10]:


import pandas as pd 
import matplotlib.pyplot as plt 
import pylab


# In[11]:


ozone = pd.read_csv("ozoneNA.csv", sep=";")


# In[12]:


ozone.head(10)


# In[13]:


ozone.shape


# In[14]:


ozone.info()


# # Les doublons (identifications)

# In[15]:


ozone.duplicated().sum()


# # Données NaN

# In[16]:


ozone.isna()


# In[17]:


ozone.isna().sum()


# # Statistique descriptives sans doublons 

# In[18]:


ozone.describe()


# In[ ]:





# 
# # Remplacement des valeurs manquantes

# In[22]:


#Remplacement des valeurs manquantes par 0
ozone1 = ozone.fillna(0)


# In[23]:


ozone1.head(15)


# In[21]:


ozone1.isna().sum()


# In[24]:


ozone1.describe()


# # GRAPH

# In[31]:


data=ozone1["maxO3"].value_counts()
data


# In[32]:


plt.bar(data.index, data, color =["green"])
plt.rcParams["figure.figsize"]=[20,20]
plt.xlabel("Quantité maximum d'ozone")
plt.ylabel("Nombre de fois")
plt.grid()
plt.title("Nombre de fois ou la quantité maximum d'ozone à atteint une certaine valeur  ")


# # Boxplot T,Ne,Vx

# In[185]:


data1= ozone1["T9"]
data2= ozone1["T12"]
data3= ozone1["T15"]

BoxName= ["T9","T12","T15"]

data =[data1,data2,data3]
plt.rcParams["figure.figsize"]=[16,9]
plt.boxplot(data)

plt.ylim(0,40)
pylab.xticks([1,2,3],BoxName)

plt.savefig("Température.png")
plt.title("Représentation des statistiques descriptives des températures")
plt.grid()
plt.show()


# In[184]:


data1= ozone1["Ne9"]
data2= ozone1["Ne12"]
data3= ozone1["Ne15"]

BoxName= ["Ne9","Ne12","Ne15"]

data =[data1,data2,data3]
plt.rcParams["figure.figsize"]=[16,9]
plt.boxplot(data)

plt.ylim(0,20)
pylab.xticks([1,2,3],BoxName)

plt.savefig("Nébulosité.png")
plt.title("Représentation des statistiques descriptives des nébulosités")
plt.grid()
plt.show()


# In[200]:


data1= ozone1["Vx9"]
data2= ozone1["Vx12"]
data3= ozone1["Vx15"]

BoxName= ["Vx9","Vx12","Vx15"]

data =[data1,data2,data3]
plt.rcParams["figure.figsize"]=[16,9]
plt.boxplot(data)

plt.ylim(-15,10)
pylab.xticks([1,2,3],BoxName)

plt.savefig("Vitesse du vent.png")
plt.title("Représentation des statistiques descriptives de la vitesse du vent")
plt.grid()
plt.show()


# In[ ]:




