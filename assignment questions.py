#!/usr/bin/env python
# coding: utf-8

# In[14]:


def reverseFib(x):
    a = [0] * x
    a[0] = 0
    a[1] = 1
    for i in range(2,x):
        a[i] =a[i - 2]+ a[i -1] 
    for i in range(x - 1,-1,-1):
        print(a[i],end = ' ')
x = 5
reverseFib(x)
      


# In[ ]:





# In[ ]:





# In[ ]:




