#!/usr/bin/env python
# coding: utf-8

# ### Standard Libraries
# * File I/O
# * Regular Expression
# * Datetime
# * Math(Numerical and mathematical)

# ### File Handling in python
# * file- Document containing information resides on the permanent storage
# * Different types of files - bd.doc,pdf,csv and etc...
# * Input - keyboard
# * Output - File

# ### Modes of the file I/O
# * 'w'- This mode is used to file writing
#  *  -- If the file is not present first it creates the file and write so me data to it
# 

# In[1]:


# Function to create a file and write
def createfile(filename):
    f = open(filename,'w')
    for i in range(10):
        f.write('this is %d line\n' %i)
    print('file is created and data has written')
    return
createfile('file.txt')
        


# In[2]:


ls


# In[3]:


def createfile(filename):
    f = open(filename,'w')
    f.write
    print('file is created and data has written')
    return
createfile('file.txt')


# In[8]:


def appendData(filename):
    f = open(filename,'a')
    for i in range(10):
        print('This is %d line \n'% i)
    print("File is created and successfully data is written")
    return
appendData('file2.txt')


# In[9]:


def appendData(filename):
    f = open(filename,'a')
    for i in range(10):
        f.write("This is %d line\n" % i)
    print("File is created and successfully data is written")
    return
appendData('file2.txt')


# In[11]:


def appendData(filename):
    f = open(filename,'a')
    f.write("New Line 1 \n")
    f.write("New Line 2 \n")
    print("File is created and successfully data is written")
    return
appendData('file2.txt')


# In[13]:


# Function to read of the file 
def readfiledata(filename):
    f = open(filename,'r')
    if f.mode == 'r':
        x = f.read()
        print(x)
    f.close
    return
readfiledata('file2.txt')


# In[1]:


# Function to read of the file 
def fileoperations(filename,mode):
    with open(filename,'r') as f:
        if f.mode == 'r':
            data = f.read()
            print(data)
        elif f.mode == 'a':
            f.write('Data to the file\n')
            print('The data is successfully written')
    f.close()
    return
filename = input('Enter the filename')
mode = input('Enter the mode of the file')
fileoperations(filename,mode)


# In[7]:


# Character count from the given file
def charcount(filename):
    with open(filename,'r') as f:
        if f.mode=='r':
            x=f.read()
            li=list(x)
    return len(li)
filename=input('Enter the filename:')
charcount(filename)


# In[11]:


# Function to find the no of lines in the input file
# Input -- filename(file2.txt)
# Output -- No of lines(12)
def countOflines(filename):
    C
            li = x.split("\n")
    return len(li)
filename = input("Enter the filename :")
countOflines(filename)


# In[14]:


def casecount(filename):
    cntUpper = 0
    cntLower = 0
    with open(filename,'r') as f:
        if f.mode == 'r':
            x = f.read()
            li = list(x)
    for i in li:    
        if i.isupper():
            cntUpper += 1 
        elif i.islower():
            cntLower += 1
    output = 'Upper Case ={0} , Lower Case ={1}'.format(cntUpper,cntLower)
    return output
filename = input("Enter the filename :")
casecount(filename)


# ### math,  random, os
# - os package it contains the certain methods which works on OS

# In[16]:


ls

