#!/usr/bin/env python
# coding: utf-8

# In[23]:


#Ans.1
## print(),len(),int(),input() are the some examples of in-build function

A="iNeuron"
print(A)  ## Example of a built-in function.


## By using def we can find user definr function.

def multiply_number(a,b):
    return a*b

solution = multiply_number(7,4)
print(solution)


# In[27]:


#Ans.2

def intro(name, age):
    print(f"Heyy, {name} I am {age} years old.")

intro("Jack", 32)  ## Example of positional arguments.


def intro(name, age):
    print(f"Heyy, {name} I am {age} years old.")

intro(name="Jack", age=32)  ## Example of keyword arguments.


# In[30]:


#Ans.3
## The purpose of the return statement in a function is to specify the value or values to be returned back to the caller of the function allowing for the use or assignment of the result in the calling code.

def check_even_odd(number):
    if number%2==0:
        return "Even"
    else:
        return "Odd"
a = check_even_odd(10)
print(a)  

b = check_even_odd(7)
print(b) 


# In[40]:


#Ans.4
## Lambda functions in python are anonymous functions that can be defined without a name they are used for small one-time operations and are created using the `lambda` keyword.

my_list = [(4, 7), (9, 3), (7, 3), (4, 3)]
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)


# In[43]:


#Ans.5
## Scope in Python refers to the visibility and accessibility of variables functions have local scope where variables defined inside the function are only accessible within that function while global scope allows variables to be accessed throughout the entire module.
x=45
def my_function():
    x = 45
    print(x)

my_function()   ## Local scope


# In[45]:


y = 18
def my_function():
    global y
    y = 20 
    print(y)

my_function() ## Global scope


# In[48]:


#Ans.6

def get_values():
    a = 78
    b = 55
    c = 41
    return a,b,c
a1, b1, c1 = get_values()  
print(a1, b1, c1)


# In[ ]:


#Ans.7
## In python function arguments are passed by assignment, which means they behave differently for mutable and immutable objects immutable objects (numbers, strings) are effectively passed by value as modifications inside the function don't affect the original value mutable objects (lists, dictionaries) are passed by reference so changes inside the function affect the original object it's important to consider this behavior when working with function arguments in python.


# In[50]:


#Ans.8
import numpy as np

def perform_oprns(number):
    log_value = np.log(number)
    exp_value = np.exp(number)
    power_value = np.power(2, number)
    sqrt_value = np.sqrt(number)
    return log_value, exp_value, power_value, sqrt_value
result = perform_oprns(4)
print(result)


# In[52]:


#Ans.9
def name(full_name):
    names = full_name.split()
    first_name = names[0]
    last_name = names[-1]
    return first_name, last_name

# Example usage:
Name = "brad smith"
first, last = name(Name)
print("First Name:", first)
print("Last Name:", last)


# In[ ]:





# In[ ]:





# In[ ]:




