#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
a = pd.Series([1,3,4,5,6,7])
print(a)


# In[4]:


import numpy as np
a1 = pd.Series([1,2,3,4,np.nan,6])
print(a1)


# In[5]:


dates = pd.date_range('20190601',periods=10)
print(dates)


# In[6]:


lst= pd.date_range('20190601',periods=5)
print(lst)


# In[16]:


a3 = pd.DataFrame({'A':1.,              
                   'B':pd.Timestamp('20190601'),
                   'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                   'D':np.array([3]*4,dtype='int32'),
                   'E':pd.Categorical(["test","train","test","train"]),
                   'F':'foo'})
print(a3)


# In[ ]:


# Turtle is a python feature like a drawing board
# Lines, Square , Star, Rect etc
# Turtle() -- it creates and returns a new turtle object


# In[1]:


import turtle as tt
a1 = tt.Turtle()
tt.forward(100)
tt.done()


# In[1]:


import turtle as tt
a1 = tt.Turtle()
a1.forward(150)
a1.right(90)

a1.forward(150)
a1.right(90)

a1.forward(150)
a1.right(90)

a1.forward(150)
a1.right(90)

tt.done()


# In[1]:


import turtle as tt
a1 = tt.Turtle()
for x in range(40):
    a1.forward(50)
    a1.right(144)
tt.done()


# In[1]:


import turtle as tt
a1 = tt.Turtle()
for i in range(40):
    a1.forward(i*10)
    a1.right(144)
tt.done()


# In[2]:


import turtle as tt
colors = ['red', 'blue', 'orange', 'green', 'yellow', 'purple']
a1 = tt.Turtle()
for x in range(360):
    a1.pencolor(colors[x%6])
    a1.width(x/100+1)
    a1.forward(x)
    a1.left(59)
    
tt.done()


# In[ ]:




