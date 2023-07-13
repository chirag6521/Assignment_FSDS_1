#!/usr/bin/env python
# coding: utf-8

# In[119]:


#Ans.1
##  Keywords in Python are reserved words that have special meanings and purposes within the language.
import keyword

all_keywords = keyword.kwlist
print(all_keywords)


# In[ ]:


#Ans.2
## Start with a letter or underscore, and be case-sensitive.
## Avoid reserved keywords, spaces, and special characters; choose descriptive names following Python's naming conventions.


# In[ ]:


#Ans.3
## Use descriptive names that accurately convey the purpose of variables follow snake_case for multi-word variable names.


# In[ ]:


#Ans.4
## Using a keyword as a variable name in python will result in a 'SyntaxError'.keywords are reserved and have predefined meanings in the language to avoid this error choose variable names that do not conflict with python's keywords.


# In[ ]:


#Ans.5
## If is used to define function.


# In[ ]:


#Ans.6
## these are some special character lik (\n) for new line and (\t) for new tab.


# In[120]:


#Ans.7
homogeneous_list = [1, 2, 3, 4, 5]
heterogeneous_set = {"dog", 10, 3}
homogeneous_tuple = ("apple", "banana", "watermelon")


# In[122]:


#Ans.8
## Mutable data types in python can be modified or changed after they are created while immutable data types cannot be altered once they are assigned.
## examples of mutable data type

my_list = [1, 2, 3]
my_list.append(4)

my_dict = {"key1": "iNeuron", "key2": "chirag"}
my_dict["key3"] = "singh"

## examples of immutable data type

my_string = "Hello"
new_string = my_string + " World"

my_tuple = (1, 2, 3)


# In[123]:


#Ans.9
rows = 5

for i in range(rows):
    for j in range(i+1):
        print("*", end="")
    print()


# In[124]:


#Ans.10
rows = 5 

while rows > 0:
    print("|" * rows)
    rows -= 1

