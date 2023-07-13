#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Ans.1
## [] , this is a empty list .


# In[69]:


#Ans.2 
spam = [2, 4, 6, 8, 10]
spam[2] = "hello" # we have type 2 coz we count from like 0 1 2 .
spam
     


# In[73]:


#Ans.3
spam = ['1', '2','3','4']
spam[int(int('3' * 2) / 11)]


# In[71]:


#Ans.4
spam = ['F', 'S','D','S']
spam[-1]


# In[76]:


#Ans.5
spam=['a','b','c','d','e','f']
print(spam[:2])


# In[77]:


#Ans.6
bacon=["iNeuron", "DS","cat",55]
bacon.index("cat")


# In[79]:


#Ans.7
bacon=["iNeuron", "DS","cat",55]
bacon.append(99)
bacon


# In[82]:


#Ans.8
bacon=["iNeuron", "DS","cat",55]
bacon.remove("cat")
bacon


# In[83]:


#Ans.9

l1 = [78,47]
l2 = [4,63]
# List concatination (+)
l1+l2


# In[84]:


l1 = [7,4]
# List replication (*)
l1*3


# In[85]:


#Ans.10
bacon=["iNeuron", "DS","cat",55]  ## append add the item in the last ,in the list ;
bacon.append("cat") 
bacon


# In[87]:


bacon=["iNeuron", "DS","cat",55]  ## inser replace the item ,in the list ;
bacon.insert(2,"dog") 
bacon


# In[88]:


#Ans.11
bacon=["iNeuron", "DS","cat",55]  
bacon.remove("cat") 
bacon


# In[91]:


bacon=["iNeuron", "DS","cat",55] 
bacon.pop() ## pop remove the last item frm the list 
bacon


# In[ ]:


#Ans.12
## List values and tring values are not identical but they have some similarities in sliciing, sequences,indexing and some common methods are ;len(),count(),index()


# In[ ]:


#Ans.13
## Tuples ()- they are immutable they cannot change values.
## List [] - They are mutable they can change values for eg add remove 


# In[93]:


#Ans.14
a_tuple=(42)
a_tuple


# In[94]:


#Ans.15
l=[1]
l1=tuple(l)
print(l)


# In[96]:


t=(1,2)
t1=list(t)
t1


# In[ ]:


#Ans.16
## variable then list values raher then contail references to list values.


# In[ ]:


#Ans.17
## copy.copy() performs a shallow copy creating a new object with references to the original object's nested objects. copy.deepcopy() performs a deep copy creating a new object with recursively copied and independent nested objects.


# In[ ]:





# In[ ]:




