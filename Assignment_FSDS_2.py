#!/usr/bin/env python
# coding: utf-8

# In[31]:


#Ans.1
## the two values of the Boolean data type are true and false and they are logical operators.

a=True
b=False
print(a)
print(b)


# In[ ]:


#Ans.2
## the three different types of Boolean operators are or , and , not....and the operators are used to compare values.


# In[ ]:


#Ans.3
##  True and True is True.

True and False = False.

False and True = False.

False and False = False.

True or True = True.

True or False = True.

False or True = True.

False or False = False.

Not True = False.

Not False = True.


# In[40]:


#Ans.4

a=(5>4) and (3==5)
print(a)

b=(not(5>4))
print(b)

c=(5>4) or (3==5)
print(c)

d=(5>4) or (3==5)
print(d)

e=((True and True) and (True==False))
print(e)

f=((not(False))or(not(True)))
print(f)


# In[ ]:


#Ans.5
## the six comparision operator are :- ==, !=, <, >, <=, >= .


# In[42]:


#Ans.6
## Equal to operator

a=7
b=5
if (a==b):
    print("true")

else :
    print("false")
    
### Assignment operator (=)

c=1
print("So the c :" ,c)


# In[45]:


#Ans.7

spam = 0
if spam == 10:
    print("eggs")     # 1st
if spam:
    print("bacon")    # 2nd
else:
    print("ham")      # 3rd
    print("spam")
    print("spam")


# In[47]:


#Ans.8

spam = int(input("Enter a number : "))
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")
    


# In[ ]:


#Ans.9
## To stop the running loop we can either interrupt the kernel or make some error or ctrl c.


# In[49]:


#Ans 10
## The break statment will continue its execusion after the loop and continue statment will run too start the statement. 

for i in range(5):
    if(i==3):
        break
    print(i)
print('stopped!')

for i in range(7):
    if(i==5):
        continue
    print(i)
print("continued")


# In[53]:


#Ans.11

for i in range(10):
    print(i)
    
for i in range(0,10):
    print(i)

for i in range(0,10,1):
    print(i)


# In[56]:


#Ans.12
## With for loop.

for i in range(1,11):
    print(i)
print("iNeuron")

### With While loop.

a =1
while a <= 10:
    print(a)
    a+=1


# In[61]:


spam="spam.bacon()"
print(spam)


# In[ ]:




