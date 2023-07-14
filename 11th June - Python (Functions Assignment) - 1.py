#!/usr/bin/env python
# coding: utf-8

# In[53]:


#Ans.1
##  A lambda function is a small anonymous function that can be defined without a name.

def square(x):
    return x**2 # Regular function

# Lambda function
lambda_square = lambda x: x**2


# In[54]:


#Ans.2
## YEs a lamda function in python can have multiple arguments use multiple arguments in a lambda function by separating them with comma.

add_numbers = lambda x, y: x + y  # Lambda function with multiple arguments.

result = add_numbers(3, 5)
print(result)  


# In[55]:


#Ans.3
## They are typically used in scenarios where a small one-time function is needed.

names = ["Jake", "Ayush", "ALi", "Brad", "Joe"]

# Sorting the names.
sorted_names = sorted(names, key=lambda x: x[-1])
print(sorted_names)


# In[ ]:


#Ans.4
## Advantages - Lambda functions offer concise syntax for defining simple functions inlin making code more readable and reducing the need for separate named functions they are especially useful for functional programming operations like mapping filtering and reducing.

## Limitation - They are restricted to a single expression lacking support for multiple statements or complex logic they are anonymous which can make debugging and understanding code more difficult.


# In[56]:


#Ans.5
## This is possible due to the concept of closures which allows lambda functions to remember and access the values of variables in their enclosing lexical scope.

def outer_function():
    x = 85
    lambda_func = lambda y: x + y
    return lambda_func

closure = outer_function()
result = closure(5)
print(result)  


# In[57]:


#Ans.6

square = lambda x: x**2

result = square(8)
print(result)  


# In[59]:


#Ans.7
numbers = [2, 8, 17, 99, 7]
max_value = max(numbers, key=lambda x: x)
print(max_value)  


# In[60]:


#Ans.8
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# In[61]:


#Ans.9
strings = ["Ayush", "Shubham", "Jin", "Riya"]

sorted_strings = sorted(strings, key=lambda x: len(x))
print(sorted_strings)


# In[62]:


#Ans.10
list1 = [55, 8, 7, 8, 3]
list2 = [34, 11, 55, 7, 7]

common_elements = list(filter(lambda x: x in list1, list2))
print(common_elements)


# In[1]:


#Ans.11
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
result = factorial(7)
print(result)


# In[3]:


#Ans.12
def fibonacci(n):
    if n <= 0:
        raise ValueError("Input should be a positive integer.")
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
result = fibonacci(7)
print(result)


# In[5]:


#Ans.13
def list_sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + list_sum(lst[1:])
result = list_sum([11, 22, 33, 44])
print(result)


# In[7]:


#Ans.14
def is_palindrome(string):
    if len(string) <= 1:
        return True
    else:
        if string[0] == string[-1]:
            return is_palindrome(string[1:-1])
        else:
            return False
result = is_palindrome("raduar")
print(result)


# In[8]:


#Ans.15
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
result = gcd(77, 26)
print(result)


# In[ ]:




