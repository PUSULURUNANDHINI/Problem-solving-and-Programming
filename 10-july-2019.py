#!/usr/bin/env python
# coding: utf-8

# In[4]:


d1= {"Name":"Gitam","Emailid":"gitam@gmail.com","address":"Hyderabad"}
print(d1)


# In[5]:


d1['Emailid']


# In[6]:


d1["Name"]


# In[8]:


d1['Emailid'] = 'Gitam-Python@gmail.com'


# In[9]:


d1['Emailid']


# In[11]:


del d1['Emailid']


# In[12]:


d1


# In[13]:


d1.keys()


# In[14]:


d1.values()


# In[15]:


d1.items()


# In[16]:


t =(1,2,3,4,5,6)
t 
type(t)


# In[22]:


contacts = {}
def addcontact(name,phone):
    if name not in contacts:
        contacts[name] = phone
        print("contact details are added")
    else:
            print("contact details are already exist")
    return
addcontact('Nandhini','9876543210')
addcontact('harini','3456798237')
addcontact('Nandhini','9876543210')


# In[25]:


def searchcontact(name):
    if name in contacts:
        print(name, ":",contacts[name])
    else:
            print("%s does not exists" % name)
    return
searchcontact('Nandhini')


# In[ ]:


def importcontact(newcontacts):
    contacts.update(newcontacts)
    print(len(newcontacts.keys()),"contacts added success"
          return
new contacts = {'nandhini':1234567890,}


# In[26]:


def deletecontact(name,phone):
    if name in contacts:
        contacts[name] = phone
        print(name,"updated succesfully")
    else:
            print(name,"Not exists")
    return
deletecontact('Nandhini',1234567890)
            


# In[49]:


s2 = "python Programming"
s3 = "Python programming"
print(s2.istitle())
print(s3.istitle())


# In[50]:


s1 = " "
s2 = "py th on"
print(s1.isspace())
print(s2.isspace())


# In[51]:


s1 = "1234"
s2 = "Apploication1234"
print(s1.isnumeric())
print(s2.isnumeric())


# In[65]:


s1 = 'python'
print(s1.join(0)


# In[59]:


s2 = " python programming easy to learn"
print(s2. split())

