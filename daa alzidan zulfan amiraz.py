#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np 


# In[20]:


print(np.__version__)


# # Big O Notation
# ## 1. constant time (0(1)) complexity
# if an algorithm takes the same amount of time to run, independent of the size of the input data, it is said to run in constant time. it is represented by 0(1)

# In[21]:


def getFirst(myList):
    return myList[0]


# In[22]:


getFirst([1,2,3])


# ## 2. Linear time (O(n)) complexity
# an algorithm is said to have a complexity of linear time, represented by O(n), if the execution time is directly proportional to the size of the input.

# In[23]:


def getSum(myList):
    sum = 0 
    for item in myList:
        sum = sum+item
    return sum
#perhatikan posisi return


# In[24]:


getSum([1,2,3,4])


# ## 3. Quadratic time ()(n^2)) complexity
# an algorithm is said to run in quadratic time if the execution time of an algorithm is proportional to the square of the input size

# In[25]:


def getSum(myList):
    sum = 0
    for row in myList:
        for item in row:
            sum += item
    return sum


# In[26]:


getSum([[1,2,5],[3,4,7]])


# ## 4. Logarithmic time (0(logn)) complexity
# an algorithm is said to run in logarithmic time if the execution time of the algorithm is proportional to the logarithm of the input size.

# In[36]:


def searchBinary(myList,item):
    first = 0
    last = len(myList)-1
    foundFlag = False
    while(first<=last and not foundFlag):
        mid = (first + last)//2
        if myList[mid] == item :
            foundFlag = True
        else:
            if item < myList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return foundFlag


# In[37]:


searchBinary([8,9,10,100,1000,2000,3000], 10)


# In[38]:


searchBinary([8,9,10,100,1000,2000,3000], 5)

