#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
a=np.array([1,2,3])
b=np.array([(1,2,3,4),(7,8,9,10)],dtype=int)
print(a)
print(b)


# In[4]:


np.zeros(3)


# In[7]:


np.zeros((2,3))


# In[11]:


np.zeros((3,2,4))


# In[12]:


np.full((3,4),2)


# In[13]:


np.random.rand(3,5)


# In[14]:


np.ones((3,4))


# In[15]:


np.eye(4)


# In[17]:


np.save("new_array",a)


# In[18]:


np.load("new_array.npy")


# In[20]:


np.loadtxt("New_file.txt")
np.genfromttxt("New_file.csv",delimiter=',')
np.savetxt("New_file.txt",arr,delimeiter='')
np.savetxt


# In[23]:


np.loadtxt('New_file.txt')


# In[32]:


# np.genfromttxt("New_file.csv",delimiter=',')
arr=[1,23,44]
np.savetxt("New_file.txt",arr,delimiter='2')


# In[34]:


b.size


# In[35]:


b.shape


# In[36]:


b.dtype


# In[37]:


np.copy(b)


# In[42]:


view(dtype)


# In[51]:


b.reshape(4,2)


# In[ ]:




