#!/usr/bin/env python
# coding: utf-8

# In[97]:


#Ans.1
a={}
type(a)


# In[98]:


#Ans.2
b={"foo":42}
b


# In[ ]:


#Ans.3
## Dictionary is an unordered collection of key-value pairs while list is an ordered collection of elements that can be accessed by their indices.


# In[99]:


#Ans.4
## tho this is an error statment 
spam = {'bar':100}
spam['foo']


# In[104]:


#Ans.5

spam ={'cat':2}
'cat' in spam

'cat' in spam.keys()


# In[108]:


#Ans.6


spam ={'cat':2}
'cat' in spam


# In[109]:


spam ={'cat':2}
'cat' in spam.values()


# In[110]:


#Ans.7
spam.setdefault('color','black')
spam


# In[111]:


#Ans8

import pprint
a_dict = [ {'Name': 'Rahul', 'Age': '14', 'Country': 'US'},
  {'Name': 'Raj', 'Age': '36', 'Country': 'India'},
  {'Name': 'Ayush', 'Age': '19', 'Country': 'Australia'},
  {'Name': 'Joe', 'Age': '45', 'Country': 'Brazil'}
]

pprint.pprint(a_dict)


# In[118]:


print(a_dict)

